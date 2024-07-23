# This is our main driver file.  It will be responsible for handling user input and displaying the current GameState Object #


import pygame as p
from Chess import ChessEngine
import sys

WIDTH = HEIGHT = 512
DIMENSION = 8  # Dimensions of chess board (8x8)
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}


# Initialize a global dictionary of images.  This will be called exactly once in the main.


def loadImages():
    pieces = ["wp", "wR", "wN", "wB", "wQ", "wK", "bp", "bR", "bN", "bB", "bQ", "bK"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(
            p.image.load("chess/images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE)
        )


# Note: We can access an image by saying 'IMAGES['wp']'


# Main driver, This will handle user input and updating the Graphics.
def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    loadImages()  # ONLY DO THIS ONCE, before the while loop
    running = True
    sqSelected = ()  # No square selected, keep track of the last click of the user (tuple: (row, col))
    playerClicks = []  # keep track of player clicks (two tuples: [(6, 3), (4, 4)])

    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
                p.quit()
                sys.exit()

            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()  # X & Y location of the mouse.
                col = location[0] // SQ_SIZE
                row = location[1] // SQ_SIZE
                if sqSelected == (
                    row,
                    col,
                ):  # if the user clicks the same square twice.
                    sqSelected = ()  # deselect
                    playerClicks = []  # clear player clicks
                else:
                    sqSelected = (row, col)
                    playerClicks.append(
                        sqSelected
                    )  # append for both 1st and 2nd Clicks.
                if len(playerClicks) == 2:  # after second click
                    move = ChessEngine.Move(playerClicks[0], playerClicks[1], gs.board)
                    print(move.getChessNotation())
                    gs.makeMove(move)
                    sqSelected = () # Reset user clicks.
                    playerClicks = []

        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()

    # p.quit()
    # sys.exit()


# Responsible for all graphics within a current Game State.
def drawGameState(screen, gs):
    drawBoard(screen)  # Draw squares on board
    # add in piece highlighting or move suggestions (later)
    drawPieces(screen, gs.board)  # draw pieces on top of those squares.


# draw squares on the board.
def drawBoard(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            color = colors[
                ((row + col) % 2)
            ]  # light squares coordinates add up to even, dark squares add up to odd.
            p.draw.rect(
                screen, color, p.Rect(col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE)
            )


# draw the peices on the board using the current GameState.board
def drawPieces(screen, board):
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            piece = board[row][col]
            if piece != "--":  # not empty square
                screen.blit(
                    IMAGES[piece],
                    p.Rect(col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE),
                )


if __name__ == "__main__":
    main()
