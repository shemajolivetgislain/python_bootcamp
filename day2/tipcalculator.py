print("welcome to the tip calculator")
total_bill = float(input("enter your total_bill "))
number_tip = int(input("what percentage tip would you like to give? 10, 12 or 15? "))
percentage_tip = total_bill * number_tip / 100
total_bill_with_tip = total_bill + percentage_tip


people_to_split = int(input("How many people to split the bill? "))

bill_per_person = total_bill_with_tip / people_to_split
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay : {final_amount}")
print(f"Each person should pay : {round(bill_per_person, 2)}")

