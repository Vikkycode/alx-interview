#!/usr/bin/python3

def island_perimeter(grid):
    """
    Calculates the perimeter of an island represented by a grid.

    Args:
        grid: A list of lists of integers representing the island.
              0 represents water, 1 represents land.

    Returns:
        The perimeter of the island.
    """

    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check top
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                # Check bottom
                if i == rows - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                # Check left
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                # Check right
                if j == cols - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

    return perimeter
