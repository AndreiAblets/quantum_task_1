from typing import List

def count_islands(grid: List[List[int]]) -> int:
    """
    Counts the number of islands in a given grid.
    An island is a group of adjacent lands connected horizontally or vertically (not diagonally).
    The function modifies the input grid in-place to mark visited cells.

    Parameters:
    grid (List[List[int]]): 2D list representing the map where 1 represents land and 0 represents water.

    Returns:
    int: The number of islands in the grid.
    """
    if not grid or not grid[0]:
        return 0

    num_rows = len(grid)
    num_cols = len(grid[0])
    num_islands = 0

    # Define the four possible directions to move (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def dfs(r: int, c: int):
        """
        Depth-First Search to explore all connected lands and mark them as visited.

        Parameters:
        r (int): Row index.
        c (int): Column index.
        """
        # Base case: check boundaries and whether the cell is unvisited land
        if r < 0 or r >= num_rows or c < 0 or c >= num_cols or grid[r][c] != 1:
            return
        grid[r][c] = -1  # Mark current cell as visited
        # Recursively visit all adjacent cells
        for dr, dc in directions:
            dfs(r + dr, c + dc)

    # Iterate over each cell in the grid
    for row in range(num_rows):
        for col in range(num_cols):
            # If the cell is land, perform DFS to mark all connected lands
            if grid[row][col] == 1:
                num_islands += 1  # Found a new island
                dfs(row, col)

    return num_islands

