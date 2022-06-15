# matrix exercises]

# for i in range(1, 8 + 1):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print("")

fact = 1
number = int(input("enter your number"))
for i in range(1,number + 1):
    fact = fact * i

print(fact)