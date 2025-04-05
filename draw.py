import pygame
import sys
from setting import *


pygame.init()


screen = pygame.display.set_mode((WIDTH, HEIGHT))



def save_grid():
    with open(f"func/{file_name}", "w") as f:
        for coord in grid:
            f.write(f"{coord[0]} {coord[1]}\n")
    pygame.image.save(screen, f"func/{file_name}.png")


grid = []

_, file_name = sys.argv

def main():
    running = True
    drawing = False 
    i = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    drawing = True
                if event.key == pygame.K_w:
                    drawing = False
                if event.key == pygame.K_s:
                    save_grid()
                    running = False


        if drawing:
            i += 1
            x, y = pygame.mouse.get_pos()
            col = x
            row = y

            if 0 <= row < HEIGHT and 0 <= col < WIDTH:
                pygame.draw.rect(
                    screen,
                    WHITE,
                    (col, row, 1, 1)
                )
                if [col, row] not in grid:
                    grid.append([col, row])

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()