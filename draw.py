import pygame
import sys


pygame.init()


WIDTH, HEIGHT = 800, 600
GRID_SIZE = 5
ROWS, COLS = HEIGHT // GRID_SIZE, WIDTH // GRID_SIZE


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Закрашивание клеток (Q + мышь)")


grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]

def draw_grid():
    """Отрисовка сетки и закрашенных клеток"""
    screen.fill(WHITE)
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == 1:
                pygame.draw.rect(
                    screen,
                    RED,
                    (col * GRID_SIZE, row * GRID_SIZE, GRID_SIZE, GRID_SIZE)
                )

def main():
    running = True
    q_pressed = False 

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    q_pressed = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_q:
                    q_pressed = False


        if q_pressed:
            x, y = pygame.mouse.get_pos()
            col = x // GRID_SIZE
            row = y // GRID_SIZE
            if 0 <= row < ROWS and 0 <= col < COLS:
                grid[row][col] = 1

        draw_grid()
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()