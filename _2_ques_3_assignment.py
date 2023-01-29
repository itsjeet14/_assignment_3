def my_string(x):
    reverse_string = ""
    for i in x:
        reverse_string = i + reverse_string
    return reverse_string

str = input("Enter a string: ")
print("Reverse String: ", my_string(str))


