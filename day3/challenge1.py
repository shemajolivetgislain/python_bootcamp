# number = int(input("Enter your number"))
# if number % 2 == 0:
#     print("number is even")
# else:
#     print("number is odd")
    
height = float(input("enter your height"))
weight = int(input("enter your weight"))
bmi = weight / height ** 2
if bmi < 18.5 : 
    print("underweight")
elif bmi > 18.5 and bmi < 25: 
    print("normal weight")
    
elif bmi > 25 and bmi < 30: 
    print("overweight")
elif bmi > 30 and bmi < 35: 
    print("obese")
elif bmi > 35: 
    print("clinically obese")