import pygame
import random
import sys

pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (219, 201, 182)
RED = (255, 0, 0)
COUNT_COLOR = (15, 90, 242)

COLORS = {
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46),
}

SIZE = 4
TILE_SIZE = 100
TILE_MARGIN = 13
WIDTH = SIZE * TILE_SIZE + (SIZE + 1) * TILE_MARGIN
HEIGHT = WIDTH + 40
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")

font = pygame.font.Font(None, 48)
game_over_font = pygame.font.Font(None, 72)

def draw_board(board):
    screen.fill(GREY)
    score_text = font.render(f"Счёт: {count_score}", True, COUNT_COLOR)
    screen.blit(score_text, (TILE_MARGIN, TILE_MARGIN))
    for row in range(SIZE):
        for col in range(SIZE):
            value = board[row][col]
            color = COLORS.get(value, BLACK)
            rect = pygame.Rect(
                col * TILE_SIZE + (col + 1) * TILE_MARGIN,
                row * TILE_SIZE + (row + 1) * TILE_MARGIN + 40,
                TILE_SIZE,
                TILE_SIZE
            )
            pygame.draw.rect(screen, color, rect)
            if value:
                text = font.render(str(value), True, BLACK if value <= 4 else WHITE)
                text_rect = text.get_rect(center=rect.center)
                screen.blit(text, text_rect)
    pygame.display.flip()

def move_left(board):
    new_board = [[0] * SIZE for _ in range(SIZE)]
    global count_score
    for row in range(SIZE):
        col_new = 0
        last = 0
        for col in range(SIZE):
            if board[row][col] != 0:
                if last == 0:
                    last = board[row][col]
                elif last == board[row][col]:
                    new_board[row][col_new] = 2 * last
                    col_new += 1
                    last = 0
                else:
                    new_board[row][col_new] = last
                    count_score += 2 * last
                    col_new += 1
                    last = board[row][col]
        if last != 0:
            new_board[row][col_new] = last
    return new_board

def rotate_board(board):
    return [[board[col][row] for col in range(SIZE)] for row in range(SIZE - 1, -1, -1)]

def add_new_tile(board):
    empty_tiles = [(row, col) for row in range(SIZE) for col in range(SIZE) if board[row][col] == 0]
    if empty_tiles:
        row, col = random.choice(empty_tiles)
        board[row][col] = 2 if random.random() < 0.9 else 4

def game_over(board):
    for row in range(SIZE):
        for col in range(SIZE):
            if board[row][col] == 0:
                return False
            if col < SIZE - 1 and board[row][col] == board[row][col + 1]:
                return False
            if row < SIZE - 1 and board[row][col] == board[row + 1][col]:
                return False
    return True

def show_game_over():
    text = game_over_font.render("Game Over!", True, RED)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.wait(3000)  # Ожидание 2 секунды перед выходом

def main():
    global count_score
    board = [[0] * SIZE for _ in range(SIZE)]
    add_new_tile(board)
    add_new_tile(board)

    running = True
    count_score = 0
    while running:
        draw_board(board)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_LEFT, pygame.K_a):
                    board = move_left(board)
                elif event.key in (pygame.K_RIGHT, pygame.K_d):
                    board = rotate_board(board)
                    board = rotate_board(board)
                    board = move_left(board)
                    board = rotate_board(board)
                    board = rotate_board(board)
                elif event.key in (pygame.K_UP, pygame.K_s):
                    board = rotate_board(board)
                    board = rotate_board(board)
                    board = rotate_board(board)
                    board = move_left(board)
                    board = rotate_board(board)
                elif event.key in (pygame.K_DOWN, pygame.K_w):
                    board = rotate_board(board)
                    board = move_left(board)
                    board = rotate_board(board)
                    board = rotate_board(board)
                    board = rotate_board(board)
                add_new_tile(board)
                if game_over(board):
                    show_game_over()
                    running = False
        draw_board(board)
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
