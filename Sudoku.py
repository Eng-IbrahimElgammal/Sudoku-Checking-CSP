import random

SIZE = 9
BOX_SIZE = 3
MIN_NUM_TO_REMOVE = 40
MAX_NUM_TO_REMOVE = 50

# Function to print the Sudoku board
def print_board(board):
    for i in range(SIZE):
        if i % BOX_SIZE == 0 and i != 0:
            print("______________________")
        for j in range(SIZE):
            if j % BOX_SIZE == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j], end=" ")
        print()

# Function to check if a value is valid in a given position on the Sudoku board
def is_valid(board, row, col, num):
    return (
        num not in board[row] and
        all(board[i][col] != num for i in range(SIZE)) and
        all(board[BOX_SIZE * (row // BOX_SIZE) + i][BOX_SIZE * (col // BOX_SIZE) + j] != num
            for i in range(BOX_SIZE) for j in range(BOX_SIZE))
    )

# Function to solve the Sudoku puzzle using backtracking
def solve(board):
    for row in range(SIZE):
        for col in range(SIZE):
            if board[row][col] == 0:
                for num in range(1, SIZE + 1):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve(board):
                            return True
                        board[row][col] = 0
                return False
    return True

# Function to generate a randomized Sudoku puzzle
def generate():
    board = [[0] * SIZE for _ in range(SIZE)]
    solve(board)
    # Remove some numbers to create the puzzle
    num_to_remove = random.randint(MIN_NUM_TO_REMOVE, MAX_NUM_TO_REMOVE)
    for _ in range(num_to_remove):
        row = random.randint(0, SIZE - 1)
        col = random.randint(0, SIZE - 1)
        board[row][col] = 0
    return board

# Main function to run the Sudoku game
def main():
    print("Welcome to Sudoku!")
    print("Enter row, column, and number (1-9) to make a move.")
    print("Enter '0 0 0' to solve the puzzle.")

    board = generate()
    print_board(board)

    while True:
        try:
            row, col, num = map(int, input("Enter your move: ").split())
            if row == col == num == 0:
                if solve(board):
                    print("Solution:")
                    print_board(board)
                    print("Congratulations! You solved the puzzle.")
                else:
                    print("The puzzle is unsolvable.")
                break
            if not (1 <= row <= SIZE) or not (1 <= col <= SIZE) or not (1 <= num <= SIZE):
                print("Invalid move. Please try again.")
                continue
            if board[row - 1][col - 1] != 0:
                print("That position is already filled. Please try again.")
                continue
            if not is_valid(board, row - 1, col - 1, num):
                print("Invalid move. Please try again.")
                continue
            board[row - 1][col - 1] = num
            print_board(board)
        except ValueError:
            print("Invalid input. Please enter row, column, and number (1-9) separated by spaces.")

if __name__ == "__main__":
    main()
