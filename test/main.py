
names = []

with open("./Input/Names/invited_names.txt") as file:
    names_file = file.read()
    names = names_file.split('\n')