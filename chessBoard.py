import pygame as pg

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
            clock.tick(MAX_FPS)
            pg.display.flip()

    def drawChessBoard(self, screen):
        drawBoard(screen)
        drawPieces(screen)

    def drawBoard(self, screen):
        colors = [pg.Color('white'), pg.Color('gray')]
        # for r in DIMENSION:
        #     for c in DIMENSION
    
    def drawPieces(seld, screen, board):
        pass

########################################################################################################################


if (__name__ == '__main__'):
    Board().show()