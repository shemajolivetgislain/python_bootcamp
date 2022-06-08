# name_list = ["jolivet", "shema", "jiji"]

# for i in range(0, len(name_list)):
#     length_name = len(name_list[i])
#     if length_name == 4:
#         print(name_list[i])


name_list = ["jolivet", "aa", "jiji"]  
name_list_a = ""
for char in range(len(name_list)):
    if name_list[char][1] == "o":
        name_list_a = name_list[char]
print(name_list_a) 