def my_list(x):
    sum = 0
    for i in x:
        sum = sum + i
    return sum


limit = int(input("Enter number of elements you want in this list: "))
lst = []
for i in range(limit):
    element = int(input("Enter element: "))
    lst.append(element)
print("List: ", lst)

print("Sum of elements: ",my_list(lst))


