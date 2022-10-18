# The magic_sorting function takes two arrays and returns
def magic_sorting(arr1, arr2):
    # A temporary array and the array that will be returned are declared.
    temp_array = []
    return_array = []

    # A for loop runs over each number in the first array and if the number is not in the second array, then the number is added to the temporary list.
    for num in arr1:
        if num not in arr2:
            temp_array.append(num)

    # A for loop runs over each number in the second array and a nested loop runs over each number in the first array.
    for item in array2:
        for num in array1:
            # If the number in array 2 equals to the number in array 1, then that number is appended to the return list.
            if item == num:
                return_array.append(num)

    # The temp array containing the extra numbers is sorted.
    temp_array.sort()

    # A for loop runs over each number in the return array and appends it to the return list.
    for item in temp_array:
        return_array.append(item)

    return return_array


# Two arrays are declared and passed through the magic_sorting() function.
array1 = [28, 6, 22, 8, 44, 17]
array2 = [22, 28, 8, 6]

final_list = magic_sorting(array1, array2)
print(final_list)