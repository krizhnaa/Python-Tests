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

# class User:
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name
#         self.followers = 0
#         self.following = 0

#     def follow(self, user):
#         user.followers+=1
#         self.following+=1

#     def unfollow(self, user ):
#         user.followers-=1
#         self.following-=1

# user_1 = User("001", "Krishna")
# user_2 = User('002','Vichu')
# # print(user_1.id, user_2.name)

# user_1.follow(user_2)

# print(user_1.name, user_1.following)
# print(user_2.name, user_2.followers)

# user_1.unfollow(user_2)

# print(user_1.following)
# print(user_2.name, user_2.followers)

from turtle import Turtle, Screen
import random
import randomcolor

rand_color = randomcolor.RandomColor()
miya = Turtle()
miya.shape('circle')

#Drawing Triangle
#360/3 = 180

# sides = [3,4,5,6,7,8,9,10]
# for shape in sides:
#     degree = 360/shape
#     miya.color(rand_color.generate())
#     for i in range(shape):
#         miya.right(degree)
#         miya.forward(100)

def randomize_direction():
    choice = [ 0, 90, 180, 270]
    return random.choice(choice)

miya.speed(4)
miya.shapesize(outline=0)
miya.pensize(10)

while True:
    miya.forward(30)
    miya.color(rand_color.generate())
    miya.setheading(randomize_direction())


screen = Screen()
screen.exitonclick()













