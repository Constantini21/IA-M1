import pygame as pg
import sys

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

class Board():
    def __init__(self):
        self.boardState = [
        ['--', 'queen', '--', '--', '--', '--', '--', '--'],
        ['--', '--', '--', '--', '--', '--', '--', '--'],
        ['--', '--', '--', '--', '--', '--', '--', '--'],
        ['--', '--', '--', '--', '--', '--', '--', '--'],
        ['--', '--', '--', '--', '--', '--', '--', '--'],
        ['--', '--', '--', '--', '--', '--', '--', '--'],
        ['--', '--', '--', '--', '--', '--', '--', '--'],
        ['--', '--', '--', '--', '--', '--', '--', '--']
        ]

        self.whiteToMove = True
        self.moveLog = []

    def loadImages(self):
        pieces = ['queen']
        for piece in pieces:
            IMAGES[piece] = pg.transform.scale(pg.image.load('images/' + piece + '.png'), (SQ_SIZE, SQ_SIZE))

    def show(self):
        pg.init()
        screen = pg.display.set_mode((WIDTH, HEIGHT))
        clock = pg.time.Clock()
        screen.fill(pg.Color('white'))
        self.loadImages()
        running = True

        while running:
            for e in pg.event.get():
                if (e.type == pg.QUIT):
                    running = False

            self.drawChessBoard(screen)
            clock.tick(MAX_FPS)
            pg.display.flip()
        
        sys.exit(1)

    def drawChessBoard(self, screen):
        self.drawBoard(screen)
        self.drawPieces(screen)

    def drawBoard(self, screen):
        colors = [pg.Color('light gray'), pg.Color('dark gray')]
        for r in range(DIMENSION):
            for c in range(DIMENSION):
                color = colors[((r+c) % 2)]
                pg.draw.rect(screen, color, pg.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))
    
    def drawPieces(self, screen):
        for r in range(DIMENSION):
            for c in range(DIMENSION):
                piece = self.boardState[r][c]

                if (piece != '--'):
                    screen.blit(IMAGES[piece], pg.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))

if (__name__ == '__main__'):
    Board().show()