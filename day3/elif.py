print("Welcome to the roalcoast")
height = int(input("what is your height in cm: "))

if height > 120:
    print("you can ride the roalcoast")
    age = int(input("what is your age: "))
    if age <= 12:
        print("You have to pay 5$")
    elif age<=18:
        print("You have to pay 7$")
    else:
        print("You have to pay 12$")
else:
    print("you can't ride the roalcoast")