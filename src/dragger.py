import pygame

from const import *


class Dragger:

    def __init__(app):
        app.piece = None
        app.dragging = False
        app.mouseX = 0
        app.mouseY = 0
        app.row_avalie = 0 
        app.col_final = 0




    def update_blit(app , surface):
        app.piece.set_texture(size=128)
        texture = app.piece.texture

        img = pygame.image.load(texture)

        img_center = (app.mouseX , app.mouseY)
        app.piece.rect = img.get_rect(center=img_center)

        surface.blit(img , app.piece.rect)

    def update_mouse(app , pos):
        app.mouseX , app.mouseY = pos


    def save_initial(app, pos ):
        app.row_avalie = pos[1] // SQSIZE
        app.col_final = pos[0] // SQSIZE


    def drag_piece(app , piece):
        app.piece = piece
        app.dragging = True


    def drop_piece(app):
        app.piece = None
        app.dragging = False