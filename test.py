from prettytable import PrettyTable

pikachu_table = PrettyTable()

pikachu_table.field_names = ['PokeNames','Types']
pikachu_table.add_rows(
    [
        ['Pikachu','Electric'],
        ['Squirtle','Water'],
        ['Charmander','Fire']
    ]
)

pikachu_table.align = 'l'

print(pikachu_table)