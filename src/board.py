from math import pi
from const import *
from piece import *
from square import Square
from move import Move
import copy



class Board: 

    def __init__(app):
         app.squares = [[0 , 0 , 0 , 0 , 0 , 0 , 0 , 0] for col in range(COLS)]
          
         app._create()
         app._add_pieces('white')
         app._add_pieces('black')


    def move_piece(app , piece , move):
        beforeMovePos = move.initial
        afterMovePos = move.final
    
        app.squares[beforeMovePos.row][beforeMovePos.col].piece = None
        app.squares[afterMovePos.row][afterMovePos.col].piece = piece
    
        piece.moved = True
    
        piece.reset_moves()


        
       
        


    def valid_move(app, piece , move):
        return move in piece.moves


    def in_check(app , piece , move):
        temp_piece = copy.deepcopy(piece)
        temp_board = copy.deepcopy(app)
        
        # Ensure move is a Move object
        if isinstance(move, Square):
            move = Move(move, move)  # Create a Move object with the same initial and final Square

        temp_board.move_piece(temp_piece , move)

        for row in range(ROWS):
            for col in range(COLS):
                if temp_board.squares[row][col].has_enemy_piece(piece.color):
                    p = temp_board.squares[row][col].piece
                    temp_board.calc_moves(p , row , col , bool = False)
                    for m in p.moves:
                        if isinstance(m.final.piece , King):
                            return True                        
        return False
    


    
    def is_checkmate(app, color):
        temp_app = copy.deepcopy(app)
        for row in range(ROWS):
            for col in range(COLS):
                if temp_app.squares[row][col].has_team_piece(color):
                    piece = temp_app.squares[row][col].piece
                    temp_app.calc_moves(piece, row, col, bool=False)
                    for move in piece.moves:
                        if not temp_app.in_check(piece, move):
                            return False
        return True


    def calc_moves(app , piece, row , col , bool = True):


        def sarbaz_move():
            if piece.moved:
                validsteps = 1
            else: 
                validsteps = 2

            start = row + piece.dir
            end = row + (piece.dir * (1+validsteps))
            for possible_move_row in range(start , end , piece.dir):
                if Square.in_range(possible_move_row):
                    move = None  # defult move 
                    if app.squares[possible_move_row][col].isempty():
                        initial = Square(row, col)
                        final = Square(possible_move_row, col)   

                        move = Move(initial , final)

                    if bool :
                        if move and not app.in_check(piece , move):  # Check if move is not None
                            piece.add_move(move) 
                    else :
                        if move:  # Check if move is not None
                            piece.add_move(move)
                else:
                    break


            possible_move_row = row + piece.dir
            possible_move_cols = [col-1 , col+1]
            for possible_move_col in possible_move_cols:
                if Square.in_range(possible_move_row , possible_move_col):
                    if app.squares[possible_move_row][possible_move_col].has_enemy_piece(piece.color):
                        initial = Square(row , col)
                        final_piece = app.squares[possible_move_row][possible_move_col].piece
                        final = Square(possible_move_row , possible_move_col , final_piece)
                        move = Move(initial , final)

                        if bool :
                         if move and not app.in_check(piece , move):  # Check if move is not None
                            piece.add_move(move) 
                        else :
                         if move:  # Check if move is not None
                            piece.add_move(move)
                        
                        
        
        def asb_moves():
            possible_moves = [
                (row-2 , col+1),
                (row-1, col+2),
                (row+1 , col+2),
                (row+2 , col+1),
                (row+2 , col-1),
                (row+1 , col-2),
                (row-1 , col-2),
                (row-2 , col-1),
            ]

            for possible_move in possible_moves:
                possible_move_row , possible_move_col = possible_move
               
                if Square.in_range(possible_move_row , possible_move_col):
                    if app.squares[possible_move_row][possible_move_col].is_empty_or_enemy(piece.color):
                        square_avalie = Square(row , col)
                        final_piece = app.squares[possible_move_row][possible_move_col].piece
                        square_final = Square(possible_move_row , possible_move_col , final_piece)
                        move = Move(square_avalie , square_final)
                        
                        if bool :
                         if move and not app.in_check(piece , move):  # Check if move is not None
                            piece.add_move(move) 
                         else:
                             break
                        else :
                         if move:  # Check if move is not None
                            piece.add_move(move)



        def straight_moves(incrs):
            for incr in incrs:
                row_incr , col_incr = incr
                possible_move_row = row + row_incr
                possible_move_col = col + col_incr

                while True:
                    if Square.in_range(possible_move_row , possible_move_col):
                        initial = Square(row , col)
                        final_piece = app.squares[possible_move_row][possible_move_col].piece
                        final = Square(possible_move_row , possible_move_col , final_piece)
                        move = Move(initial , final)

                        # خونه خالیه پس حرکت معتبره
                        if app.squares[possible_move_row][possible_move_col].isempty():
                            if bool :
                             if move and not app.in_check(piece , move):  # Check if move is not None
                              piece.add_move(move) 
                            else :
                             if move:  # Check if move is not None
                              piece.add_move(move)
                        
                        # خونه مهره حریف روشه با اینکه معتبره حرکت ولی لوپ باید برک شه
                        elif app.squares[possible_move_row][possible_move_col].has_enemy_piece(piece.color):
                           if bool :
                             if move and not app.in_check(piece , move):  # Check if move is not None
                              piece.add_move(move) 
                           else :
                             if move:  # Check if move is not None
                              piece.add_move(move)
                           break

                        # خونه مهره خودی روشه پس لوپ برک میشه
                        elif app.squares[possible_move_row][possible_move_col].has_team_piece(piece.color):
                            break

                    else :
                        break

                    possible_move_row = possible_move_row + row_incr 
                    possible_move_col = possible_move_col + col_incr



        def king_moves():
            king_moves = [
                (row-1 , col+0),
                (row-1 , col+1),
                (row+0 , col+1),
                (row+1 , col+1),
                (row+1 , col+0),
                (row+1 , col-1),
                (row+0 , col-1),
                (row-1 , col-1),
            ]
        
            for possible_move in king_moves:
                possible_move_row , possible_move_col = possible_move
                if Square.in_range(possible_move_row , possible_move_col):
                    if app.squares[possible_move_row][possible_move_col].is_empty_or_enemy(piece.color):
                        initial = Square(row , col)
                        final = Square(possible_move_row , possible_move_col)
                        move = Move(initial , final)
                        if bool :
                            # Create a copy of the board and apply the move
                            temp_board = copy.deepcopy(app)
                            temp_piece = copy.deepcopy(piece)
                            temp_board.move_piece(temp_piece, move)  
                            # Check if the king is still in check after the move
                            if not temp_board.in_check(temp_piece, final):  # Corrected line
                                piece.add_move(move)

                    
        if isinstance(piece , Sarbaz):
            sarbaz_move()

        elif isinstance(piece , Asb):
            asb_moves()

        elif isinstance(piece , Fil):
            straight_moves([
                (-1 , 1), # bal rast
                (1 , 1), # paien rast
                (1 , -1), # paien chap
                (-1 , -1), # bala chap
            ])

        elif isinstance(piece , Castle):
            straight_moves([
                (-1 , 0), # bala
                (1 , 0), # paien
                (0 , 1), # rast
                (0 , -1), # chap
            ])

        elif isinstance(piece , Queen):
            straight_moves([
                (-1 , 0), # bala
                (1 , 0), # paien
                (0 , 1), # rast
                (0 , -1), # chap
                (-1 , 1), # bala rast
                (1 , 1), # paien rast
                (1 , -1), # paien chap
                (-1 , -1), # bala chap
            ])

        elif isinstance(piece , King):
            king_moves()


    
         
    def _create(app):
     
        
        for row in range(ROWS):
            for col in range(COLS):
                app.squares[row][col] = Square(row , col )

    def _add_pieces(app , color):
        if color == 'white':
            row_sarbaz , row_other = (6 , 7)
        else :
            row_sarbaz , row_other = (1 , 0)
            
        # sarbaz
        for col in range(COLS):
            app.squares[row_sarbaz][col].piece = Sarbaz(color)
        
        # asb
        app.squares[row_other][1].piece = Asb(color)
        app.squares[row_other][6].piece = Asb(color)
        
        # fil
        app.squares[row_other][2].piece = Fil(color)
        app.squares[row_other][5].piece = Fil(color)

        
        
        # castle 
        app.squares[row_other][0].piece = Castle(color)
        app.squares[row_other][7].piece = Castle(color)

         

        # queen 
        app.squares[row_other][3].piece = Queen(color)

        

        # king 
        app.squares[row_other][4].piece = King(color)

      
