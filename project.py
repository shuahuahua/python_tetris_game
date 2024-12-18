import pygame
import sys
import random

# Game Constants
WINDOW_WIDTH = 300
WINDOW_HEIGHT = 600
BACKGROUND_COLOR = (0, 0, 0)
GRID_COLOR = (200, 200, 200)
FPS = 60
GRID_WIDTH = 10
GRID_HEIGHT = 20
CELL_SIZE = 30

# Tetromino shapes and their properties
TETROMINOES = {
    "I": [(0, 1), (1, 1), (2, 1), (3, 1)],
    "O": [(0, 0), (0, 1), (1, 0), (1, 1)],
    "T": [(1, 0), (0, 1), (1, 1), (2, 1)],
    "S": [(1, 0), (2, 0), (0, 1), (1, 1)],
    "Z": [(0, 0), (1, 0), (1, 1), (2, 1)],
    "J": [(0, 1), (1, 1), (2, 1), (2, 0)],
    "L": [(0, 1), (1, 1), (2, 1), (2, 2)]
}

TETROMINO_COLORS = {
    "I": (0, 255, 255),
    "O": (255, 255, 0),
    "T": (128, 0, 128),
    "S": (0, 255, 0),
    "Z": (255, 0, 0),
    "J": (0, 0, 255),
    "L": (255, 165, 0)
}

# Create the grid
def initialize_grid():
    return [[(0, 0, 0) for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

# Draw the grid on the screen
def draw_grid(screen, grid):
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            pygame.draw.rect(screen, grid[y][x], (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, GRID_COLOR, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

# Place Tetromino on the grid
def place_tetromino_on_grid(grid, tetromino):
    for px, py in tetromino.blocks:
        if 0 <= py < GRID_HEIGHT and 0 <= px < GRID_WIDTH:
            grid[tetromino.y + py][tetromino.x + px] = tetromino.color

# Check for collisions with the grid boundaries and other Tetrominoes
def check_collision(grid, tetromino, dx, dy):
    for px, py in tetromino.blocks:
        new_x = tetromino.x + px + dx
        new_y = tetromino.y + py + dy
        if new_x < 0 or new_x >= GRID_WIDTH or new_y < 0 or new_y >= GRID_HEIGHT or grid[new_y][new_x] != (0, 0, 0):
            return True
    return False

# Tetromino class to manage individual shapes
class Tetromino:
    def __init__(self):
        self.shape = random.choice(list(TETROMINOES.keys()))
        self.color = TETROMINO_COLORS[self.shape]
        self.blocks = TETROMINOES[self.shape]
        self.x = 5
        self.y = 0

    def draw(self, screen):
        for px, py in self.blocks:
            pygame.draw.rect(
                screen,
                self.color,
                ((self.x + px) * CELL_SIZE, (self.y + py) * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            )

def main():
    pygame.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Tetris')

    clock = pygame.time.Clock()

    grid = initialize_grid()

    # Create a new random Tetromino
    tetromino = Tetromino()

    last_fall_time = pygame.time.get_ticks()
    fall_speed = 500  # Milliseconds

    running = True
    while running:
        current_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and not check_collision(grid, tetromino, -1, 0):
                    tetromino.x -= 1
                elif event.key == pygame.K_RIGHT and not check_collision(grid, tetromino, 1, 0):
                    tetromino.x += 1
                elif event.key == pygame.K_DOWN and not check_collision(grid, tetromino, 0, 1):
                    tetromino.y += 1

        if current_time - last_fall_time > fall_speed:
            if not check_collision(grid, tetromino, 0, 1):
                tetromino.y += 1
            else:
                place_tetromino_on_grid(grid, tetromino)
                tetromino = Tetromino()  # Create a new random Tetromino

            last_fall_time = current_time

        screen.fill(BACKGROUND_COLOR)

        draw_grid(screen, grid)
        tetromino.draw(screen)

        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
