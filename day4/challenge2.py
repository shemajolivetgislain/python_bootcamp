import random
# this program we allow us to take random person to bill from list of person 
names_string = input("Gives me evrybody's names,  separated by a comma, ")
names = names_string.split(", ")
num_item = len(names)
random_names = random.randint(0, num_item)

person_to_bill = names[random_names]

print(f"{person_to_bill} is going to pay today's bill")
