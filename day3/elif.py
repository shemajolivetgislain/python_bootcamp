print("Welcome to the roalcoast")
height = int(input("what is your height in cm: "))
bill= 0

if height > 120:
    print("you can ride the roalcoast")
    age = int(input("what is your age: "))
    if age <= 12:
        bill = 5
        print("You have to pay 5$")
    elif age<=18:
        bill = 7
        print("You have to pay 7$")
    elif age<=45 and age <= 55:
        print(f"Your bill is 0")
    
    else:
        bill = 12
        print("You have to pay 12$")
    wants_photo = input("Do you want a photo taken? (y/n): ")
    if wants_photo == "y":
        bill += 3
        print(f"You have to pay {bill}$")
        
else:
    print("you can't ride the roalcoast")