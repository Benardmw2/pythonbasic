# arithmetics operators
number = int(input("enter no:"))
number2 = int(input("enter no 2:"))
print(number + number2)
print(number - number2)
print(number * number2)
print(number / number2)
print(number % number2)
# comparison operator
number3 = int(input("enter no 3:"))
number4 = int(input("enter no 4:"))
print(f"{number3} is equal to {number4} : {number3 == number4}")
print(f"{number3} is  not equal to {number4} : {number3 != number4}")
print(f"{number3} is  greater than {number4} : {number3 > number4}")
print(f"{number3} is  greater than or equal to {number4} : {number3 >= number4}")
print(f"{number3} is  less than {number4} : {number3 < number4}")
print(f"{number3} is  less than or equal to {number4} : {number3 <= number4}")

number5 = int(input("enter no:"))
number6 = int(input("enter no:"))
print(f"{number5} and {number6} are equal and {number5} is greater than {number6} : {number5 == number6 and number5 > number6}")
print(f"{number5} and {number6} are equal or {number5} is greater than {number6}: {number5 == number6 or number5 > number6}")

