# Chess Game

This project is a simple implementation of the classic game of Chess, written in Python using the Pygame library.

## Structure

The project is structured into several Python files, each responsible for a different aspect of the game:

- `main.py`: This is the entry point of the application. It initializes the Pygame library, sets up the game window, and contains the main game loop.

- `game.py`: This file contains the `Game` class which handles the game logic.

- `piece.py`: This file defines the `Piece` class, which represents a chess piece.

- `square.py`: This file defines the `Square` class, which represents a square on the chess board.

- `move.py`: This file defines the `Move` class, which represents a move in the game.

- `const.py`: This file contains constant values used throughout the project, such as the width and height of the game window.

## Enhancements

- **Checkmate Detection**: Implemented a feature to detect checkmate conditions, ensuring the game ends correctly when a checkmate occurs, enhancing the overall game experience.

## Running the Game

To run the game, simply execute the `main.py` file:

```bash
python main.py
```

## Requirements

- Python 3.x
- Pygame
