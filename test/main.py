# Creating a list called names to store all the names
names = []

# Reading all the names into the list
with open("./Input/Names/invited_names.txt") as file:
    names_file = file.read()
    names = names_file.split('\n')

# Looping through the names in the list and replacing it with the placeholder in the letter for all the names
with open("./Input/Letters/starting_letter.txt", mode='r') as file:
    letter = file.read()
    for name in names:
        replaced_letter = letter.replace('[name]', name)
        # Writing the new letter with replaced name into the folder
        with open(f'./Output/ReadyToSend/{name}_letter.txt', mode='w') as filee:
            filee.write(replaced_letter)

