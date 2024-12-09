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
    cols = len(grid[0]) if rows else 0
    land_cells = 0
    common_edges = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                land_cells += 1
                if i < rows - 1 and grid[i + 1][j] == 1:  # Check below
                    common_edges += 1
                if j < cols - 1 and grid[i][j + 1] == 1:  # Check to the right
                    common_edges += 1
    return land_cells * 4 - 2 * common_edges
