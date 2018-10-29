def tally():
    score = 0
    while True:
        increment = yield score
        score += increment
