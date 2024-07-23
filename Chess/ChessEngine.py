# This class is responsible for storying all of the information about the current state of a chess game.  It will also be responible for determining the valid moves given for any scenario/state.  It will also keep a log of moves.

class GameState():
  def __init__(self):
    
    # board is a 8x8 2D list.  Each element of the list has 2 characters.
    # First character represents the color of the piece. (b or w)
    # Second character represents the type of piece. (R, N, B, Q, K, P).
    # "--" represents blank space. (no piece present)
    self.board = [
      ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"] ,
      ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
      ["--", "--", "--", "--", "--", "--", "--", "--",],
      ["--", "--", "--", "--", "--", "--", "--", "--",],
      ["--", "--", "--", "--", "--", "--", "--", "--",],
      ["--", "--", "--", "--", "--", "--", "--", "--",],
      ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp",],
      ["wR", "wN", "wB", "wQ", "wK", "wB", "wK", "wR"]
    ]
    self.whiteToMove = True
    self.moveLog = []