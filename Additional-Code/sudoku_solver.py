board = [
    [1,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def print_board(board):
    for row in range(len(board)):
        if row % 3 == 0 and row != 0:
            print("- - - - - - - - -")
        for column in range(len(board[row])):
            if column % 3 == 0 and column != 0:
                    print(" | ", end = '')

            if column == 8:
                 print(board[row][column])
            else:
                 print(board[row][column],end='')

def count_empty_spaces(board):
    zeros = 0
    numbers = 0
    for row in range(len(board)):
          for column in range(len(board[row])):
               numbers += 1
               if board[row][column] == 0:
                    zeros += 1
    print(zeros,numbers)
               

print_board(board)
count_empty_spaces(board)