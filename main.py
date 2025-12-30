import json
# (command line) program that takes any String input and converts it into Morse Code.

# open the file
with open('morse_code.json', 'r') as data:
    # scraping the data
    data_file = json.load(data)
data_file = data_file['morse_code']

# Collecting the input string
input_str = input("Typed out a phrase: ").lower()

# for loop across the string and using it as key to access the data
for let in input_str:
    print(data_file[let])