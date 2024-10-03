#!/usr/bin/python3

def pascals_triangle(n):
    """Generates Pascal's Triangle with n rows using optimized space."""
    
    if n <= 0:
        return []  # Return an empty triangle for non-positive n

    triangle = []  # List to hold the final triangle
    
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

# Input Handling with Try-Except Blocks
# while True:
#     try:
#         # Get the number of rows from the user
#         rows = int(input("Enter the number of rows for Pascal's Triangle (positive integer): "))
        
#         # Check if the input is a positive integer
#         if rows < 1:
#             raise ValueError("The number of rows must be a positive integer.")
        
#         # Generate Pascal's Triangle
#         pascals_triangle = generate_pascals_triangle_optimized(rows)
        
#         # Print Pascal's Triangle row by row
#         for row in pascals_triangle:
#             print(row)
        
#         break  # Exit the loop after successful execution

#     except ValueError as e:
#         print(f"Invalid input: {e}. Please try again.")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}. Please try again.")
