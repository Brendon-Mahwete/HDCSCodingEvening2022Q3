# This code returns the sum of the Nth row of a Pascal triangle.
def pascal_triangle(number):
    #Declearing lists to work with
    old_list = []
    new_list = []

    # Checking if input is in range 0 to 30 then prints a message and returns a negative number
    if (number < 0) or (number > 30):
        print("Invalid input")
        return -1

    for i in range(number):
        # A for loop using list comprehension to calculate the next from of a pascal triangle
        new_list = [1 if num == 0 else (old_list[num] + old_list[num - 1]) for num in range(len(old_list))]
        new_list.append(1)
        old_list = new_list

    # returning the sum of the list
    return sum(new_list)

digit = int(input("Enter a number between 0 and 30 (inclusive): "))
print(pascal_triangle(digit))
