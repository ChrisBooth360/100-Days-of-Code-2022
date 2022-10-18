# This function copies the list of numbers and adds as many copies of the list as necessary to allow for the adding
# of k numbers.
def copy_list(key):
    list_copy = num_list.copy()

    # If key is less than the length of numbers, the multiples of the list copied is 2.
    if key < len(num_list):
        multiple = 2

    # Else, kay is divided by the length of the list, rounded and 2 is added.
    else:
        multiple = (round(key / len(num_list))) + 2

    # This for loop adds the list of numbers to the copied list as many times as needed.
    for n in range(1, multiple):
        for element in num_list:
            list_copy.append(element)

    # The copy of the list is returned.
    return list_copy


# This function replaces each number is the list with the sum of the next k integers.
def deactivate_bomb():

    # The for loop runs for the length of the num_list.
    for i in range(len(num_list)):

        # The nested for loop runs for the range of i plus 1, to i plus k plus 1 - and adds all the numbers.
        new_num = 0
        for j in range(i + 1, i + k + 1):
            new_num += copied_list[j]

        # The integer at index i changes to the sum of the next k integers.
        num_list[i] = new_num


num_list = [2, 4, 9, 3]
k = 2

# If k is less than 0, the list is reversed, k is turned into a positive, the list is copied and the bomb code determined.
if k < 0:
    num_list.reverse()
    k = -k
    copied_list = copy_list(k)
    deactivate_bomb()
    num_list.reverse()

# If k is 0 or greater, the list is copied and the bomb code determined. (If k is 0, then all items in the final list will be 0).
else:
    copied_list = copy_list(k)
    deactivate_bomb()

print(num_list)
