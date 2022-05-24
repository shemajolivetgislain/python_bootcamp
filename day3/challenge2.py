# # days 3 challenge
# year = int(input('Which year you what TO check?: '))
# if year % 4 == 0:
#     print ("It is leap year")
#     if year % 100 == 0 :
#         print ("also leap year")
#     elif year % 400 == 0:
#         print ("also leap year")
# else:
#     print ("it is not leap year")
    
# way2 challenge
year = int(input('Which year you what TO check?: '))
if year % 4 == 0:
    if year % 100 == 0 :
       if year % 400 == 0:
        print ("leap year")
       else:
           print ("Not leap year")
    else:
        print ("leap year")
else:
    print ("Not leap year")
