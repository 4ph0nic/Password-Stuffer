import itertools

def generate_combinations(s):
    chars = list(s)
    results = []
    for i in range(1, len(chars) + 1):
        results.extend([''.join(combo) for combo in itertools.combinations(chars, i)])
    return results

input_string = input("Please enter a password to generate combinations: ")
combinations = generate_combinations(input_string)
print("All possible combinations of '{}' are:".format(input_string))
with open("combinations.txt", "w") as f:
    for combination in combinations:
        print(combination)
        f.write(combination + "\n")
print("Output written to combinations.txt")
