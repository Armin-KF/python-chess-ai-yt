import stat


class Square:

    def __init__(app, row , col , piece=None):
        app.row = row
        app.col = col
        app.piece = piece



    def __eq__(app , other):
        return app.row == other.row and app.col == other.col


    def has_piece(app):
        return app.piece != None
    

    def isempty(app):
       return not app.has_piece()
    

    def has_team_piece(app , color):
        return app.has_piece() and app.piece.color == color
    

    def has_enemy_piece(app , color):
       return app.has_piece() and app.piece.color != color
    

    def is_empty_or_enemy(app , color):
       return app.isempty() or app.has_enemy_piece(color)



    @staticmethod
    def in_range(*args):
        for arg in args:
          if arg < 0 or arg > 7:
            return False

        return True  