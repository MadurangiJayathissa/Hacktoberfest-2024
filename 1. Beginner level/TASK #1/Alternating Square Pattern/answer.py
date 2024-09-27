def alternating_square_pattern(N):
    num = 1  # Start with the first number
    for i in range(1, N+1):
        row = []
        # For odd rows, numbers increase
        if i % 2 != 0:
            for j in range(num, num + 5):
                row.append(j)
        # For even rows, numbers decrease
        else:
            for j in range(num + 4, num - 1, -1):
                row.append(j)
        # Print the row and update num for the next row
        print(" ".join(map(str, row)))
        num += 5

# Example usage:
N = 6  # Number of rows you want to print
alternating_square_pattern(N)
