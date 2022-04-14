import pygame
import sys

MAX_FPS = 15
IMAGES = {}

class Board:
    def __init__(self, dimension, width = 512, height = 512):
        self.DIMENSION = dimension
        self.WIDTH = width
        self.HEIGHT = height
        self.SQ_SIZE = height // dimension
        self.whiteToMove = True
        
        self.loadImages()
        self.resetBoard()

    def resetBoard(self):
        self.boardState = []

        for i in range(self.DIMENSION):
            for j in range(self.DIMENSION):
                if (j == 0):
                    self.boardState.append([])
                    self.boardState[i].append(None)
                else:
                    self.boardState[i].append(None)

    def loadImages(self):
        pieces = ['queen']
        for piece in pieces:
            IMAGES[piece] = pygame.transform.scale(pygame.image.load('images/' + piece + '.png'), (self.SQ_SIZE, self.SQ_SIZE))

    def show(self):
        pygame.init()
        pygame.display.set_caption('N Rainhas')
        pygame.display.set_icon(pygame.image.load('images/queen.png'))
        
        screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        clock = pygame.time.Clock()
        screen.fill(pygame.Color('white'))
        running = True

        while running:
            for e in pygame.event.get():
                if (e.type == pygame.QUIT):
                    running = False

            self.drawChessBoard(screen)
            clock.tick(MAX_FPS)
            pygame.display.flip()
        
        sys.exit(1)

    def drawChessBoard(self, screen):
        self.drawBoard(screen)
        self.drawPieces(screen)

    def drawBoard(self, screen):
        colors = [pygame.Color('light gray'), pygame.Color('dark gray')]
        for r in range(self.DIMENSION):
            for c in range(self.DIMENSION):
                color = colors[((r+c) % 2)]
                pygame.draw.rect(screen, color, pygame.Rect(c * self.SQ_SIZE, r * self.SQ_SIZE, self.SQ_SIZE, self.SQ_SIZE))
    
    def drawPieces(self, screen):
        for r in range(self.DIMENSION):
            for c in range(self.DIMENSION):
                piece = self.boardState[r][c]

                if (piece != None):
                    screen.blit(IMAGES[piece], pygame.Rect(c * self.SQ_SIZE, r * self.SQ_SIZE, self.SQ_SIZE, self.SQ_SIZE))
