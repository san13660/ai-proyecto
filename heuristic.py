EMPTY = 99

squares = [
    [0,1,30,31],
    [6,7,31,32],
    [12,13,32,33],
    [18,19,33,34],
    [24,25,34,35],
    [1,2,36,37],
    [7,8,37,38],
    [13,14,38,39],
    [19,20,39,40],
    [25,26,40,41],
    [2,3,42,43],
    [8,9,43,44],
    [14,15,44,45],
    [20,21,45,46],
    [26,27,46,47],
    [3,4,48,49],
    [9,10,49,50],
    [15,16,50,51],
    [21,22,51,52],
    [27,28,52,53],
    [4,5,54,55],
    [10,11,55,56],
    [16,17,56,57],
    [22,23,57,58],
    [28,29,58,59]
]

def get_heuristic(board, is_max):
    free_squares = 0
    for square_index in range(len(squares)):
        empty_lines = get_empty_lines_in_square(board, squares[square_index])
        if len(empty_lines) == 1:
            free_squares += 1

            square_index_1, corridor_line_1 = get_corridor(board,square_index,empty_lines[0])
            if corridor_line_1 != -1:
                free_squares += 1
                square_index_2, corridor_line_2 = get_corridor(board,square_index_1,corridor_line_1)
                if corridor_line_2 != -1:
                    free_squares += 1
                    square_index_3, corridor_line_3 = get_corridor(board,square_index_2,corridor_line_2)
                    if corridor_line_3 != -1:
                        free_squares += 1
                        square_index_4, corridor_line_4 = get_corridor(board,square_index_3,corridor_line_3)
                        if corridor_line_4 != -1:
                            free_squares += 1

    if is_max:
        return free_squares
    else:
        return -free_squares

def get_empty_lines_in_square(board, square):
    empty_lines = []
    for line in square:
        if board[line] == EMPTY:
            empty_lines.append(line)
    return empty_lines

def get_corridor(board, square_index, common_line):
    if square_index + 1 < len(squares) and common_line in squares[square_index + 1]:
        empty_lines = get_empty_lines_in_square(board, squares[square_index + 1])
        if len(empty_lines) == 2:
            if empty_lines[0] != common_line:
                return [square_index + 1, empty_lines[0]]
            else:
                return [square_index + 1, empty_lines[1]]
        else:
            return [-1,-1]

    elif square_index - 1 < len(squares) and common_line in squares[square_index - 1]:
        empty_lines = get_empty_lines_in_square(board, squares[square_index - 1])
        if len(empty_lines) == 2:
            if empty_lines[0] != common_line:
                return [square_index - 1, empty_lines[0]]
            else:
                return [square_index - 1, empty_lines[1]]
        else:
            return [-1,-1]

    elif square_index + 5 < len(squares) and common_line in squares[square_index + 5]:
        empty_lines = get_empty_lines_in_square(board, squares[square_index + 5])
        if len(empty_lines) == 2:
            if empty_lines[0] != common_line:
                return [square_index + 5, empty_lines[0]]
            else:
                return [square_index + 5, empty_lines[1]]
        else:
            return [-1,-1]

    elif square_index - 5 < len(squares) and common_line in squares[square_index - 5]:
        empty_lines = get_empty_lines_in_square(board, squares[square_index - 5])
        if len(empty_lines) == 2:
            if empty_lines[0] != common_line:
                return [square_index - 5, empty_lines[0]]
            else:
                return [square_index - 5, empty_lines[1]]
        else:
            return [-1,-1]
    else:
        return [-1,-1]