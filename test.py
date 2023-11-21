with open('file1.txt', 'r') as file1:
    list1 = [ int(num.rstrip()) for num in file1.readlines()]

with open('file2.txt', 'r') as file2:
    list2 = [ int(num.rstrip()) for num in file2.readlines()]


result = [ num for num in list1 if num in list2]


# # Write your code above 👆
print(result)
