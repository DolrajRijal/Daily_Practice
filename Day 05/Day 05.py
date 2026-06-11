#reversing the string
str1 = input("enter the string: ")
str_rev = ""
# #with slicing
# str_rev = str1[::-1]
# print(str_rev)

#without slicing using loop
for char in str1:
    str_rev = char + str_rev

print(str_rev)