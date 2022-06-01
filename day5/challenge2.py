# highest score in list
highest_score= 0
marks = input("enter your marks ").split()

for i in range(0, len(marks)):
    marks[i] = int(marks[i])
    if highest_score < marks[i]:
        highest_score = marks[i]    
print(highest_score)
