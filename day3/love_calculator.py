print("Welcome to love calculator")
name1 = input("What is your name : \n")
name2 = input("What is your name : \n")

combined_names = name1.lower() + name2.lower()
t = combined_names.count("t")
r = combined_names.count("r")
u = combined_names.count("u")
e = combined_names.count("t")

true = t + r + u + e

l = combined_names.count("l")
o = combined_names.count("o")
v = combined_names.count("v")
e = combined_names.count("e")

love = l + o + v + e

Love_Score = int(str(true) + str(love))

if Love_Score<10 or Love_Score > 90:
    print(f"Your score is {Love_Score}, you go together like coke and mentos.")
elif Love_Score >= 40 and Love_Score <= 50:
    print(f"Your score is {Love_Score}, you are alright together.")
else:
    print(f"Your score is {Love_Score}")
        