# 8. Number Manipulation and F Strings in Python
# rounding number in python like 8/3 is equal to 2.6666666666665 when round that number will be equal to 3
# round convert float number into whole number
from doctest import Example


print(round(8 / 3))
# Example 2
print(round(8 / 3, 2))
# Example 3
print(round(2.66666666666666, 2))
# floor division
print(round(8 // 3))
# F string
# f-string help us to concentinate string type to the other type like int , bol and float
score= 0
height= 1.9
isWinning = True
print(f"your score is {score}, your height is {height} your winning is {isWinning}")
