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
    for row_index in range(len(board)):
        if row_index % 3 == 0 and row_index != 0:
            print("- - - - - - - - -")
        for column_index in range(len(board[row_index])):
            if column_index % 3 == 0 and column_index != 0:
                    print(" | ", end = '')

            if column_index == 8:
                 print(board[row_index][column_index])
            else:
                 print(board[row_index][column_index],end='')

def count_empty_spaces(board):
    zeros = 0
    numbers = 0
    for row_index in range(len(board)):
          for column_index in range(len(board[row_index])):
               numbers += 1
               if board[row_index][column_index] == 0:
                    zeros += 1
    print(zeros,numbers)

# Attempt 1

def indexing_empty_spaces(board):
    empty_positions = []
    for row_index in range(len(board)):
          for column_index in range(len(board[row_index])):
               if board[row_index][column_index] == 0:
                    empty_positions.append([column_index,row_index])
                    return (column_index, row_index)
    print(empty_positions)

def is_current_board_valid(board, num, pos):
     
     # check row

     for row_index in range(len(board[0])):
          if board[pos[0]][row_index] and pos [1] != row_index:
               return False

print_board(board)
count_empty_spaces(board)
indexing_empty_spaces(board)