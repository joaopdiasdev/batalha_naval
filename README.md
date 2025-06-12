# Battleship Game

A text-based version of the classic **Battleship** game where you can play in two modes:
1. **PvP (Player vs Player)** mode.
2. **PvE (Player vs AI)** mode.

This version of the game is written in Python and uses the `colorama` library to add some color to the terminal interface.

## Features

- **Dynamic board size**: Choose the size of the board (between 10x10 and 20x20).
- **Ship placement**: Players can manually place ships on the board. The game includes various ship types:
  - **Battleship** (5 spaces)
  - **Aircraft Carrier** (4 spaces)
  - **Destroyers** (2 ships, each 3 spaces)
  - **Submarines** (2 ships, each 2 spaces)
- **Ship placement validation**: Ensures ships do not overlap or go off the board.
- **PvP Mode**: Two players can play against each other on their own boards.
- **PvE Mode**: One player competes against the AI, which automatically places ships and attacks randomly.
- **Turn-based combat**: Players take turns attacking each other's board.
- **Victory Check**: The game detects when a player has sunk all of the opponent’s ships.

## Requirements

- Python 3.x
- `colorama` package for color formatting in the terminal

You can install `colorama` via pip:

```bash
pip install colorama

How to Play

    Run the game with Python:

    python battleship.py

    Select your game mode (PvP or PvE).

    If playing PvP, both players take turns placing their ships on their respective boards.

    If playing PvE, the player places their ships, and the AI automatically places its ships.

    Players take turns attacking each other. Input a row (1-20) and a column (A-T) to target a location.

    The game ends when one player sinks all the opponent's ships.

Game Modes

    PvP (Player vs Player): Two players take turns placing ships and attacking each other.

    PvE (Player vs AI): The player faces off against an AI. The AI places ships randomly and attacks the player at random.

Example Gameplay
Game Start

Escolha o seu modo de jogo:
1 - Jogar contra a máquina
2 - Jogar no modo PvP

Ship Placement

Este é o tabuleiro
Digite um número de linha (1 a 20) para o encouraçado (5 casas):
Digite uma letra para a coluna inicial:

Attack

Digite um número de linha para atacar:
Digite uma coluna para atacar:

Victory

Parabéns! Você venceu!

Feel free to fork this project, submit issues, or create pull requests to improve the game!
