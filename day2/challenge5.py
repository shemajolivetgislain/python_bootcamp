daysInYear = 365
weeksInYear = 52
monthsInYear = 12
defaultYear= 90
defaultdays= daysInYear * defaultYear
defaultweeks= weeksInYear * defaultYear
defaultMonth= monthsInYear * defaultYear
age = int(input("please enter your age \n"))
livedDays = age * daysInYear
livedWeeks = age * weeksInYear
livedMonths = age * monthsInYear

remainDays = defaultdays  - livedDays
remainWeeks = defaultweeks  - livedWeeks
remainMonth = defaultMonth - livedMonths

print(f"your have {remainMonth} months , {remainWeeks} weeks, {remainDays} days left")