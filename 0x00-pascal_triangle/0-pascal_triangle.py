def pascal_triangle(n):
    """Generates Pascal's Triangle with n rows using optimized space."""
    
    if n <= 0:
        return []  

    triangle = [] 
    
    # Start with the first row
    previous_row = [1]
    triangle.append(previous_row)

    for i in range(1, n):
        current_row = [1]  # First element of the current row is always 1
        
        # Calculate the middle values based on the previous row
        for j in range(1, i):
            current_value = previous_row[j - 1] + previous_row[j]
            current_row.append(current_value)
        
        current_row.append(1)  # Last element of the current row is always 1
        triangle.append(current_row)
        
        # Move to the next iteration
        previous_row = current_row  # Update previous_row to current_row

    return triangle