# This class is responsible for storying all of the information about the current state of a chess game.  It will also be responible for determining the valid moves given for any scenario/state.  It will also keep a log of moves.


class GameState:
    def __init__(self):
        # board is a 8x8 2D list. Each element of the list has 2 characters.
        # First character represents the color of the piece. (b or w)
        # Second character represents the type of piece. (R, N, B, Q, K, P).
        # "--" represents blank space. (no piece present)
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
        ]
        self.whiteToMove = True
        self.moveLog = []
 
    # takes a Move as a param and executes.  (this will not work for castling)
    def makeMove(self, move: 'Move'):
        self.board[move.startRow][move.startCol] = "--" # change to empty space after moving piece.
        self.board[move.endRow][move.endCol] = move.pieceMoved  
        self.moveLog.append(move)  # Log the move so we can undo it later
        self.whiteToMove = not self.whiteToMove  # Swap players after each move
        
        

    # UNDO the last move made.
    def undoMove(self):
        if len(self.moveLog) != 0:
            move = self.moveLog.pop()
            self.board[move.startRow][move.startCol] = move.pieceMoved
            self.board[move.endRow][move.endCol] = move.pieceCaptured
            self.whiteToMove = not self.whiteToMove # Switch turn back

class Move:
    # maps keys to values for proper chess notation
    # key : value
    ranksToRows = {"1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0}
    rowsToRanks = {v: k for k, v in ranksToRows.items()}
    filesToCols = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
    colsToFiles = {v: k for k, v in filesToCols.items()}

    def __init__(self, startSq: tuple[int, int], endSq: tuple[int, int], board: list[list[str]]):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]

    def getChessNotation(self) -> str:
        return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(
            self.endRow, self.endCol
        )

    def getRankFile(self, r: int, c: int) -> str:
        return self.colsToFiles[c] + self.rowsToRanks[r]
