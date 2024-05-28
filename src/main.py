import pygame
import sys

from const import *
from game import Game
from piece import Piece
from square import Square
from move import Move




class Main: 

    def __init__(app):
        pygame.init()
        app.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('شطرنج')
        app.game = Game()
        app.checkmate = False

    def mainloop(app):

        game = app.game
        board = app.game.board
        screen = app.screen
        dragger = app.game.dragger


        while True:
            app.game.show_board(screen)
            app.game.show_moves(screen)
            app.game.show_pieces(screen)


            if dragger.dragging:
                dragger.update_blit(screen)

            for event in pygame.event.get():
                

                # click
                if event.type == pygame.MOUSEBUTTONDOWN and not app.checkmate:
                    dragger.update_mouse(event.pos)
                    
                    clicked_row = dragger.mouseY // SQSIZE
                    clicked_col = dragger.mouseX // SQSIZE

                   


                    # if click has a piece
                    if board.squares[clicked_row][clicked_col].has_piece(): 
                        piece = board.squares[clicked_row][clicked_col].piece
                        board.calc_moves(piece , clicked_row , clicked_col, bool = True)
                        dragger.save_initial(event.pos)
                        dragger.drag_piece(piece)

                        game.show_board(screen)
                        game.show_moves(screen)
                        game.show_pieces(screen)


                # mouse motion
                elif event.type == pygame.MOUSEMOTION and not app.checkmate:
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        game.show_board(screen)
                        
                        game.show_moves(screen)
                        game.show_pieces(screen)
                        dragger.update_blit(screen)


                # click release
                elif event.type == pygame.MOUSEBUTTONUP and not app.checkmate:
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        relased_row = dragger.mouseY // SQSIZE
                
                        relased_col = dragger.mouseX // SQSIZE
                        

                        first = Square(dragger.row_avalie , dragger.col_final)
                        final = Square(relased_row , relased_col)
                        move = Move(first , final)

                        if board.valid_move(dragger.piece , move):
                            board.move_piece(dragger.piece , move)
                            game.show_board(screen)
                            game.show_pieces(screen)

                        
                        if game.is_checkmate():
                                app.checkmate = True
                              
                                
                               
                    dragger.drop_piece()



                # quit
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
     
            if app.checkmate:
                font = pygame.font.SysFont('Arial', 72)
                text = font.render('Checkmate', True, (255, 0, 0))
                text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
                screen.blit(text, text_rect)

                    
            pygame.display.update()

main = Main()
main.mainloop()