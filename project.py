import pygame
import sys

WINDOW_WIDTH = 300
WINDOW_HEIGHT = 600
BACKGROUND_COLOR = (0, 0, 0)  
GRID_COLOR = (200, 200, 200) 
FPS = 60
GRID_WIDTH = 10
GRID_HEIGHT = 20
CELL_SIZE = 30

SHAPES = {
    'I': [(0, 1), (1, 1), (2, 1), (3, 1)],
    'O': [(0, 0), (0, 1), (1, 0), (1, 1)],
    'T': [(0, 1), (1, 1), (2, 1), (1, 0)],
    'S': [(1, 0), (2, 0), (0, 1), (1, 1)],
    'Z': [(0, 0), (1, 0), (1, 1), (2, 1)],
    'J': [(0, 1), (1, 1), (2, 1), (2, 0)],
    'L': [(0, 1), (1, 1), (2, 1), (2, 2)]
}

TETROMINOES = {
    "I": [(0, 1), (1, 1), (2, 1), (3, 1)],
    "O": [(0, 0), (0, 1), (1, 0), (1, 1)],
    "T": [(1, 0), (0, 1), (1, 1), (2, 1)],
    "S": [(1, 0), (2, 0), (0, 1), (1, 1)],
    "Z": [(0, 0), (1, 0), (1, 1), (2, 1)],
    "J": [(0, 0), (0, 1), (0, 2), (1, 2)],
    "L": [(1, 0), (1, 1), (1, 2), (0, 2)]
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

def draw_tetromino(screen, tetromino, position, color):
    x, y = position
    for px, py in tetromino:
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

def main():
    pygame.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Tetris')

    clock = pygame.time.Clock()

    grid = initialize_grid()

    # Create a new Tetromino
    tetromino = Tetromino("T")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tetromino.x -= 1
                elif event.key == pygame.K_RIGHT:
                    tetromino.x += 1
                elif event.key == pygame.K_DOWN:
                    tetromino.y += 1

        if not running:
            break

        screen.fill(BACKGROUND_COLOR)

        draw_grid(screen, grid)
        tetromino.draw(screen)

        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
