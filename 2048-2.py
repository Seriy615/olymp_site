import random
import pygame
import pyautogui

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

# Инициализация игрового поля
board = [[0] * 4 for _ in range(4)]
add_random_tile(board)
add_random_tile(board)

# Функция для добавления случайного числа на поле
def add_random_tile(board):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        board[i][j] = random.choice([2, 4])

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
# Основной цикл игры
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                # Обработка движения влево
                # Допишите здесь код для движения влево
                move_left(board)
                pass
            elif event.key == pygame.K_RIGHT:
                # Обработка движения вправо
                # Допишите здесь код для движения вправо
                move_right(board)
                pass
            elif event.key == pygame.K_UP:
                # Обработка движения вверх
                # Допишите здесь код для движения вверх
                move_up(board)
                pass
            elif event.key == pygame.K_DOWN:
                # Обработка движения вниз
                # Допишите здесь код для движения вниз
                move_down(board)
                pass

    # Отображение игрового поля
    draw_board(board)
    pygame.display.flip()

pygame.quit()
