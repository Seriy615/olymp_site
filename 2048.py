import random
import curses

def initialize_board():
    # Создаем пустое игровое поле 4x4
    board = [[0] * 4 for _ in range(4)]
    # Генерируем два начальных числа
    for _ in range(2):
        add_random_tile(board)
    return board

def add_random_tile(board):
    # Генерируем случайные координаты для нового числа
    empty_cells = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        # Случайным образом выбираем 2 или 4 для нового числа
        board[i][j] = random.choice([2, 4])

def print_board(stdscr, board):
    stdscr.clear()
    for i, row in enumerate(board):
        for j, val in enumerate(row):
            stdscr.addstr(i, j * 5, str(val))
    stdscr.refresh()

def slide_left(board):
    for row in board:
        # Сжимаем ряд влево
        row[:] = [val for val in row if val != 0]
        row.extend([0] * (4 - len(row)))

def merge_left(board):
    for row in board:
        for i in range(3):
            if row[i] == row[i + 1] and row[i] != 0:
                row[i] *= 2
                row[i + 1] = 0

def move_left(board):
    slide_left(board)
    merge_left(board)
    slide_left(board)

def move_right(board):
    # Зеркально отражаем доску и используем существующий код для движения влево
    mirror_board(board)
    move_left(board)
    mirror_board(board)

def move_up(board):
    # Транспонируем доску (строки становятся столбцами) и используем код для движения влево
    transpose_board(board)
    move_left(board)
    transpose_board(board)

def move_down(board):
    # Транспонируем доску и отражаем ее, затем используем код для движения влево
    transpose_board(board)
    mirror_board(board)
    move_left(board)
    mirror_board(board)
    transpose_board(board)

def is_game_over(board):
    # Проверяем условие победы (наличие 2048)
    for row in board:
        if 2048 in row:
            return True

    # Проверяем, есть ли еще ходы (нет пустых ячеек и нет соседних равных чисел)
    for i in range(4):
        for j in range(3):
            if board[i][j] == board[i][j + 1] or board[j][i] == board[j + 1][i]:
                return False

    return True

def transpose_board(board):
    # Транспонируем доску (строки становятся столбцами)
    board[:] = [list(row) for row in zip(*board)]

def mirror_board(board):
    # Отражаем доску по вертикали
    for row in board:
        row.reverse()

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    board = initialize_board()
    
    while True:
        print_board(stdscr, board)
        if is_game_over(board):
            stdscr.addstr(5, 0, "Игра окончена! Для выхода нажмите 'q'.")
            stdscr.refresh()
            while True:
                key = stdscr.getch()
                if key == ord('q'):
                    return
        key = stdscr.getch()
        if key == curses.KEY_LEFT:
            move_left(board)
        elif key == curses.KEY_RIGHT:
            move_right(board)
        elif key == curses.KEY_UP:
            move_up(board)
        elif key == curses.KEY_DOWN:
            move_down(board)

        add_random_tile(board)

if __name__ == "__main__":
    curses.wrapper(main)
