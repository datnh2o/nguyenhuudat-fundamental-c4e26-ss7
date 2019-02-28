from random import randint, choice
from calc import generate_quiz

x = randint(0, 11)
y = randint(0, 11)
er = randint(-1, 1)

op = choice(["+", "-", "*", "/"])
c = generate_quiz(x, y, op) + er
s = f"{x} {op} {y} = {c}"
#print(a,"+",b,"=",c)
# print(s)
# yn = input("Y/N? ")
# if er == 0:
#     if yn == "y":
#         print("good")
#     elif yn == "n":
#         print("false")
# else:
#     if yn == "y":
#         print("false")
#     elif yn == "n":
#         print("good")


 

