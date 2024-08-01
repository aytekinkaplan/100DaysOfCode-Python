# import another_module
#
# print(another_module.a_kind_of_variable)
#
# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvwidth)
# my_screen.exitonclick()
#
# print("| Pokemon | Type | HP | Attack | Defense | Sp. Atk | Sp. Def | Speed |")
# print("| Bulbasaur | Grass | 45 | 49 | 49 | 65 | 65 | 45 |")
# print("| Charmander | Fire | 39 | 52 | 43 | 60 | 50 | 65 |")
# print("| Squirtle | Water | 44 | 48 | 65 | 50 | 64 | 43 |")

from prettytable import PrettyTable

table = PrettyTable(["Pokemon", "Type", "HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed"])

table.add_row(["Bulbasaur", "Grass", 45, 49, 49, 65, 65, 45])
table.add_row(["Charmander", "Fire", 39, 52, 43, 60, 50, 65])
table.add_row(["Squirtle", "Water", 44, 48, 65, 50, 64, 43])
table.align = "l"
print(table)