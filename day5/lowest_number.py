lowest_number= 0
number = input("enter the number ").split()
for i in range(0, len(number)):
    number[i] = int(number[i])
    if lowest_number <= number[i]:
        lowest_number = number[i]
print(lowest_number)
    