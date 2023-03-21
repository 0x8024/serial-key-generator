import random
import json
import os

def generate_random_string():
    string = ""
    for i in range(9):
        string += random.choice("abcdefghijklmnopqrstuvwxyz")
    string += "-"
    for i in range(9):
        string += random.choice("abcdefghijklmnopqrstuvwxyz")
    string += "-"
    for i in range(9):
        string += random.choice("abcdefghijklmnopqrstuvwxyz")
    return string

num_strings = int(input("How many random strings do you want to generate? "))

random_strings = [generate_random_string() for _ in range(num_strings)]

filename = "random_strings.json"

if not os.path.exists(filename):
    with open(filename, "w") as f:
        json.dump([], f)

with open(filename, "r") as f:
    data = json.load(f)

data.extend(random_strings)

with open(filename, "w") as f:
    json.dump(data, f)
