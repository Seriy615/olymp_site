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
                pass
            elif event.key == pygame.K_RIGHT:
                # Обработка движения вправо
                # Допишите здесь код для движения вправо
                pass
            elif event.key == pygame.K_UP:
                # Обработка движения вверх
                # Допишите здесь код для движения вверх
                pass
            elif event.key == pygame.K_DOWN:
                # Обработка движения вниз
                # Допишите здесь код для движения вниз
                pass

    # Отображение игрового поля
    draw_board(board)
    pygame.display.flip()

pygame.quit()
