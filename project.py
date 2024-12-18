import pygame
import sys
import random

# Constants
WINDOW_WIDTH = 300
WINDOW_HEIGHT = 600
BACKGROUND_COLOR = (0, 0, 0)
GRID_COLOR = (200, 200, 200)
FPS = 60
GRID_WIDTH = 10
GRID_HEIGHT = 20
CELL_SIZE = 30

# Tetromino Shapes
TETROMINOES = {
    "I": [(0, 1), (1, 1), (2, 1), (3, 1)],
    "O": [(0, 0), (0, 1), (1, 0), (1, 1)],
    "T": [(1, 0), (0, 1), (1, 1), (2, 1)],
    "S": [(1, 0), (2, 0), (0, 1), (1, 1)],
    "Z": [(0, 0), (1, 0), (1, 1), (2, 1)],
    "J": [(0, 1), (1, 1), (2, 1), (2, 0)],
    "L": [(0, 1), (1, 1), (2, 1), (2, 2)]
}

# Tetromino Colors
TETROMINO_COLORS = {
    "I": (0, 255, 255),
    "O": (255, 255, 0),
    "T": (128, 0, 128),
    "S": (0, 255, 0),
    "Z": (255, 0, 0),
    "J": (0, 0, 255),
    "L": (255, 165, 0)
}

def draw_tetromino(screen, tetromino, position, color):
    x, y = position
    for px, py in tetromino.blocks:
        pygame.draw.rect(screen, color, ((x + px) * CELL_SIZE, (y + py) * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def initialize_grid():
    return [[(0, 0, 0) for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

def draw_grid(screen, grid):
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            pygame.draw.rect(screen, grid[y][x], (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, GRID_COLOR, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

class Tetromino:
    def __init__(self, shape):
        self.shape = shape
        self.color = TETROMINO_COLORS[shape]
        self.blocks = TETROMINOES[shape]
        self.x = 5
        self.y = 0

    def draw(self, screen):
        for block in self.blocks:
            pygame.draw.rect(
                screen,
                self.color,
                ((self.x + block[0]) * CELL_SIZE, (self.y + block[1]) * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            )

    def rotate(self, grid):
        new_blocks = [(py, -px) for px, py in self.blocks]
        for px, py in new_blocks:
            if not (0 <= self.x + px < GRID_WIDTH and 0 <= self.y + py < GRID_HEIGHT) or grid[self.y + py][self.x + px] != (0, 0, 0):
                return
        self.blocks = new_blocks

def check_collision(grid, tetromino):
    for px, py in tetromino.blocks:
        if not (0 <= tetromino.x + px < GRID_WIDTH and 0 <= tetromino.y + py < GRID_HEIGHT) or grid[tetromino.y + py][tetromino.x + px] != (0, 0, 0):
            return True
    return False

def place_tetromino(grid, tetromino):
    for px, py in tetromino.blocks:
        grid[tetromino.y + py][tetromino.x + px] = tetromino.color

def clear_lines(grid):
    lines_cleared = 0
    for y in range(GRID_HEIGHT - 1, -1, -1):
        if all(grid[y][x] != (0, 0, 0) for x in range(GRID_WIDTH)):
            del grid[y]
            grid.insert(0, [(0, 0, 0) for _ in range(GRID_WIDTH)])
            lines_cleared += 1
    return lines_cleared

def main():
    pygame.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Tetris')

    clock = pygame.time.Clock()

    grid = initialize_grid()
    score = 0
    font = pygame.font.Font(None, 36)

    tetromino = Tetromino(random.choice(list(TETROMINOES.keys())))

    running = True
    drop_time = 0
    drop_speed = 500  # Milliseconds

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if tetromino.x > 0:  # Check for left boundary
                        tetromino.x -= 1
                elif event.key == pygame.K_RIGHT:
                    if tetromino.x < GRID_WIDTH - 1:  # Check for right boundary
                        tetromino.x += 1
                elif event.key == pygame.K_DOWN:
                    tetromino.y += 1
                elif event.key == pygame.K_UP:
                    tetromino.rotate(grid)
                elif event.key == pygame.K_SPACE:
                    while not check_collision(grid, tetromino):
                        tetromino.y += 1
                    tetromino.y -= 1

        drop_time += clock.get_rawtime()
        if drop_time > drop_speed:
            tetromino.y += 1
            drop_time = 0

        if check_collision(grid, tetromino):
            tetromino.y -= 1
            place_tetromino(grid, tetromino)
            lines_cleared = clear_lines(grid)
            score += lines_cleared

            tetromino = Tetromino(random.choice(list(TETROMINOES.keys())))
            if check_collision(grid, tetromino):
                print(f"Game Over! Final Score: {score}")
                pygame.quit()
                sys.exit()

        screen.fill(BACKGROUND_COLOR)
        draw_grid(screen, grid)
        tetromino.draw(screen)

        score_text = font.render(f'Score: {score}', True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
