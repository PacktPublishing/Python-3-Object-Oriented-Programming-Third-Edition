input_strings = ["1", "5", "28", "131", "3"]
# without comprehension
output_integers = []
for num in input_strings:
    output_integers.append(int(num))
print(output_integers)


# with comprehension
output_integers = [int(num) for num in input_strings]
print(output_integers)

# with filter
output_integers = [int(num) for num in input_strings if len(num) < 3]
print(output_integers)
