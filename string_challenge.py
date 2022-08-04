# The function to return the list
def string_array(the_string):
    # Creating the list and adding the length, first string and Last string
    my_list = [len(the_string), the_string[0], the_string[-1]]

    # Appending the the middle character/characters
    if len(the_string) % 2 == 0:
        mid_index = int(len(the_string) / 2)
        left_mid_index = mid_index - 1
        right_mid_index = mid_index + 1
        my_list.append(the_string[left_mid_index:right_mid_index])
    else:
        mid_index = int(len(the_string) / 2)
        my_list.append(the_string[mid_index])

    # Finding the second occurrence of the second character
    second_char = the_string[1]
    try:
        second_char = the_string.index(second_char, 3, len(the_string))
        my_list.append(f"@ index {second_char}")
    except ValueError:
        my_list.append("not found")

    return my_list

# The string
my_string = "Science"

# Checking if the string is more than 2 characters
if len(my_string) <= 2:
    print("string too short")
else:
    the_list = string_array(my_string)
    print(the_list)
