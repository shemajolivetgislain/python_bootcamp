# pizza ordering program

print("Welcome to python pizza Deliveries !")
bill = 0
size = input("what size pizza so you want? S, M, l ? ")
add_pepporoni = input("Do you want pepperoni? Y or N ? " )
extra_cheese = input("Do you want Extra cheese? Y or N ? ")

if size == "s":
    bill = 15
    if add_pepporoni == "y":
        with_pepporoni = bill + 2
        print(f"pizza with pepperoni is equal: {with_pepporoni}")
    else:
        print("bill is equal to bill to 15")
    if extra_cheese == "y":
        with_cheese = with_pepporoni + 1
        print(f"pizza with extra cheese is equal: {with_cheese}")
    else:
        print(f"bill without extra cheese is equal to {with_pepporoni} ")
elif size == "m":
    bill = 20
    if add_pepporoni == "y":
        with_pepporoni = bill + 3
        print(f"pizza with pepperoni is equal: {with_pepporoni}")
    else:
        print("bill is equal to bill to 15")
    if extra_cheese == "y":
        with_cheese = with_pepporoni + 1
        print(f"pizza with extra cheese is equal: {with_cheese}")
    else:
        print(f"bill without extra cheese is equal to {with_pepporoni} ")

elif size == "l":
    bill = 25
    if add_pepporoni == "y":
        with_pepporoni = bill + 3
        print(f"pizza with pepperoni is equal: {with_pepporoni}")
    else:
        print("bill is equal to bill to 15")
    if extra_cheese == "y":
        with_cheese = with_pepporoni + 1
        print(f"your final bill is equal: {with_cheese}")
    else:
        print(f"bill without extra cheese is equal to {with_pepporoni} ")
               