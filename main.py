from island_counter import count_islands 

def main():
    """
    Main function to execute the island counting program.
    Reads input from standard input and outputs the number of islands.
    """
    try:
        # Read dimensions of the grid
        M, N = map(int, input().split())
        grid = []
        for _ in range(M):
            # Read each line and remove any spaces
            line = input().replace(" ", "")
            if len(line) != N:
                raise ValueError("Incorrect number of columns in input.")
            # Convert each character to an integer (0 or 1)
            row = [int(ch) for ch in line]
            grid.append(row)
        # Count islands
        result = count_islands(grid)
        print(result)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()