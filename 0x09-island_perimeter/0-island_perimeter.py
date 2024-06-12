#!/usr/bin/python3
"""
Island perimeter
"""


def island_perimeter(grid):
    """
    returns the perimeter of 
    the island described in grid
    """
    perimeter = 0

    # Get the dimensions of the grid
    rows, cols = len(grid), len(grid[0])

    # Iterate through each cell in the grid
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Count the number of adjacent water cells
                adjacent_water = 0
                if i > 0 and grid[i - 1][j] == 0:
                    adjacent_water += 1
                if i < rows - 1 and grid[i + 1][j] == 0:
                    adjacent_water += 1
                if j > 0 and grid[i][j - 1] == 0:
                    adjacent_water += 1
                if j < cols - 1 and grid[i][j + 1] == 0:
                    adjacent_water += 1

                # Add the perimeter contribution for this cell
                perimeter += adjacent_water

    return perimeter
