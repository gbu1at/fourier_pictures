import pygame
import sys
import math
import numpy as np
from setting import *
from fourier import *
from functions import *



pygame.init()


screen = pygame.display.set_mode((WIDTH, HEIGHT))



def get_cr(p):
    x = int(p.real * WIDTH / 2 / XMAX) + WIDTH // 2
    y = int(p.imag * HEIGHT / 2 / YMAX) + HEIGHT // 2

    return x, y


save_points = []


def main():
    running = True

    t = 0
    step = 10000

    _, N, file_name = sys.argv
    N = int(N)

    func = get_function(f"func/{file_name}")
    f = FourierComposition(N + (N + 1) % 2)
    f.fit(func)
    idx_coeff = list(enumerate(f.coef))
    sorted_idx_coeff = list(reversed(sorted(idx_coeff, key=lambda x: abs(x[1]))))


    clock = pygame.time.Clock()
    FPS = 200

    screen.fill(BLACK)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        for x, y in save_points:
            pygame.draw.rect(screen, WHITE, (x, y, 1, 1))

        if t < 1:
            p = 0
            for x in sorted_idx_coeff:
                next_p = f.coef[x[0]] * math.e ** (1j * (x[0] - f.N // 2) * t) / math.sqrt(2 * math.pi) + p
                xp, yp = get_cr(p)

                xnp, ynp = get_cr(next_p)

                pygame.draw.circle(screen, 
                                    color=WHITE,
                                    center=(xp, yp),
                                    radius=int(math.sqrt((xnp - xp) ** 2 + (ynp - yp) ** 2)),
                                    width=1
                                    )

                pygame.draw.line(
                    surface=screen,
                    color=WHITE,
                    start_pos=(xp, yp),
                    end_pos=(xnp, ynp),
                    width=1
                )
                p = next_p

            x, y = get_cr(p)

            if x >= 0 and x < WIDTH and y >= 0 and y < HEIGHT:
                pygame.draw.rect(screen, WHITE, (x, y, 1, 1))
                save_points.append((x, y))


            t += 1 / step


        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()