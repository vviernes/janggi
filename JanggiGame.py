from itertools import chain

class JanggiGame:
    '''Defines the template for the JanggiGame class.'''
    
    def __init__(self):
        '''
        Initializes a JanggiGame object with the following specified data attributes:
            _board : instantiates a Board object.
            _pieces : instantiates a Piece object.
            _player_turn : play begins with the blue player.
            _turn_counter : incremenets after each turn; used to determine player turn.
            _is_game_over : handles end-game conditions; when True, signals that the game is over.
        '''
        self._board = Board()
        self._pieces = Piece()
        self._player_turn = "blue"
        self._turn_counter = 1
        self._is_game_over = False

        # Instantiates each Piece object and creates a list of all Piece objects in the game
        self._all_pieces = list()
        self._players = ["red", "blue"]
        self._pieces = ["general", "guard", "elephant", "horse", "chariot", "cannon", "soldier"]
        for player in self._players:
            for piece in self._pieces:
                if player == "red":
                    if piece == "general":
                        self._all_pieces.append(Piece(player, "general", "e2"))
                    if piece == "guard":
                        self._all_pieces.append(Piece(player, "guard", "d1"))
                        self._all_pieces.append(Piece(player, "guard", "f1"))
                    if piece == "elephant":
                        self._all_pieces.append(Piece(player, "elephant", "b1")) 
                        self._all_pieces.append(Piece(player, "elephant", "g1")) 
                    if piece == "horse":
                        self._all_pieces.append(Piece(player, "horse", "c1")) 
                        self._all_pieces.append(Piece(player, "horse", "h1")) 
                    if piece == "chariot":
                        self._all_pieces.append(Piece(player, "chariot", "a1"))
                        self._all_pieces.append(Piece(player, "chariot", "i1"))
                    if piece == "cannon":
                        self._all_pieces.append(Piece(player, "cannon", "b3")) 
                        self._all_pieces.append(Piece(player, "cannon", "h3")) 
                    if piece == "soldier":
                        self._all_pieces.append(Piece(player, "soldier", "a4"))
                        self._all_pieces.append(Piece(player, "soldier", "c4"))
                        self._all_pieces.append(Piece(player, "soldier", "e4"))
                        self._all_pieces.append(Piece(player, "soldier", "g4"))
                        self._all_pieces.append(Piece(player, "soldier", "i4"))
                if player == "blue":
                    if piece == "general":
                        self._all_pieces.append(Piece(player, "general", "e9"))
                    if piece == "guard":
                        self._all_pieces.append(Piece(player, "guard", "d10"))
                        self._all_pieces.append(Piece(player, "guard", "f10"))
                    if piece == "elephant":
                        self._all_pieces.append(Piece(player, "elephant", "b10"))
                        self._all_pieces.append(Piece(player, "elephant", "g10"))
                    if piece == "horse":
                        self._all_pieces.append(Piece(player, "horse", "c10"))
                        self._all_pieces.append(Piece(player, "horse", "h10"))
                    if piece == "chariot":
                        self._all_pieces.append(Piece(player, "chariot", "a10"))
                        self._all_pieces.append(Piece(player, "chariot", "i10"))
                    if piece == "cannon":
                        self._all_pieces.append(Piece(player, "cannon", "b8"))
                        self._all_pieces.append(Piece(player, "cannon", "h8"))
                    if piece == "soldier":
                        self._all_pieces.append(Piece(player, "soldier", "a7"))
                        self._all_pieces.append(Piece(player, "soldier", "c7"))
                        self._all_pieces.append(Piece(player, "soldier", "e7"))
                        self._all_pieces.append(Piece(player, "soldier", "g7"))
                        self._all_pieces.append(Piece(player, "soldier", "i7"))

        # Places each Piece object in its appropriate Square object to finalize Board setup
        for square in self._board.get_boardmap().values():
            for piece in self._all_pieces:
                if square.get_square_position() == piece.get_piece_position():
                    square.place_piece(piece)
        
        # Displays a welcome message and prints a visual representation of the Board.
        print("")
        print("")
        print("Welcome to Janggi. The pieces and the board is now setup. Blue player goes first.")
        self._board.print_board()
       
    def get_player_turn(self):
        '''
        Returns the player whose turn it currently is.
        '''
        return self._player_turn
    
    def get_piece_on_square(self, square_position):
        '''
        Receives the square_position parameter and returns the Piece object that is occupying the 
        Square object associated with that square_position.
        '''
        return self._board._boardmap[square_position].get_piece()
    
    def get_piece_from_name(self, player, piece_type):
        '''
        Receieves the player and piece_type parameter and returns the Piece object associated with 
        that player and piece_type.
        '''
        for piece in self._all_pieces:
            if piece.get_player() == player and piece.get_piece_type() == piece_type:
                return piece

    def get_game_state(self):
        '''
        Describes if any conditions have been met to end the game. Returns 'BLUE_WON', 'RED_WON', 
        or 'UNIFINISHED', depending on whether or not a player has achieved the conditions for a 
        checkmate.
        '''
        if self._is_game_over == False:
            return 'UNFINISHED'
        if self._is_game_over == True:
            if self._player_turn == "blue":
                return 'RED_WON'
            if self._player_turn == "red":
                return 'BLUE_WON'
        
    def get_moves(self, from_pos):
        '''
        Receives the from_pos parameter, which is a string representation of a paricular square 
        location. From this square location, the function determines which Piece object currently 
        occupies it and maps out all the possible moves for that Piece, given the square location. 
        Returns a list containing all of this Piece's valid moves from the from_pos square.
        '''
        # piece_to_move is the Piece object currently occupying the square associated with from_pos
        piece_to_move = self.get_piece_on_square(from_pos)  
        
        # possible_moves serves as an intermediary list of possible moves for the Piece
        possible_moves = list()
        piece_column = piece_to_move.get_piece_position()[0]
        piece_row = piece_to_move.get_piece_position()[1:]

        # the variables below represent up/down/left/right movements on the Board. Since 
        # piece_column and piece_row are strings, these variables convert them to their associated 
        # ASCII code, which allows each move to be incremented and decremented by an integer value. 
        move_left = ord(piece_column)-1
        move_right = ord(piece_column)+1
        move_up = int(piece_row)-1                
        move_down = int(piece_row)+1                
        move_left2 = ord(piece_column)-2
        move_right2 = ord(piece_column)+2
        move_up2 = int(piece_row)-2               
        move_down2 = int(piece_row)+2             
        move_left3 = ord(piece_column)-3
        move_right3 = ord(piece_column)+3
        move_up3 = int(piece_row)-3               
        move_down3 = int(piece_row)+3      
        
     
        ''' 
        MOVE LOGIC FOR THE GENERAL AND GUARD PIECE:
            From the current position, moves one value left and appends the position to 
            possible_moves. Does the same for right/up/down positions. Constrains those movements 
            to the piece's respective palace. When the piece is on a corner square of the palace, 
            appends the diagonal movements as well.
        '''
        if piece_to_move.get_piece_type() == "general" or piece_to_move.get_piece_type() == "guard":
            # Conditions for bounding left/right movements within the both blue and red palaces.
            if move_left > 99:  # 99 is the ASCII code for the column 'c' 
                possible_moves.append(chr(move_left) + piece_row)
            if move_right < 103:  # 103 is the ASCII code for column 'g'
                possible_moves.append(chr(move_right) + piece_row)

            # conditions for bounding up/down movements within the blue palace 
            if piece_to_move.get_player() == "blue":
                if move_up > 7:         
                    possible_moves.append(piece_column + str(move_up))
                if move_down < 11:   
                    possible_moves.append(piece_column + str(move_down))
                
                # conditions for diagonal movements within the blue palace
                if (piece_to_move.get_piece_position() == "d8"
                    or piece_to_move.get_piece_position() == "d10"
                    or piece_to_move.get_piece_position() == "f8" 
                    or piece_to_move.get_piece_position() == "f10"):
                    possible_moves.append("e9")
                if piece_to_move.get_piece_position() == "e9":
                    possible_moves.append("d8")
                    possible_moves.append("f8")
                    possible_moves.append("d10")
                    possible_moves.append("f10")
            
            # conditions for bounding up/down movements within the red palace 
            if piece_to_move.get_player() == "red":
                if move_up > 0:         
                    possible_moves.append(piece_column + str(move_up))
                if move_down < 4:   
                    possible_moves.append(piece_column + str(move_down))

                # conditions for diagonal movements within the red palace
                if (piece_to_move.get_piece_position() == "d1"
                    or piece_to_move.get_piece_position() == "d3"
                    or piece_to_move.get_piece_position() == "f1"
                    or piece_to_move.get_piece_position() == "f3"):
                    possible_moves.append("e2")
                if piece_to_move.get_piece_position() == "e2":
                    possible_moves.append("d1")
                    possible_moves.append("f1")
                    possible_moves.append("d3")
                    possible_moves.append("f3")
        
        ''' 
        MOVE LOGIC FOR THE SOLDIER PIECE:
            From the current position, moves one value left and right and appends the position to 
            possible_moves. Does the same for moving forward one value. (Forward for the blue 
            solider means moving up on the board; forward for the red solider means down. 
            Constrains those movements to the boundaries of the board. When the piece is on a 
            corner square of the palace, appends the forward diagonal movements as well.
        '''
        if piece_to_move.get_piece_type() == "soldier":  
            # conditions for bounding left/right movement to the boundaries of the Board          
            if move_left > 96:  # 96 is the ASCII code "`", which precedes 'a'
                possible_moves.append(chr(move_left) + piece_row)
            if move_right < 106: # 106 is the ASCII code "j", which follows 'i'
                possible_moves.append(chr(move_right) + piece_row)
            if piece_to_move.get_player() == "blue" and move_up > 0:
                possible_moves.append(piece_column + str(move_up))
            if piece_to_move.get_player() == "red" and move_up < 11:
                possible_moves.append(piece_column + str(move_down))

            # conditions for moving within diagonals of the enemy's palace
            if piece_to_move.get_player() == "blue":
                if  (piece_to_move.get_piece_position() == "d3" 
                    or piece_to_move.get_piece_position() == "f3"):
                    possible_moves.append("e2")
                if piece_to_move.get_piece_position() == "e2":
                    possible_moves.append("d1")
                    possible_moves.append("f1")
            if piece_to_move.get_player()== "red":
                if (piece_to_move.get_piece_position() == "d8" 
                    or piece_to_move.get_piece_position() == "f8"):
                    possible_moves.append("e9")
                if piece_to_move.get_piece_position() == "e9":
                    possible_moves.append("d10")
                    possible_moves.append("f10")

        ''' 
        MOVE LOGIC FOR THE HORSE PIECE:
            From the current position, checks if moving two spaces in any direction is within the 
            bounds of the Board. If within bounds, checks if a square one away in that direction is 
            unoccupied. If so, then it appends the position of the squares that are a combination 
            of two values up/down + one value left/right away from its current position. Does the 
            same for the squares that are two values left/right + one value up/down away. 
        '''
        if piece_to_move.get_piece_type()  == "horse":
            # conditions for moving up 2 and left/right 1 (appends position only if within bounds)
            if move_up2 > 0:  
                if self._board._boardmap[piece_column+str(move_up)].get_occupied_by() == None:
                    if move_left > 96: 
                        possible_moves.append(chr(move_left)+str(move_up2))
                    if move_right < 106:
                        possible_moves.append(chr(move_right)+str(move_up2))
            # conditions for moving down 2 and left/right 1 (appends position only if within bounds)
            if move_down2 < 11 :  #
                if self._board._boardmap[piece_column+str(move_down)].get_occupied_by() == None:
                    if move_left > 96: 
                        possible_moves.append(chr(move_left)+str(move_down2))
                    if move_right < 106:
                        possible_moves.append(chr(move_right)+str(move_down2))
            # conditions for moving left 2 and up/down 1 (appends position only if within bounds)
            if move_left2 > 96:
                if self._board._boardmap[chr(move_left)+piece_row].get_occupied_by() == None:
                    if move_up > 0:
                        possible_moves.append(chr(move_left2)+str(move_up))
                    if move_down < 11:
                        possible_moves.append(chr(move_left2)+str(move_down))
            # conditions for moving right 2 and up/down 1 (appends position only if within bounds)
            if move_right2 < 106:
                if self._board._boardmap[chr(move_right)+piece_row].get_occupied_by() == None:
                    if move_up > 0:
                        possible_moves.append(chr(move_right2)+str(move_up))
                    if move_down < 11:
                        possible_moves.append(chr(move_right2)+str(move_down))

        ''' 
        MOVE LOGIC FOR THE ELEPHANT PIECE:
            Functions similarly to the Horse piece, but moves in a combination of 3 values up/down 
            with 2 values left/right, or vice versa.
        '''
        if piece_to_move.get_piece_type()  == "elephant":
            # conditions for moving up 3 and left/right 2 (appends position only if within bounds)
            if move_up3 > 0:
                if self._board._boardmap[piece_column+str(move_up)].get_occupied_by() == None:
                    if move_left2 > 96: 
                        possible_moves.append(chr(move_left2)+str(move_up3))
                    if move_right2 < 106:
                        possible_moves.append(chr(move_right2)+str(move_up3))
            # conditions for moving down 3 and left/right 2 (appends position only if within bounds)
            if move_down3 < 11 :
                if self._board._boardmap[piece_column+str(move_down)].get_occupied_by() == None:
                    if move_left2 > 96: 
                        possible_moves.append(chr(move_left2)+str(move_down3))
                    if move_right2 < 106:
                        possible_moves.append(chr(move_right2)+str(move_down3))
            # conditions for moving left 3 and up/down 2 (appends position only if within bounds)
            if move_left3 > 96:
                if self._board._boardmap[chr(move_left)+piece_row].get_occupied_by() == None:
                    if move_up2 > 0:
                        possible_moves.append(chr(move_left3)+str(move_up2))
                    if move_down2 < 11:
                        possible_moves.append(chr(move_left3)+str(move_down2))
            # conditions for moving left 3 and up/down 2 (appends position only if within bounds)
            if move_right3 < 106:
                if self._board._boardmap[chr(move_right)+piece_row].get_occupied_by() == None:
                    if move_up2 > 0:
                        possible_moves.append(chr(move_right3)+str(move_up2))
                    if move_down2 < 11:
                        possible_moves.append(chr(move_right3)+str(move_down2))

        ''' 
        MOVE LOGIC FOR THE CHARIOT PIECE:
            From its current position, checks if the square ahead of it is unoccupied. If so, 
            appends that position to possible_moves. Then it checks two squares ahead of the current 
            possition and appends that position if the square unoccupied. Continues to check +1 away.
            When it encounters a square that is occupied, checks if the piece in that occupied 
            square is friendly or not. Appends the square if an enemy piece is on that square. 
            Variables are resetted and the process is repeated for the remaining directions. If the 
            chariot is in a palace, appends diagonal movements within the palace if it is occupying 
            the corner squares of the palace.
        '''
        if piece_to_move.get_piece_type()  == "chariot":
            files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
            ranks = [str(1), str(2), str(3), str(4), str(5), str(6), str(7), str(8), str(9), str(10)]
            
            # conditions are vertical movement
            for file in files:
                if file == piece_column:
                    # conditions for moving up
                    while move_up > 0 and self._board._boardmap[file+str(move_up)].get_occupied_by() == None:  
                        possible_moves.append(file+str(move_up))
                        move_up -= 1
                    if move_up > 0:
                        if (self._board._boardmap[file+str(move_up)].get_occupied_by() != self.get_player_turn()):
                            possible_moves.append(file+str(move_up))   # append to capture
                    # conditions for moving down
                    while move_down < 11 and self._board._boardmap[file+str(move_down)].get_piece() is None: 
                            possible_moves.append(file+str(move_down))
                            move_down += 1
                    if move_down < 11:
                        if self._board._boardmap[file+str(move_down)].get_occupied_by() != self.get_player_turn():
                            possible_moves.append(file+str(move_down))  # append to capture
                    
            # conditions are horizontal movement
            for rank in ranks:
                if rank == piece_row:
                    for file in files:
                        # conditions for moving left
                        while move_left > 96 and self._board._boardmap[chr(move_left)+rank].get_piece() is None: 
                            possible_moves.append(chr(move_left)+rank)
                            move_left -= 1
                        if move_left > 96:
                            if self._board._boardmap[chr(move_left)+rank].get_occupied_by() != self.get_player_turn():
                                possible_moves.append(chr(move_left)+rank)  # append to capture
                                
                        # conditions for moving right
                        while move_right < 106 and self._board._boardmap[chr(move_right)+rank].get_piece() is None: 
                            possible_moves.append(chr(move_right)+rank)
                            move_right += 1
                        if move_right < 106:
                            if self._board._boardmap[chr(move_right)+rank].get_occupied_by() != self.get_player_turn():
                                possible_moves.append(chr(move_right)+rank)  # append to capture
            
            # conditions for moving diagonally in blue palace
            if piece_to_move.get_piece_position() == "e9":
                possible_moves.append("d8")
                possible_moves.append("d10")
                possible_moves.append("f8")
                possible_moves.append("f10")
            if piece_to_move.get_piece_position() == "d8":
                possible_moves.append("e9")
                if self._board._boardmap["e9"].get_occupied_by() == None:
                    possible_moves.append("f10")
            if piece_to_move.get_piece_position() == "f8":
                possible_moves.append("e9")
                if self._board._boardmap["e9"].get_occupied_by() == None:
                    possible_moves.append("d10")
            if piece_to_move.get_piece_position() == "d10":
                possible_moves.append("e9")
                if self._board._boardmap["e9"].get_occupied_by() == None:
                    possible_moves.append("f8")
            if piece_to_move.get_piece_position() == "f10":
                possible_moves.append("e9")
                if self._board._boardmap["e9"].get_occupied_by() == None:
                    possible_moves.append("d8")

            # conditions for moving diagonally in red palace
            if piece_to_move.get_piece_position() == "e2":
                possible_moves.append("d1")
                possible_moves.append("d3")
                possible_moves.append("f1")
                possible_moves.append("f3")
            if piece_to_move.get_piece_position() == "d1":
                possible_moves.append("e2")
                if self._board._boardmap["e2"].get_occupied_by() == None:
                    possible_moves.append("f3")
            if piece_to_move.get_piece_position() == "f1":
                possible_moves.append("e2")
                if self._board._boardmap["e2"].get_occupied_by() == None:
                    possible_moves.append("d3")
            if piece_to_move.get_piece_position() == "d3":
                possible_moves.append("e2")
                if self._board._boardmap["e2"].get_occupied_by() == None:
                    possible_moves.append("f1")
            if piece_to_move.get_piece_position() == "f3":
                possible_moves.append("e2")
                if self._board._boardmap["e2"].get_occupied_by() == None:
                    possible_moves.append("d1")

        ''' 
        MOVE LOGIC FOR THE CANNON PIECE:
            Functions similarly to the Chariot piece. The main difference is that when it is 
            searching for potential squares to append, it keeps track of how many pieces it has 
            encountered. For example, consider how the Cannon piece will append squares below it's 
            current position. First, it will check if the square one down from it is unoccupied. If 
            so, it will continue to move down until it encounters a piece. If it doesn't, then it is 
            unable to move in that direction. If it encounters a piece (and if it's not a cannon), 
            then this is the piece the cannon and "jump over". After jumping, the function continue 
            checks for unoccupied squares in the down direction. For each unoccupied square it 
            encounters after the jump, it appends that square to possible_moves. It continues to do 
            so until it encounters a second piece. Once it does, it checks to see if that piece is 
            friendly or not. If not, it appends that square location as it is possible to capture 
            this piece. Performs this sequence for all directions. When occupying the corner squares 
            of either palace, the Cannon is able to jump diagonally as well (assuming the center 
            palace square is occupied).
        '''
        if piece_to_move.get_piece_type() == "cannon":
            files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
            ranks = [str(1), str(2), str(3), str(4), str(5), str(6), str(7), str(8), str(9), str(10)]
            
            # conditions for vertical movement
            for file in files:
                if file == piece_column:
                    encountered_pieces = 0
                    encountered_cannon = False
                    # conditions for moving up
                    while move_up > 0 and encountered_pieces == 0:
                        if self._board._boardmap[file+str(move_up)].get_occupied_by() != None:
                            encountered_pieces = 1
                            if self.get_piece_on_square(file+str(move_up)).get_piece_type() == "cannon":
                                encountered_cannon = True
                        move_up -= 1
                    if encountered_cannon == False:
                        while move_up > 0 and encountered_pieces == 1:
                            if self._board._boardmap[file+str(move_up)].get_occupied_by() == None:
                                possible_moves.append(file+str(move_up))
                                move_up -= 1
                            elif self._board._boardmap[file+str(move_up)].get_occupied_by() != None:
                                encountered_pieces = 2
                    if move_up > 0 and self._board._boardmap[file+str(move_up)].get_occupied_by() != None:
                        if self._board._boardmap[file+str(move_up)].get_occupied_by() != self.get_player_turn():
                            if self.get_piece_on_square(file+str(move_up)).get_piece_type() != piece_to_move.get_player():
                                possible_moves.append(file+str(move_up))
                    move_up = int(piece_row)-1
                    encountered_pieces = 0
                    encountered_cannon = False

                    # conditions for moving down
                    while move_down < 11 and encountered_pieces == 0:
                        if self._board._boardmap[file+str(move_down)].get_occupied_by() != None:
                            encountered_pieces = 1
                            if self.get_piece_on_square(file+str(move_down)).get_piece_type() == "cannon":
                                encountered_cannon = True
                        move_down += 1
                    if encountered_cannon == False:
                        while move_down < 11 and encountered_pieces == 1:
                            if self._board._boardmap[file+str(move_down)].get_occupied_by() == None:
                                possible_moves.append(file+str(move_down))
                                move_down += 1
                            elif self._board._boardmap[file+str(move_down)].get_occupied_by() != None:
                                encountered_pieces = 2
                    if move_down < 11 and self._board._boardmap[file+str(move_down)].get_occupied_by() != None:
                        if self._board._boardmap[file+str(move_down)].get_occupied_by() != piece_to_move.get_player():
                            if self.get_piece_on_square(file+str(move_down)).get_piece_type() != "cannon":
                                possible_moves.append(file+str(move_down))
                    move_down = int(piece_row)+1  

            # conditions for horizontal movement
            for rank in ranks:
                if rank == piece_row:
                    encountered_pieces = 0
                    encountered_cannon = False

                    # conditions for moving left
                    while move_left > 96 and encountered_pieces == 0:
                        if self._board._boardmap[chr(move_left)+rank].get_occupied_by() != None:
                            encountered_pieces = 1
                            if self.get_piece_on_square(chr(move_left)+rank).get_piece_type() == "cannon":
                                encountered_cannon = True
                        move_left-= 1
                    if encountered_cannon == False:
                        while move_left > 96 and encountered_pieces == 1:
                            if self._board._boardmap[chr(move_left)+rank].get_occupied_by() == None:
                                possible_moves.append(chr(move_left)+rank)
                                move_left-= 1
                            elif self._board._boardmap[chr(move_left)+rank].get_occupied_by() != None:
                                encountered_pieces = 2
                    if move_left > 96 and self._board._boardmap[chr(move_left)+rank].get_occupied_by() != None:
                        if self._board._boardmap[chr(move_left)+rank].get_occupied_by() != piece_to_move.get_player():
                            if self.get_piece_on_square(chr(move_left)+rank).get_piece_type() != "cannon":
                                possible_moves.append(chr(move_left)+rank)
                    move_left= ord(piece_column)-1
                    encountered_pieces = 0
                    encountered_cannon = False

                    # conditions for moving right
                    while move_right < 106 and encountered_pieces == 0:
                        if self._board._boardmap[chr(move_right)+rank].get_occupied_by() != None:
                            encountered_pieces = 1
                            if self.get_piece_on_square(chr(move_right)+rank).get_piece_type() == "cannon":
                                encountered_cannon = True
                        move_right += 1
                    if encountered_cannon == False:
                        while move_right < 106 and encountered_pieces == 1:
                            if self._board._boardmap[chr(move_right)+rank].get_occupied_by() == None:
                                possible_moves.append(chr(move_right)+rank)
                                move_right += 1
                            elif self._board._boardmap[chr(move_right)+rank].get_occupied_by() != None:
                                encountered_pieces = 2
                    if move_right < 106 and self._board._boardmap[chr(move_right)+rank].get_occupied_by() != None:
                        if self._board._boardmap[chr(move_right)+rank].get_occupied_by() != piece_to_move.get_player():
                            if self.get_piece_on_square(chr(move_right)+rank).get_piece_type() != "cannon":
                                possible_moves.append(chr(move_right)+rank)
                    move_right = ord(piece_column)+1

            # diagonal movement in blue palace
            if self._board._boardmap["e9"].get_occupied_by() != None:
                if piece_to_move.get_piece_position() == "d8":
                    possible_moves.append("f10")
                if piece_to_move.get_piece_position() == "f10":
                    possible_moves.append("d8")
                if piece_to_move.get_piece_position() == "f8":
                    possible_moves.append("d10")
                if piece_to_move.get_piece_position() == "d10":
                    possible_moves.append("f8")

            # diagonal movement in red palace
            if self._board._boardmap["e2"].get_occupied_by() != None:
                if piece_to_move.get_piece_position() == "d3":
                    possible_moves.append("f1")
                if piece_to_move.get_piece_position() == "f1":
                    possible_moves.append("d3")
                if piece_to_move.get_piece_position() == "f3":
                    possible_moves.append("d1")
                if piece_to_move.get_piece_position() == "d1":
                    possible_moves.append("f3")

        # Instantiates an empty list called final_moves which will represent all valid moves for a 
        # given piece. Appends the current square position (representing passing one's turn). Then, 
        # for each move in possible_moves, only appends to final_moves the squares that are empty or 
        # occupied by enemy pieces. 
        final_moves = list()
        final_moves.append(from_pos)
        for move in possible_moves:
            if (self._board.get_square_from_position(move).get_occupied_by() == None 
                or self.get_piece_on_square(move).get_player() != piece_to_move.get_player()):
                final_moves.append(move) 
        return list(set(final_moves))

    def get_attacking_moves(self, player):
        '''
        A helper function for is_in_check. Receives the player parameter and returns a list of all 
        possible moves for all possible pieces that can perform on their turn.
        '''
        if player == "blue":
            all_blue_moves = list()
            for piece in self._all_pieces: 
                if piece.get_player() == "blue":
                    try:
                        # for each blue piece, call the get_moves method and appends the list of 
                        # moves to all_blue_moves
                        all_blue_moves.append(self.get_moves(piece.get_piece_position()))
                    except AttributeError:  # error handling for pieces with no valid moves
                        pass
            attacking_moves = list(set(list(chain.from_iterable(all_blue_moves))))

        if player == "red":
            all_red_moves = list()
            for piece in self._all_pieces: 
                if piece.get_player() == "red":
                    try:
                        all_red_moves.append(self.get_moves(piece.get_piece_position()))
                    except AttributeError:
                        pass
            attacking_moves = list(set(list(chain.from_iterable(all_red_moves))))

        return attacking_moves
    
    def is_in_check(self, player):
        '''
        Receives the player parameter (red or blue), and determines if the player is in check. Return 
        True if so, otherwise returns False. In addition, if the player is in check, the function 
        calls the is_in_mate function to determine if the player is in checkmate.
        '''
        general_piece = self.get_piece_from_name(player, "general")
        general_position = general_piece.get_piece_position()
        attacking_moves = list()

        # for the given player, calls the helper function get_attacking_moves to get a list of all 
        # possible moves the opponent can make for all pieces on the board. 
        if player == "red":
            attacking_moves = self.get_attacking_moves("blue")
        if player == "blue":
            attacking_moves = self.get_attacking_moves("red")
        
        # if the player's general is in a square position that is a member the opponent's list of 
        # attacking_moves, then it is in check. 
        if general_position in attacking_moves:
            self._is_game_over = self.is_in_mate(player)  # function call to is_in_mate
            if self._is_game_over == True:
                print(f"{self._player_turn.upper()} is checkmated.")
            return True
        elif general_position not in attacking_moves:
            return False

    def is_in_mate(self, player):
        '''
        A helper function to is_in_check. Receives the player parameter and returns whether or not 
        the player is in checkmate.
        '''
        general_piece = self.get_piece_from_name(player, "general")  # the general piece object
        general_position= general_piece.get_piece_position()  
        general_moves = self.get_moves(general_position)  # the general's valid moves from its square

        safe_moves = list()  # a list of possible moves for the general that leave it uncaptured
        opponent_attacking_moves = list()

        # calls get_attacking_moves to get a list of the opponent's possible attack moves
        if player == "red":
            opponent_attacking_moves = self.get_attacking_moves("blue")
        if player == "blue":
            opponent_attacking_moves = self.get_attacking_moves("red")

        # appends to safe_moves all the general's moves that the opposing player cannot attack. If no 
        # safe move exists, the player is in checkmate. Otherwise, the player is not in checkmate. 
        for move in general_moves:
            if move not in opponent_attacking_moves:
                safe_moves.append(move)
        if not safe_moves:
            return True
        else:
            return False

    def make_move(self, from_pos, to_pos):
        '''
        Receives as parameters the from_pos(the starting square position) and to_pos(the target 
        square position). Performs that move for the piece that occupies to_pos. Returns True if the 
        requested move; returns False otherwise.
        '''
        # players can only make move is game is not over
        if self.get_game_state() == 'UNFINISHED':  
            piece_to_move = self.get_piece_on_square(from_pos)  # the Piece object
            home_square = self._board.get_square_from_position(from_pos)  # a Square object
            target_square = self._board.get_square_from_position(to_pos)  # a Square object

            if piece_to_move is None:
                print("Invalid. No piece occupies that square. Try again.")
                return False

            if piece_to_move.get_captured() == True:
                print("Invalid. This piece has already been captured. Try again.")
                return False
                            
            if piece_to_move.get_player() != self._player_turn:
                print("Invalid. The piece belongs to the opposing player. Try again.")
                return False
            
            # represents when a player chooses to pass their turn
            if from_pos == to_pos:
                self.change_turn()
                return True

            # performs a series of function calls when a valid move is performed:
                    #   · occupying piece on target square is 'captured'
                    #   · places the piece on the target square
                    #   · sets the piece's position to the targeted square
                    #   · sets the previous square to None as it is now unoccupied
                    #   · change player turn
            if to_pos in self.get_moves(from_pos): 
                if target_square.get_piece() != None:
                    target_square.get_piece().set_captured()
                target_square.place_piece(piece_to_move)     
                piece_to_move.set_piece_position(to_pos)     
                home_square.clear_square()                    
                self.change_turn()                            
                return True
            else:
                print("Invalid move for this particular piece. Enter another.")
                return False

        # if a checkmate has been achieved and the game is over, display ending message.
        elif self.get_game_state() == "RED_WON":
            print("Game over. Red player wins.")

        elif self.get_game_state() == "BLUE_WON":
            print("Game over. Blue player wins.")
   
    def change_turn(self):
        '''
        Changes the player_turn by incrementing _turn_counter after a move has been performed.
        '''
        self._turn_counter += 1
        if self._turn_counter % 2 == 1:
            self._player_turn = "blue"
        else:
            self._player_turn = "red"


class Board:
    '''Defines the template of the Board class.'''
    
    def __init__(self):
        '''
        Initializes a Board object with the following specified data attributes:
            _column : a list of all the Board's columns
            _row : a list of all the Board's row
            _boardmap : a mapping of each Square's position to its associated Square object
        '''
        self._column = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
        self._row = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        self._boardmap = dict()
        
        # Instanstiates every Square object that compose the Board; maps it's position (as a string) 
        # to the Square object itself and adds this key, value pair to _boardmap.
        for column in self._column:
            for row in self._row:
                self._boardmap[column+row] = Square(column, row, None)
    
    def get_boardmap(self):
        '''
        Returns _boardmap, which is the dictionary that contain each Square position mapped to its 
        Square object.
        '''
        return self._boardmap

    def get_square_from_position(self, position):
        '''
        Receives a position parameter that represents a square position as a string. Returns the 
        Square object associated with that position.
        '''
        return self._boardmap[position]

    def print_board(self):
        '''
        Displays a visual representation of the board layout along with the pieces on their 
        appropriate square locations. 
        '''
        self._display = dict()
        for square in self._boardmap.keys():
            if self._boardmap[square].get_piece() is not None:
                self._display[square] = self._boardmap[square].get_piece().display_piece()
            elif self._boardmap[square].get_piece() is None:
                self._display[square] = '     '
        self._viz_board = (f'''
                A       B       C       D      E        F       G      H       I
           +-------+-------+-------+-------+-------+-------+-------+-------+-------+
         1 | {self._display["a1"]} | {self._display["b1"]} | {self._display["c1"]} | {self._display["d1"]} | {self._display["e1"]} | {self._display["f1"]} | {self._display["g1"]} | {self._display["h1"]} | {self._display["i1"]} |
           +-------+-------+-------+-------+-------+-------+-------+-------+-------+
         2 | {self._display["a2"]} | {self._display["b2"]} | {self._display["c2"]} | {self._display["d2"]} | {self._display["e2"]} | {self._display["f2"]} | {self._display["g2"]} | {self._display["h2"]} | {self._display["i2"]} |
           +-------+-------+-------+-------+-------+-------+-------+-------+-------+
         3 | {self._display["a3"]} | {self._display["b3"]} | {self._display["c3"]} | {self._display["d3"]} | {self._display["e3"]} | {self._display["f3"]} | {self._display["g3"]} | {self._display["h3"]} | {self._display["i3"]} |
           +-------+-------+-------+-------+-------+-------+-------+-------+-------+
         4 | {self._display["a4"]} | {self._display["b4"]} | {self._display["c4"]} | {self._display["d4"]} | {self._display["e4"]} | {self._display["f4"]} | {self._display["g4"]} | {self._display["h4"]} | {self._display["i4"]} |
           +-------+-------+-------+-------+-------+-------+-------+-------+-------+
         5 | {self._display["a5"]} | {self._display["b5"]} | {self._display["c5"]} | {self._display["d5"]} | {self._display["e5"]} | {self._display["f5"]} | {self._display["g5"]} | {self._display["h5"]} | {self._display["i5"]} |
           +-------+-------+-------+-------+-------+-------+-------+-------+-------+
         6 | {self._display["a6"]} | {self._display["b6"]} | {self._display["c6"]} | {self._display["d6"]} | {self._display["e6"]} | {self._display["f6"]} | {self._display["g6"]} | {self._display["h6"]} | {self._display["i6"]} |
           +-------+-------+-------+-------+-------+-------+-------+-------+-------+
         7 | {self._display["a7"]} | {self._display["b7"]} | {self._display["c7"]} | {self._display["d7"]} | {self._display["e7"]} | {self._display["f7"]} | {self._display["g7"]} | {self._display["h7"]} | {self._display["i7"]} |
           +-------+-------+-------+-------+-------+-------+-------+-------+-------+
         8 | {self._display["a8"]} | {self._display["b8"]} | {self._display["c8"]} | {self._display["d8"]} | {self._display["e8"]} | {self._display["f8"]} | {self._display["g8"]} | {self._display["h8"]} | {self._display["i8"]} |
           +-------+-------+-------+-------+-------+-------+-------+-------+-------+
         9 | {self._display["a9"]} | {self._display["b9"]} | {self._display["c9"]} | {self._display["d9"]} | {self._display["e9"]} | {self._display["f9"]} | {self._display["g9"]} | {self._display["h9"]} | {self._display["i9"]} |
           +-------+-------+-------+-------+-------+-------+-------+-------+-------+
        10 | {self._display["a10"]} | {self._display["b10"]} | {self._display["c10"]} | {self._display["d10"]} | {self._display["e10"]} | {self._display["f10"]} | {self._display["g10"]} | {self._display["h10"]} | {self._display["i10"]} |
           +-------+-------+-------+-------+-------+-------+-------+-------+-------+
                A       B       C       D      E        F       G      H       I
           ''')  
        print(self._viz_board)

    
class Square(Board):
    '''Defines the template of the Square subclass of Board.'''

    def __init__(self, column, row, piece=None):
        '''
        Initializes a Square object with the following specified data attributes:
            _column : describes a Square's column attribute
            _row : describes a Square's row attribute
            _square_position : describes a Square's position attribute
            _piece: the piece object that is occupying the Square
        '''
        self._column = column
        self._row = row
        self._square_position = column+row
        self._piece = piece                     
            
    def get_column(self):
        '''
        Returns the square's column attribute.
        '''
        return self._column
    
    def get_row(self):
        '''
        Returns the square's row attribute.
        '''
        return self._row

    def get_square_position(self):
        '''
        Returns the square's position attribute.
        '''
        return self._square_position

    def get_piece(self):
        '''
        Returns the piece occuyping the square; if no piece is occupying it, then returns None.
        '''
        return self._piece

    def get_occupied_by(self):
        '''
        Returns whether or not a square is occupied or not. If occupied, returns what player is 
        currently occupying the square. Otherwise, returns None.
        '''
        if self._piece == None:
            return None
        if self._piece != None:
            return self._piece.get_player()

    def place_piece(self, piece):
        '''
        Receives a piece object as a paramter and sets it to _piece when a piece object occupies it.
        '''
        self._piece = piece

    def clear_square(self):
        '''
        Sets a square's _piece parameter to None when a piece object leaves it.
        '''
        self._piece = None
   

class Piece:
    '''Defines the template of the Piece class.'''

    def __init__(self, player=None, piece_type=None, piece_position=None):
        '''
        Initializes a Piece object with its specified attributes:
            _player: describes to which player the Piece belongs (red or blue)
            _piece_type = describes the Piece's type (general, chariot, cannon, etc.)
            _position: describes the board position of the Piece
            _captured: describes whether the piece has been captured or not
        '''        
        self._player = player
        self._piece_type = piece_type
        self._piece_position = piece_position
        self._captured = False

    def get_player(self):
        '''
        Returns the player to which the Piece belongs.
        '''
        return self._player
    
    def get_piece_type(self):
        '''
        Returns the Piece type.
        '''
        return self._piece_type 

    def get_piece_position(self):
        '''
        Returns the Piece's current position on the board.
        '''
        return self._piece_position

    def get_captured(self):
        '''
        Returns whether the Piece has been captured or not.
        '''
        return self._captured

    def set_piece_position(self, piece_position):
        '''
        Receives a position on the Board and sets the Piece's position attribute to it.
        '''
        self._piece_position = piece_position

    def set_captured(self):
        '''
        Sets the captured attribute of a Piece to True if captured by the opponent.
        '''
        self._captured = True
    
    def display_piece(self):
        '''
        Determines how a Piece object is to be visually represented on the game board.
        '''
        return self._player[0].upper() + "." + self._piece_type[0:3].upper()
