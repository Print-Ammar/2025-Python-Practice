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
                    return (row_index, column_index)
    print(empty_positions)

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

     box_x = pos[0] // 3
     box_y = pos[1] // 3

     for x_pos in range(box_x*3, box_x*3 + 3):
          for y_pos in (box_y*3, box_y*3 + 3):
               if board[x_pos][y_pos] == num and (x_pos,y_pos) != pos:
                    return False
        

print_board(board)
count_empty_spaces(board)
indexing_empty_spaces(board)