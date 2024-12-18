import pytest
from tetris import Tetromino, TETROMINOES, initialize_grid, check_collision, place_tetromino, clear_lines

def test_tetromino_initialization():
    shape = "I"
    tetromino = Tetromino(shape)
    assert tetromino.shape == shape
    assert tetromino.color == (0, 255, 255)
    assert len(tetromino.blocks) == 4

def test_initialize_grid():
    grid = initialize_grid()
    assert len(grid) == 20
    assert len(grid[0]) == 10
    for row in grid:
        assert len(row) == 10
        assert all(cell == (0, 0, 0) for cell in row)

def test_check_collision():
    grid = initialize_grid()
    tetromino = Tetromino("O")
    tetromino.x = 4
    tetromino.y = 0
    place_tetromino(grid, tetromino)
    new_tetromino = Tetromino("O")
    new_tetromino.x = 4
    new_tetromino.y = 0
    assert check_collision(grid, new_tetromino) == True

def test_place_tetromino():
    grid = initialize_grid()
    tetromino = Tetromino("I")
    tetromino.x = 5
    tetromino.y = 0
    place_tetromino(grid, tetromino)

    for px, py in tetromino.blocks:
        assert grid[tetromino.y + py][tetromino.x + px] == tetromino.color

def test_clear_lines():
    grid = initialize_grid()
    for x in range(10):
        grid[19][x] = (255, 255, 255)
    lines_cleared = clear_lines(grid)
    assert lines_cleared == 1
    assert all(cell == (0, 0, 0) for cell in grid[19])
