board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
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
    for row_index in range(len(board)):
          for column_index in range(len(board[row_index])):
               if board[row_index][column_index] == 0:
                    return (row_index, column_index)
    return None

def is_current_board_valid(board, num, pos):
     
     # check row

     for column_index in range(len(board[0])):
         if board[pos[0]][column_index] == num and pos[1] != column_index:
               return False
    
    # check column

     for row_index in range(len(board)):
         if board[row_index][pos[1]] == num and pos[0] != row_index:
             return False
          
    # check box

     box_row = pos[0] // 3
     box_column = pos[1] // 3

     for row in range(box_row*3, box_row*3 + 3):
         for col in range(box_column*3, box_column*3 + 3):
             if board[row][col] == num and (row,col) != pos:
                 return False
    
     return True
        
def solve(board):
     find = indexing_empty_spaces(board)
     if not find:
          return True
     else:
          row, col = find
    
     for i in range(1,10):
          if is_current_board_valid(board, i, (row,col)):
               board[row][col] = i

               if solve(board):
                    return True
               
               board[row][col] = 0
     return False

print_board(board)
count_empty_spaces(board)
solve(board)
print_board(board)