#File handling
# with open(r"C:\Users\Lenovo\Desktop\portfolio_projects\Daily practice\Day_11\geek.txt.txt", "r") as f:
#     print(f.read())


# f = open(r"Day_11\geek.txt.txt", "r")

# print("file name:", f.name)
# print("mode:", f.mode)
# print("is closed?", f.closed)

# f.close()

# print("is closed?:", f.closed)


with open("geek.txt", "w") as f:
    f.write("Hello world!\n")
    f.write("this is my first file handling exercise\n hope it works")
    f.close()
print("file created and edited succesfully!")
try:

    with open("geek.txt", "r") as f:
        print(f.read())
except FileNotFoundError as e:
    print("Error:", e)
finally:
    f.close()       