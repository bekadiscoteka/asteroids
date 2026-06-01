# Asteroids

A simple Pygame-based Asteroids-style game.

## Description

This project is a small arcade game built with Python and Pygame. The player controls a spaceship, dodges asteroids, and shoots them to score points.

## Requirements

- Python 3.13 or newer
- Pygame 2.6.1
- `uv` (if used for project tooling or runtime)

## Installation

1. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

If you do not have a `requirements.txt`, install dependencies directly:
```bash
pip install pygame==2.6.1 uv
```

## Running the Game

From the project directory, run:

```bash
python main.py
```

## Controls

- `W` — move forward
- `S` — move backward
- `A` — rotate left
- `D` — rotate right
- `SPACE` — shoot
- `ESC` — exit game
- `R` — restart after game over

## Notes

- The game begins on a menu screen. Press `SPACE` to start.
- Score increases by destroying asteroids.
