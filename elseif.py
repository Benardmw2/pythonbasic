marks = int(input("Enter marks:"))

if 80 <= marks <= 100:
    print("You have an A")
elif 60 <= marks <= 79:
    print("You have a B")
elif 40 <= marks <= 59:
    print("You have a C")
elif 0 <= marks <= 39:
    print("You have failed")
else:
    print("Wrong input")
