"""
In the 2nd edition of Python 3 Object Oriented Programming, I presented the
case study using coroutines. In the third edition, I switched to a generator
based implementation instead. It is extremely unusual to use coroutines for
this purpose, and the generator implementation is actually simpler to
understand, read, and maintain. It's also substantially more object oriented.

This file contains the coroutine based implementation. I am including it here
for historical purposes in case anyone has an academic interest in this
implementation.
"""

import csv
from random import random
import math
from collections import Counter

dataset_filename = "colors.csv"


def load_colors(filename):
    with open(filename) as dataset_file:
        lines = csv.reader(dataset_file)
        for line in lines:
            yield tuple(float(y) for y in line[0:3]), line[3]


def generate_colors(count=100):
    for i in range(count):
        yield (random(), random(), random())


def color_distance(color1, color2):
    channels = zip(color1, color2)
    sum_distance_squared = 0
    for c1, c2 in channels:
        sum_distance_squared += (c1 - c2) ** 2
    return math.sqrt(sum_distance_squared)


def nearest_neighbors(model_colors, num_neighbors):
    model = list(model_colors)
    target = yield
    while True:
        distances = sorted(
            ((color_distance(c[0], target), c) for c in model)
        )
        target = yield [d[1] for d in distances[0:num_neighbors]]


def name_colors(get_neighbors):
    color = yield
    while True:
        near = get_neighbors.send(color)
        name_guess = Counter(n[1] for n in near).most_common(1)[0][0]
        color = yield name_guess


def write_results(filename="output.csv"):
    with open(filename, "w") as file:
        writer = csv.writer(file)
        while True:
            color, name = yield
            writer.writerow(list(color) + [name])


def process_colors(dataset_filename="colors.csv"):
    model_colors = load_colors(dataset_filename)
    get_neighbors = nearest_neighbors(model_colors, 5)
    get_color_name = name_colors(get_neighbors)
    output = write_results()
    next(output)
    next(get_neighbors)
    next(get_color_name)

    for color in generate_colors():
        name = get_color_name.send(color)
        output.send((color, name))


process_colors()
