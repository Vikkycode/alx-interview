def pascal_triangle(n):
    """ Generate Pascal's Triangle """

    if n <= 0:
        return []
    
    triangle = []

    previous_row = [1]
    triangle.append(previous_row)

    for i in range(1, n):
        current_row = [1]


        for j in range(1, i):
            current_value = previous_row[j-1] + previous_row[j]
            current_row.append(current_value)

        current_row.append(1)
        triangle.append(current_row)
        

        previous_row = current_row
    
    return triangle