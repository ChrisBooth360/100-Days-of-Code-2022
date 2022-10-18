def pascals_triangle(num_rows):
    pascal_list = []

    for index in range(0, num_rows):  # A for loop runs for the amount of rows inputted

        # [1] is appended to pascal_list in the first index position.
        if index == 0:
            pascal_list.append([1])

        # [1, 1] is appended to pascal_list in the second index position.
        elif index == 1:
            pascal_list.append([1, 1])

        # If the index is greater than 1, then this else function is run.
        else:
            # In Pascal's Triangle, each row starts with a 1.
            row = [1]
            # The row before in pascal_list is needed to calculate the elements in the current row.
            row_above = pascal_list[index - 1]

            # A for loop runs in the range of 1 to the length of the row_above.
            for i in range(1, len(row_above)):
                # The next element in the current row is determined using the row above and appended to the current row.
                next_element = row_above[i - 1] + row_above[i]
                row.append(next_element)

            # Each row in Pascal's Triangle ends with a 1.
            row.append(1)
            # The new row is appended to pascal_list
            pascal_list.append(row)

    # pascal_list is returned.
    return pascal_list


print(pascals_triangle(10))
