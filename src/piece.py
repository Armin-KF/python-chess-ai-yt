import os

class Piece:
    def __init__(app, name, color, texture=None, texture_rect=None):
        app.name = name
        app.color = color
        value_sign = 1 if color == 'white' else -1 
        app.moves = []
        app.moved = False
        app.texture = texture
        app.set_texture()
        app.texture_rect = texture_rect

    def set_texture(app, size=80):
        app.texture = os.path.join(
            f'assets/images/imgs-{size}px/{app.color}_{app.name}.png')

    def add_move(app, move):
        app.moves.append(move)


    def reset_moves(app):
        app.moves = []


class Sarbaz(Piece):
    def __init__(app, color):
        if color == 'white':
            app.dir = -1
        else:
            app.dir = 1
        super().__init__('sarbaz', color)


class Asb(Piece):
    def __init__(app, color):
        super().__init__('asb', color)


class Fil(Piece):
    def __init__(app, color):
        super().__init__('fil', color)


class Castle(Piece):
    def __init__(app, color):
        super().__init__('castle', color)


class Queen(Piece):
    def __init__(app, color):
        super().__init__('queen', color)


class King(Piece):
    def __init__(app, color):
        super().__init__('king', color)