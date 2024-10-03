def pascal_triangle(n):
    """Generates Pascal's Triangle with n rows while handling list copying properly."""
    
    triangle = []  # Initialize the triangle as an empty list
    
    for i in range(n):
        row = []  # Initialize a new row
        
        # Loop through each position in the row
        for j in range(i + 1):
            # First and last element of each row is always 1
            if j == 0 or j == i:
                row.append(1)  # Edge elements are always 1
            else:
                # Properly access the previous row's elements for calculation
                value = triangle[i - 1][j - 1] + triangle[i - 1][j]
                row.append(value)  # Append calculated value to the new row
        
        # Append the newly created row to the triangle
        triangle.append(row.copy())  # Use .copy() to ensure a new list is added
    
    return triangle

# Input Handling with Try-Except Blocks
# while True:
#     try:
#         # Get the number of rows from the user
#         rows = int(input("Enter the number of rows for Pascal's Triangle (positive integer): "))
        
#         # Check if the input is a positive integer
#         if rows < 1:
#             raise ValueError("The number of rows must be a positive integer.")
        
#         # Generate Pascal's Triangle
#         pascals_triangle = generate_pascals_triangle(rows)
        
#         # Print Pascal's Triangle row by row
#         for row in pascals_triangle:
#             print(row)
        
#         break  # Exit the loop after successful execution

#     except ValueError as e:
#         print(f"Invalid input: {e}. Please try again.")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}. Please try again.")
