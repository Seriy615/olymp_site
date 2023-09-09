import random
import pygame
import pyautogui
import time

# Инициализация Pygame
pygame.init()

# Размер окна
WINDOW_SIZE = (400, 400)

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Инициализация окна
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("2048")

# Шрифт для текста
font = pygame.font.Font(None, 36)



# Функция для добавления случайного числа на поле
def add_random_tile(board):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        board[i][j] = random.choice([2, 4])
# Инициализация игрового поля
board = [[0] * 4 for _ in range(4)]
add_random_tile(board)
add_random_tile(board)
# Проверка доступных ходов
def can_move(board, new_board):
    for i in range(4):
        for j in range(4):
            if new_board[i][j] != board[i][j]:
                return True
    return False

# Проверка поражения
def is_game_over(board):
    if any(0 in row for row in board):
        return False
    for i in range(4):
        for j in range(3):
            if board[i][j] == board[i][j + 1] or board[j][i] == board[j + 1][i]:
                return False
    return True

# Отображение игрового поля
def draw_board(board):
    for i in range(4):
        for j in range(4):
            pygame.draw.rect(screen, WHITE, (j * 100, i * 100, 100, 100))
            if board[i][j] != 0:
                text = font.render(str(board[i][j]), True, BLACK)
                text_rect = text.get_rect(center=(j * 100 + 50, i * 100 + 50))
                screen.blit(text, text_rect)

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


def transpose_board(board):
    # Транспонируем доску (строки становятся столбцами)
    board[:] = [list(row) for row in zip(*board)]

def mirror_board(board):
    # Отражаем доску по вертикали
    for row in board:
        row.reverse()
# Основной цикл игры
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            temp_board = [row[:] for row in board]  # Создаем резервную копию
            if event.key == pygame.K_LEFT:
                # Обработка движения влево
                move_left(board)
            elif event.key == pygame.K_RIGHT:
                # Обработка движения вправо
                move_right(board)
            elif event.key == pygame.K_UP:
                # Обработка движения вверх
                move_up(board)

            elif event.key == pygame.K_DOWN:
                move_down(board)
            
            # Проверка доступности хода перед выполнением
            if can_move(temp_board, board):
                add_random_tile(board)
            else:
                # Отображение ошибки
                error_text = font.render("Невозможно сделать ход!", True, (255, 0, 0))
                screen.blit(error_text)
    # Отображение игрового поля и текста ошибки
    draw_board(board)
    pygame.display.flip()

    # Проверка условия поражения и завершение игры
    if is_game_over(board):
        error_text = font.render("Игра окончена. Вы проиграли!", True, (255, 0, 0))
        screen.blit(error_text)
        running = False
        time.sleep(2)
pygame.quit()
