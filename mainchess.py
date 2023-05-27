# 象棋小程序

# 定义棋盘
chessboard = [['車', '馬', '象', '士', '将', '士', '象', '馬', '車'],
              ['　', '　', '　', '　', '　', '　', '　', '　', '　'],
              ['　', '砲', '　', '　', '　', '　', '　', '砲', '　'],
              ['卒', '　', '卒', '　', '卒', '　', '卒', '　', '卒'],
              ['　', '　', '　', '　', '　', '　', '　', '　', '　'],
              ['　', '　', '　', '　', '　', '　', '　', '　', '　'],
              ['兵', '　', '兵', '　', '兵', '　', '兵', '　', '兵'],
              ['　', '炮', '　', '　', '　', '　', '　', '炮', '　'],
              ['　', '　', '　', '　', '　', '　', '　', '　', '　'],
              ['車', '馬', '相', '仕', '帅', '仕', '相', '馬', '車']]

# 定义玩家
PLAYER_1 = 1
PLAYER_2 = 2

# 打印棋盘
def print_chessboard(board):
    print('  0 1 2 3 4 5 6 7 8')
    for i in range(10):
        print(i, end=' ')
        for j in range(9):
            print(board[i][j], end=' ')
        print()

# 获取棋子位置
def get_piece_position(board, piece):
    for i in range(10):
        for j in range(9):
            if board[i][j] == piece:
                return i, j
    return None, None

# 移动棋子
def move_piece(board, start_row, start_col, end_row, end_col):
    piece = board[start_row][start_col]
    board[start_row][start_col] = '　'
    board[end_row][end_col] = piece

# 检查将军
def check_check(board, player):
    # 获取对方帅的位置
    if player == PLAYER_1:
        opponent_king = '帅'
    else:
        opponent_king = '将'
    king_row, king_col = get_piece_position(board, opponent_king)

    # 检查是否被对方的棋子将军
    for i in range(10):
        for j in range(9):
            piece = board[i][j]
            if piece != '　' and \
                    (player == PLAYER_1 and piece.islower() or \
                     player == PLAYER_2 and piece.isupper()):
                if can_move(board, i, j, king_row, king_col):
                    return True



