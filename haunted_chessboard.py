#!/usr/bin/env python3
"""
Haunted Chessboard - A Terminal-Based Chess Puzzle Game
Solve chess puzzles to escape the haunted mansion!
"""

import re
import time
import sys
import os
from datetime import datetime
from typing import Dict, List, Tuple, Optional

class ChessBoard:
    """Represents a chess board with FEN notation support"""
    
    def __init__(self, fen: str = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"):
        self.board = [[' ' for _ in range(8)] for _ in range(8)]
        self.to_move = 'w'
        self.parse_fen(fen)
    
    def parse_fen(self, fen: str):
        """Parse FEN notation and set up the board"""
        parts = fen.split()
        board_part = parts[0]
        self.to_move = parts[1] if len(parts) > 1 else 'w'
        
        row = 0
        col = 0
        
        for char in board_part:
            if char == '/':
                row += 1
                col = 0
            elif char.isdigit():
                col += int(char)
            else:
                if row < 8 and col < 8:
                    self.board[row][col] = char
                    col += 1
    
    def piece_to_unicode(self, piece: str) -> str:
        """Convert piece letter to Unicode chess symbol
        
        White pieces: ♔♕♖♗♘♙ (King, Queen, Rook, Bishop, Knight, Pawn)
        Black pieces: ♚♛♜♝♞♟ (King, Queen, Rook, Bishop, Knight, Pawn)
        """
        piece_map = {
            'K': '♔', 'Q': '♕', 'R': '♖', 'B': '♗', 'N': '♘', 'P': '♙',  # White pieces
            'k': '♚', 'q': '♛', 'r': '♜', 'b': '♝', 'n': '♞', 'p': '♟',  # Black pieces
            ' ': ' ', '.': ' '  # Empty squares
        }
        return piece_map.get(piece, piece)
    
    def display(self):
        """Display the chess board with Unicode chess pieces - clean and simple
        
        Features:
        - Unicode chess pieces for better visual appeal
        - Clean grid layout with box drawing characters
        - Clear coordinate labels
        - Minimal clutter for easy reading
        """
        """Display the chess board with Unicode chess pieces - clean and simple"""
        print("\n" + "─" * 40)
        print("     a   b   c   d   e   f   g   h")
        print("   " + "┌" + "───┬" * 7 + "───┐")
        
        for i in range(8):
            row_num = 8 - i
            print(f" {row_num} │", end="")
            
            for j in range(8):
                piece = self.board[i][j]
                if piece == ' ':
                    display_piece = ' '
                else:
                    display_piece = self.piece_to_unicode(piece)
                
                print(f" {display_piece} │", end="")
            
            print(f" {row_num}")
            
            if i < 7:
                print("   ├" + "───┼" * 7 + "───┤")
        
        print("   └" + "───┴" * 7 + "───┘")
        print("     a   b   c   d   e   f   g   h")
        print("─" * 40)
        
        turn = "White" if self.to_move == 'w' else "Black"
        print(f"Turn: {turn}")
    
    def get_piece_at(self, square: str) -> str:
        """Get piece at algebraic notation square (e.g., 'e4')"""
        if len(square) != 2:
            return ' '
        
        col = ord(square[0].lower()) - ord('a')
        row = 8 - int(square[1])
        
        if 0 <= row < 8 and 0 <= col < 8:
            return self.board[row][col]
        return ' '
    
    def is_valid_move_format(self, move: str) -> bool:
        """Check if move is in valid algebraic notation"""
        # Simple patterns: Qh5, Nf3, e4, O-O, etc.
        patterns = [
            r'^[KQRBN][a-h][1-8]$',  # Piece moves like Qh5
            r'^[a-h][1-8]$',         # Pawn moves like e4
            r'^[KQRBN]x[a-h][1-8]$', # Captures like Qxh5
            r'^[a-h]x[a-h][1-8]$',   # Pawn captures like exd5
            r'^O-O$',                # Kingside castling
            r'^O-O-O$',              # Queenside castling
            r'^[KQRBN][a-h][1-8]\+$', # Check moves
            r'^[KQRBN][a-h][1-8]#$',  # Checkmate moves
        ]
        
        return any(re.match(pattern, move) for pattern in patterns)

class HauntedRoom:
    """Represents a haunted room with a chess puzzle"""
    
    def __init__(self, name: str, description: str, fen: str, solution: List[str], backstory: str):
        self.name = name
        self.description = description
        self.board = ChessBoard(fen)
        self.solution = solution  # List of acceptable moves
        self.backstory = backstory
        self.solved = False

class HauntedChessboard:
    """Main game class"""
    
    def __init__(self):
        self.player_health = 100
        self.current_room = 0
        self.rooms = self.create_rooms()
        self.game_over = False
        self.hall_of_souls_file = "hall_of_souls.txt"
    
    def create_rooms(self) -> List[HauntedRoom]:
        """Create the haunted rooms with chess puzzles"""
        rooms = [
            HauntedRoom(
                name="The Dusty Library",
                description="""You awaken in a dimly lit library, ancient books scattered everywhere.
A ghostly whisper echoes: 'Solve the puzzle... or remain forever...'
The chess board glows with an eerie light. White to move and mate in 1.""",
                fen="6k1/5ppp/8/8/8/8/5PPP/4Q1K1 w - - 0 1",
                solution=["Qe8#", "Qe8"],
                backstory="""As the pieces settle, you hear a voice from beyond:
'I was the mansion's chess master... trapped here when I failed to solve the final puzzle.
The next room holds darker secrets...'"""
            ),
            
            HauntedRoom(
                name="The Moonlit Parlor",
                description="""You enter a parlor bathed in pale moonlight. Portraits on the walls
seem to watch your every move. The temperature drops suddenly.
A spectral figure points at the board: 'White to move... mate in 2...'""",
                fen="r3k2r/ppp2ppp/2n5/2bqp3/2B1P3/3P1N2/PPP2PPP/R1BQK2R w KQkq - 0 1",
                solution=["Qd5", "Qd5+"],
                backstory="""The ghostly figure nods approvingly:
'Well done... I am the mansion's former owner. My obsession with chess
led to my downfall. One final challenge awaits in the master bedroom...'"""
            ),
            
            HauntedRoom(
                name="The Master Bedroom",
                description="""You enter the master bedroom where shadows dance on the walls.
An ornate chess set sits on a table beside a four-poster bed.
A deep, menacing voice booms: 'This is your final test... White to move and mate in 1.
Fail, and join us in eternal torment!'""",
                fen="6k1/6pp/8/8/8/8/6PP/R5K1 w - - 0 1",
                solution=["Ra8#", "Ra8"],
                backstory="""As you make the final move, the room fills with blinding light.
The spirits are finally at peace. You hear a gentle voice:
'Thank you for freeing us from this cursed game. The door is now open...'"""
            )
        ]
        return rooms
    
    def display_intro(self):
        """Display game introduction"""
        print("\n" + "="*60)
        print("🏚️  HAUNTED CHESSBOARD 🏚️")
        print("="*60)
        print("""
You wake up in a mysterious mansion, trapped by restless spirits.
The only way to escape is to solve their chess puzzles.

Each wrong move drains your life force...
Solve all puzzles to uncover the truth and escape!

Commands:
- Enter moves in algebraic notation (e.g., Qh5, Nf3, e4)
- Type 'hint' for a clue
- Type 'quit' to give up and remain trapped forever
        """)
        print("="*60)
        input("\nPress Enter to begin your haunting journey...")
    
    def display_health(self):
        """Display player health"""
        health_bar = "█" * (self.player_health // 10) + "░" * (10 - self.player_health // 10)
        print(f"\n💀 Life Force: [{health_bar}] {self.player_health}/100")
    
    def typewriter_effect(self, text: str, delay: float = 0.03):
        """Print text with typewriter effect"""
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()
    
    def display_victory_cutscene(self):
        """Display dramatic ASCII art victory cutscene"""
        print("\n" * 3)
        time.sleep(1)
        
        # Mansion breaking apart
        mansion_art = [
            """
    ╔══════════════════════════════════════════════════════════════╗
    ║                    THE MANSION TREMBLES...                   ║
    ╚══════════════════════════════════════════════════════════════╝
            """,
            """
                    🏚️ 💥 🏚️ 💥 🏚️ 💥 🏚️
                         ░░░░░░░░░░░░░░░░░
                        ░ WALLS CRACKING ░
                         ░░░░░░░░░░░░░░░░░
                    🏚️ 💥 🏚️ 💥 🏚️ 💥 🏚️
            """,
            """
            ╭─────────────────────────────────────────────────╮
            │  ⚡ CHAINS OF TORMENT BREAKING ⚡              │
            │                                                 │
            │    ⛓️💥  ⛓️💥  ⛓️💥  ⛓️💥  ⛓️💥           │
            │                                                 │
            │         SPIRITS ASCENDING TO PEACE...          │
            ╰─────────────────────────────────────────────────╯
            """,
            """
                        ✨ 👻 ✨ 👻 ✨ 👻 ✨
                           SOULS FREED!
                        ✨ 👻 ✨ 👻 ✨ 👻 ✨
            
                    🚪 THE DOOR OPENS WITH A CREAK... 🚪
            """,
            """
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║    🌅 SUNLIGHT STREAMS THROUGH THE DOORWAY 🌅              ║
    ║                                                              ║
    ║              YOU STEP INTO FREEDOM...                       ║
    ║                                                              ║
    ║    🚶‍♂️ ➡️  🚪 ➡️  🌳🌳🌳 ESCAPE! 🌳🌳🌳              ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝
            """
        ]
        
        for art in mansion_art:
            print(art)
            time.sleep(2)
        
        # Final victory message
        victory_text = """
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║  🎉🎉🎉 CONGRATULATIONS, CHESS MASTER! 🎉🎉🎉              ║
    ║                                                              ║
    ║     You have broken the curse of the Haunted Mansion!       ║
    ║                                                              ║
    ║    The spirits can finally rest in peace, thanks to your    ║
    ║              superior chess knowledge!                       ║
    ║                                                              ║
    ║  🏆 YOUR NAME SHALL BE RECORDED IN THE HALL OF SOULS 🏆     ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝
        """
        
        print(victory_text)
        time.sleep(2)
    
    def record_in_hall_of_souls(self):
        """Record the player's escape in the Hall of Souls"""
        print("\n" + "👻" * 50)
        print("ENTERING THE HALL OF SOULS...")
        print("👻" * 50)
        
        player_name = input("\n🏆 Enter your name for the Hall of Souls: ").strip()
        if not player_name:
            player_name = "Anonymous Hero"
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        health_remaining = self.player_health
        
        # Create entry for Hall of Souls
        entry = f"""
{'='*60}
🏆 SOUL FREED: {player_name}
📅 Date of Escape: {timestamp}
💀 Life Force Remaining: {health_remaining}/100
🏚️ Status: ESCAPED THE HAUNTED MANSION
⚡ Achievement: Chess Master of the Supernatural
{'='*60}
"""
        
        try:
            # Append to Hall of Souls file
            with open(self.hall_of_souls_file, 'a', encoding='utf-8') as f:
                f.write(entry)
            
            print(f"\n✅ Your escape has been recorded in the Hall of Souls!")
            print(f"📜 Check '{self.hall_of_souls_file}' to see all escaped souls.")
            
            # Display current Hall of Souls
            self.display_hall_of_souls()
            
        except Exception as e:
            print(f"❌ Could not record in Hall of Souls: {e}")
    
    def display_hall_of_souls(self):
        """Display the current Hall of Souls"""
        print("\n" + "👻" * 50)
        print("HALL OF SOULS - ESCAPED HEROES")
        print("👻" * 50)
        
        try:
            if os.path.exists(self.hall_of_souls_file):
                with open(self.hall_of_souls_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if content.strip():
                        print(content)
                    else:
                        print("The Hall of Souls is empty... You are the first to escape!")
            else:
                print("The Hall of Souls is empty... You are the first to escape!")
        except Exception as e:
            print(f"❌ Could not read Hall of Souls: {e}")
        
        print("👻" * 50)
    
    def play_room(self, room: HauntedRoom):
        """Play through a single room"""
        print("\n" + "🏚️ " * 20)
        print(f"ENTERING: {room.name.upper()}")
        print("🏚️ " * 20)
        
        self.typewriter_effect(room.description)
        
        while not room.solved and self.player_health > 0:
            self.display_health()
            room.board.display()
            
            move = input("\n👻 Enter your move (or 'hint'/'quit'): ").strip()
            
            if move.lower() == 'quit':
                print("\n💀 You give up and become another lost soul in the mansion...")
                self.game_over = True
                return
            
            if move.lower() == 'hint':
                self.give_hint(room)
                continue
            
            if not room.board.is_valid_move_format(move):
                print("❌ Invalid move format! Use algebraic notation (e.g., Qh5, Nf3)")
                continue
            
            if move in room.solution:
                print("\n✅ Correct! The spirits whisper their approval...")
                room.solved = True
                time.sleep(1)
                print("\n" + "="*50)
                self.typewriter_effect(room.backstory)
                print("="*50)
            else:
                self.player_health -= 10
                print(f"\n❌ Wrong move! The spirits grow angry... (-10 life force)")
                if self.player_health <= 0:
                    print("\n💀 Your life force is drained... You become part of the mansion forever...")
                    self.game_over = True
                    return
    
    def give_hint(self, room: HauntedRoom):
        """Provide hints for the current puzzle"""
        hints = {
            0: "👻 The queen can deliver mate from the back rank...",
            1: "👻 Look for a powerful central move with the queen...",
            2: "👻 The rook can deliver mate along the back rank..."
        }
        print(f"\n{hints.get(self.current_room, '👻 Study the board carefully...')}")
    
    def play(self):
        """Main game loop"""
        self.display_intro()
        
        while self.current_room < len(self.rooms) and not self.game_over and self.player_health > 0:
            self.play_room(self.rooms[self.current_room])
            
            if not self.game_over and self.rooms[self.current_room].solved:
                self.current_room += 1
                if self.current_room < len(self.rooms):
                    input("\nPress Enter to continue to the next room...")
        
        if self.current_room >= len(self.rooms) and not self.game_over:
            # Victory! Display cutscene and record in Hall of Souls
            self.display_victory_cutscene()
            self.record_in_hall_of_souls()
        
        print("\nThanks for playing Haunted Chessboard!")

def main():
    """Main function to start the game"""
    try:
        game = HauntedChessboard()
        game.play()
    except KeyboardInterrupt:
        print("\n\n💀 You flee in terror, leaving the spirits unsolved...")
    except Exception as e:
        print(f"\n❌ A supernatural error occurred: {e}")

if __name__ == "__main__":
    main()
