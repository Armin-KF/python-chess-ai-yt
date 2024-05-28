from math import pi
import pygame 

from const import *
from board import Board
from dragger import Dragger

class Game: 
            
    def __init__(app):
        app.board = Board()
        app.dragger = Dragger()

    def show_board(app , surface):
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    color = (234, 235 , 200)
                else:
                    color = (119, 148, 85)

                rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)
                pygame.draw.rect(surface, color, rect)

    def show_pieces(app , surface):
        for row in range (ROWS):
            for col in range(COLS):
                if app.board.squares[row][col].has_piece():
                    piece = app.board.squares[row][col].piece


                    if piece is not app.dragger.piece:
                        piece.set_texture(size=80)
                        img = pygame.image.load(piece.texture)
                        img_center = col * SQSIZE + SQSIZE // 2 , row * SQSIZE + SQSIZE // 2
                        piece.texture_rect = img.get_rect(center = img_center)
                        surface.blit(img, piece.texture_rect)
    
    def is_checkmate(app):
        return app.board.is_checkmate('white') or app.board.is_checkmate('black')

    def show_moves(app, surface):
        if app.dragger.dragging:
            piece = app.dragger.piece

            for move in piece.moves:
                color = '#C86464' if (move.final.row + move.final.col) % 2 == 0 else '#C84646'

                rect = (move.final.col * SQSIZE, move.final.row * SQSIZE, SQSIZE, SQSIZE)

                pygame.draw.rect(surface, color, rect)