# from turtle import Turtle, Screen
#
# ramu = Turtle()
# ramu.shape('turtle')
# ramu.color('red','green')
# ramu.setpos(-200,0)
#
# myscreen = Screen()
#
# myscreen.exitonclick()

# from prettytable import PrettyTable
#
# pikachu_table = PrettyTable()
#
# pikachu_table.field_names = ['PokeNames','Types']
# pikachu_table.add_rows(
#     [
#         ['Pikachu','Electric'],
#         ['Squirtle','Water'],
#         ['Charmander','Fire']
#     ]
# )
#
# pikachu_table.align = 'l'
#
# print(pikachu_table)

class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name


user_1 = User("001", "Krishna")
user_2 = User('002','Vichu')
print(user_1.id, user_2.name)






