weight = float(input("Enter weight in kgs:"))
height = float(input("Enter height in m:"))
bmi = weight / (height ** 2)

if bmi <= 18.4:
    print(f"You are bmi is {bmi:.2f} and you are underweight")
elif 18.5 <= bmi <= 24.9:
    print(f"you are bmi is {bmi:.2f} and you are in Healthy weight range")
elif 25.0 <= bmi <= 29.9:
    print(f"You are bmi is {bmi:.2f} and you are Overweight")
elif bmi >= 30.0:
    print(f"You are bmi is {bmi:.2f} and you are Obese")
else:
    print(" invalid input")
