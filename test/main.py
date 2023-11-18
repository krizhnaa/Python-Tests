
names = []

with open("./Input/Names/invited_names.txt") as file:
    names_file = file.read()
    names = names_file.split('\n')

# data_into_list = data.replace('\n', ' ')

with open("./Input/Letters/starting_letter.txt") as file:
    letter = file.read()
    replaced_letter = letter.replace('[name]', names[0])


