#!/usr/bin/env python3

def island_perimeter(grid):
    """
    Calculates the perimeter of an island represented by a grid.

    Args:
        grid: A list of lists of integers representing the island.
              0 represents water, 1 represents land.

    Returns:
        The perimeter of the island.
    """

    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                perimeter += 4  # Assume each land cell has 4 sides

                # Subtract shared sides with neighboring land cells
                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 2
                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 2

    return perimeter
