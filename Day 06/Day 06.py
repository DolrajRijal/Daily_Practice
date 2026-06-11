#wap that takes 5 integer inputs from the user and stores them in the list and print largest smallest and averages
num_list = []

for i in range (5):
    item = int(input(f"Enter item {i+1} of the list: "))
    num_list.append(item)

print(num_list)
print("largest = ",max(num_list))
print("smallest = ",min(num_list))
average = sum(num_list)/len(num_list)
print("average = ",average)