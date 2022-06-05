# total = 0

# for num in range(1, 100, 2):
#     total += num   
# print(total)


total = 0
count = int(input("enter your range "))
numbers = input("enter your numbers ").split()
for num in range(0, count):
    total += int(numbers[num])
print (total)   