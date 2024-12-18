# Tetris Game with Python
https://youtu.be/gSBuXM6sESo

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Tools and Libraries](#tools-and-libraries)
- [Installation](#installation)
- [Usage](#usage)
- [File Overview](#file-overview)
- [Future Improvements](#future-improvements)
- [License](#license)

---

## Introduction
Welcome to the Tetris Game! This project is a Python implementation of the classic Tetris game using the `pygame` library. The game captures the essence of the original Tetris with features like falling tetrominoes, rotating and moving blocks, line clearing, and a scoring system. It’s a simple yet engaging way to dive into game development and experience the nostalgic thrill of Tetris.

Whether you’re a beginner looking to learn about game logic or an experienced developer wanting to explore `pygame`, this project provides an excellent opportunity for both learning and fun.

---

## Features
- Classic Tetris gameplay mechanics:
  - Tetrominoes falling on a 10x20 grid.
  - Blocks can be rotated and moved left, right, or down.
  - Completed lines are cleared and scored.
- Scoring system based on lines cleared.
- Game over detection when blocks stack to the top.
- Intuitive and responsive keyboard controls:
  - Arrow keys for movement and rotation.
  - Spacebar for instant drop.
- Modular and readable codebase for easy customization.

---

## Tools and Libraries
The following tools and libraries were used in this project:
- **Python**: The core programming language for the project.
- **Pygame**: A library used for creating graphical interfaces and handling game logic.

---

## Installation
To run the game on your local machine, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/shuahuahua/python_tetris_game.git
    cd python_tetris_game
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the game:
    ```bash
    python project.py
    ```

---

## Usage
Once the game starts:
- Use the arrow keys for controlling the tetrominoes:
  - **Left Arrow**: Move left.
  - **Right Arrow**: Move right.
  - **Down Arrow**: Speed up descent.
  - **Up Arrow**: Rotate block.
  - **Spacebar**: Hard drop to the bottom.
- Clear lines to score points and avoid stacking to the top.
- Aim to beat your high score!

---

## File Overview
Here’s a summary of the files included in this project:

- **`project.py`**: Contains the main game logic, including tetromino movements, collision detection, and grid rendering.
- **`test_project.py`**: Unit tests for verifying the functionality of key game components, such as tetromino placement, line clearing, and collision checks.
- **`requirements.txt`**: Lists all Python libraries required to run the project, ensuring a smooth setup process.
- **`README.md`**: Comprehensive documentation providing an overview of the project and setup instructions.

---

## Future Improvements
While the game is functional, there are several features and enhancements that could be added in the future:
1. **Hold Mechanic**: Allow players to hold a tetromino for later use.
2. **Advanced Scoring System**: Introduce bonuses for combos or T-spins.
3. **Enhanced Graphics and Animations**: Improve the visual appeal of the game with smoother animations and custom sprites.
4. **Sound Effects and Music**: Add an immersive audio experience with background music and sound effects for actions like line clears.
5. **Multiplayer Mode**: Implement a competitive mode where two players can play simultaneously.
6. **Settings Menu**: Add options for customizing controls, grid size, and game speed.

---

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute the code as you see fit.

---

With this README, your project will look polished and professional on GitHub. Let me know if there are any specific sections you’d like to adjust!
