# 🏚️ Haunted Chessboard 🏚️

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

## 🏆 Features

- **Unicode Chess Board Display** - Beautiful chess pieces (♔♕♖♗♘♙ vs ♚♛♜♝♞♟) with clean grid layout
- **Spooky Atmosphere** - Typewriter effects and haunting descriptions
- **Health System** - Wrong moves drain your life force
- **Dramatic Victory Cutscene** - Epic ASCII art celebration
- **Hall of Souls** - Your escape is permanently recorded
- **Hint System** - Get help when you're stuck

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

---

*Good luck, brave soul. The spirits are waiting...*
