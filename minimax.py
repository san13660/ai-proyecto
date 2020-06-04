import random
from heuristic import get_heuristic

EMPTY = 99

def minimax(board, use_heuristic):
    flat_board = flatten_board(board)
    
    value_l0 = -99
    movement_l0 = 0
    board_l0 = flat_board
    is_max_l0 = True

    for a in range(60):
        if is_invalid_movement(board_l0, a):
            continue
        
        movement_l1 = a
        board_l1 = board_l0[:]    
        score_l1 = make_movement(board_l1, movement_l1, is_max_l0)

        if score_l1 > 0:
            is_max_l1 = True
            value_l1 = -99
        else:
            is_max_l1 = False
            value_l1 = 99
           
        level_2_exists = False
        for b in range(60):
            if is_invalid_movement(board_l1, b):
                continue

            movement_l2 = b
            board_l2 = board_l1[:]
            score_l2 = make_movement(board_l2, movement_l2, is_max_l1)

            is_max_l2 = True
            value_l2 = -99

            if not is_max_l1 and score_l2 < 0:
                is_max_l2 = False
                value_l2 = 99
            elif is_max_l1 and score_l2 == 0:
                is_max_l2 = False
                value_l2 = 99

            level_2_exists = True
            level_3_exists = False
            for c in range(60):
                if is_invalid_movement(board_l2, c):
                    continue

                movement_l3 = c
                board_l3 = board_l2[:]
                score_l3 = make_movement(board_l3, movement_l3, is_max_l2)

                is_max_l3 = True
                value_l3 = -99

                if not is_max_l2 and score_l3 < 0:
                    is_max_l3 = False
                    value_l3 = 99
                elif is_max_l2 and score_l3 == 0:
                    is_max_l3 = False
                    value_l3 = 99
                
                value_l3 = get_board_score(board_l3, is_max_l3, use_heuristic)

                level_3_exists = True

                if (is_max_l2 and value_l3 > value_l2) or (not is_max_l2 and value_l3 < value_l2):
                    value_l2 = value_l3
                    if (is_max_l2 and not is_max_l1 and value_l2 >= value_l1) or (not is_max_l2 and is_max_l1 and value_l2 <= value_l1):
                        break

            if not level_3_exists:
                value_l2 = get_board_score(board_l2, is_max_l2, use_heuristic)

            if (is_max_l1 and value_l2 > value_l1) or (not is_max_l1 and value_l2 < value_l1):
                value_l1 = value_l2
                if (not is_max_l1 and value_l1 <= value_l0):
                    break

        if not level_2_exists:
            value_l1 = get_board_score(board_l1, is_max_l1, use_heuristic)

        if value_l1 > value_l0 or (use_heuristic and value_l0 == 0 and board_l0.count(0) < 6 and random.randint(0,7) == 4):
            value_l0 = value_l1
            movement_l0 = movement_l1

    print('BEST VALUE: ' + str(value_l0))
    print('BEST MOVEMENT: [' + str(movement_l0) +']')
    print('-----------------')

    return get_o_n(movement_l0)                           

def get_o_n(a):
    if a > 29:
        return [1, (a-30)]
    else:
        return [0, (a)]

def is_invalid_movement(board, n):
    if board[n] == EMPTY:
        return False
    else:
        return True

def get_board_score(board, is_max, use_heuristic):
    score = 0
    for i in range(60):
        if board[i] != EMPTY:
            score += board[i]
    
    if use_heuristic:
        score += get_heuristic(board, is_max)

    return score

def flatten_board(board):
    new_board = []
    for o in range(2):
        for n in range(30):
            if board[o][n] == EMPTY:
                new_board.append(99)
            else:
                new_board.append(0)
    return new_board

def make_movement(board, n, is_max):
    score_before = get_total_score(board)
    board[n] = 0
    score_after = get_total_score(board)

    total = score_after - score_before

    if not is_max:
        total = -total

    board[n] = total

    return total

def get_total_score(board): 
    acumulator = 0
    counter = 0
    points = 0
    for i in range(30):
        if(((i + 1) % 6) != 0):
            if(board[i] != EMPTY and board[i + 1] != EMPTY and board[(counter + acumulator)+30] != EMPTY and board[(counter + acumulator + 1)+30] != EMPTY):
                points += 1
            acumulator += 6
        else:
            counter += 1
            acumulator = 0
    return points