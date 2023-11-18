import sys, fileinput
names = []

with open("./Input/Names/invited_names.txt") as file:
    names_file = file.read()
    names = names_file.split('\n')

# data_into_list = data.replace('\n', ' ')

with open("./Input/Letters/starting_letter.txt", mode='r') as file:
    letter = file.read()
    for name in names:
        replaced_letter = letter.replace('name', name)
        with open(f'./Output/ReadyToSend/{name}_letter.txt', mode='w') as filee:
            filee.write(replaced_letter)

