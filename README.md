# 🏚️ Haunted Chessboard

**A spooky terminal-based chess puzzle game built in Python.**  
Solve eerie mate-in-one and mate-in-two puzzles to escape a cursed mansion — or remain trapped forever. 🪦
A spooky terminal-based chess puzzle game where you must solve chess puzzles to escape a haunted mansion!

## 🎮 How to Play

1. **Start the game:**
   ```bash
   python3 haunted_chessboard.py
   # or
   ./play_haunted_chess.sh
   ```

2. **Game Mechanics:**
   - You start with 100 life force
   - Each wrong move costs 10 life force
   - Solve all 3 chess puzzles to escape
   - Your escape will be recorded in the Hall of Souls!

3. **Commands:**
   - Enter moves in algebraic notation: `Qh5`, `Nf3`, `e4`, etc.
   - Type `hint` for a clue
   - Type `quit` to give up (and become a ghost forever!)

## 🏚️ The Rooms

1. **The Dusty Library** - Mate in 1 puzzle
2. **The Moonlit Parlor** - Mate in 2 puzzle  
3. **The Master Bedroom** - Final mate in 1 puzzle
## 👻 Haunted Gameplay Preview

![Gameplay Screenshot](https://github.com/isthatananya/haunted-chessboard/blob/55d3e244a500109c900b4825483a8c0621061804/haunted_gameplay.png)


## 🏆 Features

- **Unicode Chess Board Display** - Beautiful chess pieces (♔♕♖♗♘♙ vs ♚♛♜♝♞♟) with clean grid layout
- **Spooky Atmosphere** - Typewriter effects and haunting descriptions
- **Health System** - Wrong moves drain your life force
- **Dramatic Victory Cutscene** - Epic ASCII art celebration
- **Hall of Souls** - Your escape is permanently recorded
- **Hint System** - Get help when you're stuck

🧩 How It Works
ASCII-based chessboard: Renders a visual 8x8 chessboard in your terminal using text characters.

Algebraic move parsing: Accepts chess moves like Qe8, Nf3, Ra8#, O-O, etc.

Life force system: Each incorrect move drains 10 points from your health bar (💀 Life Force).

Puzzles using FEN notation: Each haunted room is backed by a real chess puzzle using FEN strings for board state.



## 📋 Chess Notation Guide

- **Piece Moves:** `Qh5` (Queen to h5), `Nf3` (Knight to f3)
- **Pawn Moves:** `e4`, `d5`
- **Captures:** `Qxh5`, `exd5`
- **Castling:** `O-O` (kingside), `O-O-O` (queenside)
- **Check/Mate:** `Qh5+` (check), `Qh5#` (checkmate)

## 🎯 Solutions (Spoiler Alert!)

<details>
<summary>Click to reveal puzzle solutions</summary>

1. **Library:** `Qe8#`
2. **Parlor:** `Qd5` or `Qd5+`
3. **Bedroom:** `Ra8#`

</details>

## 📜 Hall of Souls

Successfully escape the mansion and your name will be recorded in `hall_of_souls.txt` for all eternity!

## 🛠️ Requirements

- Python 3.6+
- Terminal with at least 80 character width
- Courage to face the supernatural!


## 👻 About the Game

Haunted Chessboard is a text-based adventure where your chess skills determine your survival.

You awaken in a haunted mansion.  
The ghosts of past chess masters demand you solve their final puzzles to earn your freedom.

Each wrong move drains your **life force**.  
Can you make the right plays and escape in time?


## 📸 Demo

<img src="assets/screenshot.png" alt="Gameplay Screenshot" width="700"/>

> *(If the image doesn’t appear, make sure you’ve added `assets/screenshot.png` and pushed it!)*  
> You can generate a terminal recording with [`asciinema`](https://asciinema.org/) too.



## 🧩 Features

- ♟️ Terminal-based chess game using FEN notation
- 🧠 Classic puzzles: mate-in-1 and mate-in-2 challenges
- 🫣 Haunted mansion storyline with creepy room narration
- 💀 Wrong moves reduce your life bar
- 📜 Typewriter-style storytelling to enhance immersion


## 🚀 Getting Started

### Requirements

- Python 3.7+
- Terminal / command-line

### Setup

Clone the repository:

```bash
git clone https://github.com/isthatananya/haunted-chessboard.git
cd haunted-chessboard
