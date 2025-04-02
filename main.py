import numpy as np
import pygame
import sys
import math


pygame.init()


WIDTH, HEIGHT = 600, 600
GRID_SIZE = 5
ROWS, COLS = HEIGHT // GRID_SIZE, WIDTH // GRID_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption()


grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]

def draw_grid():
    for row in range(ROWS):
        for col in range(COLS):
            color = RED if grid[row][col] == 1 else WHITE
            pygame.draw.rect(
                screen,
                color,
                (col * GRID_SIZE, row * GRID_SIZE, GRID_SIZE, GRID_SIZE),
            )

class Function:
    def __init__(self, func):
        self.func = func

    def __mul__(self, other):
        return Function(self.func * other.func)

    def integrate(self, diap=(0, 1), size=100):
        s, f = diap

        X = np.linspace(s, f, size)
        dx = (f - s) / size

        return sum([self.func(x) for x in X]) * dx 


class FourierComposition:
    def __init__(self, N = 51):
        assert N % 2 == 1
        self.N = N
        self.coef = [0j] * self.N

    def fit(self, f: Function):
        self.f = f

        for i in range(-self.N // 2, self.N // 2 + 1):
            self.coef[i] = (self.f * Function(lambda t : math.e ** (1j * -i * t))).integarte()


def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # elif event.type == pygame.MOUSEBUTTONDOWN:
            #     x, y = pygame.mouse.get_pos()
            #     col = x // GRID_SIZE
            #     row = y // GRID_SIZE
            #     grid[row][col] = 1 - grid[row][col]

        screen.fill(WHITE)
        start()
        draw_grid()
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()