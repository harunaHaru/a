import gambling
class GameState:
    def __init__(self):
        self.board=[
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']]
        
        self.functionpiece ={ 'p':self.getpawnmoves, 'R':self.getRockMoves, 'N':self.getKnightMoves, 
                             'B':self.getBishopMoves, 'Q':self.getQUEENMoves, 'K':self.getKingMoves}
        self.whiteToMove=True
        self.moveLog=[]
        self.whiteLocation=(7,4)
        self.blackLocation =(0,4)
        self.checkMate= False
        self.staleMate = False
        
    def makemove(self, move):
        self.board[move.startRow][move.startCol] = "--"
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.moveLog.append(move)
        self.whiteToMove =not self.whiteToMove #swap players
        if move.pieceMoved =="wK":
            self.whiteLocation = (move.endRow, move.endCol)
        if move.pieceMoved =="bK":
            self.blackLocation = (move.endRow, move.endCol)
        
    def undo(self):
        if len(self.moveLog) != 0 :
            move= self.moveLog.pop()
            self.board[move.startRow][move.startCol]= move.pieceMoved
            self.board[move.endRow][move.endCol]= move.pieceCaptured
            self.whiteToMove =not self.whiteToMove
            if move.pieceMoved =="wK":
                self.whiteLocation = (move.startRow, move.startCol)
            if move.pieceMoved =="bK":
                self.blackLocation = (move.startRow, move.startCol)
            
    def getValidmoves(self):
        #1.) generate all possible moves
        moves= self.getAllPossibleMoves()
         #2.) for each move,make the move
        for i in range(len(moves)-1,-1,-1):
            self.makemove(moves[i])
            #3.generate the oppennent's move
            #4.) for each of your opponnent's moves, see if they attack your king
            self.whiteToMove = not self.whiteToMove
            if self.checkIn:
                moves.remove(moves[i])
            self.whiteToMove = not self.whiteToMove
            self.undo()
        if len(moves)== 0:
            if self.checkIn():
                self.checkMate= True
            else:
                self.staleMate =True
        else:
            self.staleMate=False
            self.checkMate=False    
        
        return moves
    """
    ALL MOVES WİTHOUT CONSİDERİNG CHECKS
    """
    
    def getAllPossibleMoves(self):
        moves=[]
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                turn= self.board[r][c][0]
                if (turn == "w" and self.whiteToMove) or (turn == "b" and not self.whiteToMove):
                    piece =self.board[r][c][1]
                    self.functionpiece[piece](r, c, moves) #calls the appropriate move function based on piece type 
        return moves  
    
    def squarUnderAttack(self,r,c):
        self.whiteToMove = not self.whiteToMove
        oppMves= self.getAllPossibleMoves()
        self.whiteToMove = not self.whiteToMove
        for move in oppMves:
            if move.endRow == r and move.endCol == c:
                return True
        
        return False
    
    
    def checkIn(self):
        if self.whiteToMove:
            return self.squarUnderAttack(self.whiteLocation[0] , self.whiteLocation[1])
        else:
            return self.squarUnderAttack(self.blackLocation[0] , self.blackLocation[1])
      
                
        
              
    def getpawnmoves(self, r,c,moves):
        if self.whiteToMove:
            if self.board[r-1][c] == "--":
                moves.append(Move((r,c), ((r-1),c), self.board))
                if r== 6 and self.board[r-2][c] == "--":
                    moves.append(Move((r,c), ((r-2),c), self.board)) # (r,c) = a ((r-2), c) =b self.board = c Move(a,b,c)
            if c-1>= 0:# captured the left
                if self.board[r-1][c-1][0] == 'b':
                    moves.append(Move((r,c), (r-1, c-1) , self.board))
            if c+1 <= 7: # captured the right
                if self.board[r-1][c+1][0] == 'b':
                    moves.append(Move((r,c), (r-1, c+1), self.board))
        else: #black pawn move
            if self.board[r+1][c] == "--":
                moves.append(Move((r,c), ((r+1),c), self.board))
                if r== 1 and self.board[r+2][c] == "--":
                    moves.append(Move((r,c), ((r+2),c), self.board))
                if c-1>= 0:# captured the left (it's not changed )
                    if self.board[r+1][c-1][0] == 'w':
                        moves.append(Move((r,c), (r+1, c-1) , self.board))
                if c+1 <= 7: # captured the right (it's not changed)
                    if self.board[r+1][c+1][0] == 'w':
                        moves.append(Move((r,c), (r+1, c+1), self.board))
            #write yourself(sorry bro)
            
        #add pawn promotions later
    def getRockMoves(self ,r ,c, moves):
        direction= ((-1,0), (0,-1), (1,0), (0,1))#up ,left ,down ,right 
        enemycolor= 'b' if self.whiteToMove else 'w'
        for d in direction:
            for i in range(1,8):
                endRow= r + d[0] * i
                endCol= c + d[1] * i
                if 0 <= endRow <8 and 0 <= endCol <8:
                    endPiece= self.board[endRow][endCol]
                    if endPiece == '--':
                        moves.append(Move((r,c), (endRow, endCol), self.board))
                    elif  endPiece[0]==  enemycolor:
                        moves.append(Move((r,c), (endRow, endCol), self.board))
                        break
                    else:
                        break
                else:
                    break
                
    def getKnightMoves(self, r,c, moves):
        knightMoves= ((-1,-2),(-1,2),(-2,1), (-2,-1), (2,-1), (2,1), (1,2), (1,-2))#up ,left ,down ,right 
        Allycolor= 'w' if self.whiteToMove else 'b'
        for m in knightMoves:
            endRow= r + m[0]
            endCol= c + m[1]
            if 0 <= endRow <8 and 0 <= endCol <8:
                endPiece= self.board[endRow][endCol]
                if endPiece[0] != Allycolor:
                    moves.append(Move((r,c), (endRow, endCol), self.board))
          
    def getBishopMoves(self, r,c, moves):
        direction= ((-1,1), (1,-1), (1,1), (-1,-1))#up ,left ,down ,right 
        enemycolor= 'b' if self.whiteToMove else 'w'
        for d in direction:
            for i in range(1,8):
                endRow= r + d[0] * i
                endCol= c + d[1] * i
                if 0 <= endRow <8 and 0 <= endCol <8:
                    endPiece= self.board[endRow][endCol]
                    if endPiece == '--':
                        moves.append(Move((r,c), (endRow, endCol), self.board))
                    elif  endPiece[0]==  enemycolor:
                        moves.append(Move((r,c), (endRow, endCol), self.board))
                        break
                    else:
                        break
                else:
                    break
                
    def getQUEENMoves(self, r,c, moves):
        self.getBishopMoves( r,c, moves)
        self.getRockMoves( r, c , moves)
        
        
    def getKingMoves(self, r,c, moves):
        kingMoves=((-1,1), (1,-1), (1,1), (-1,-1), (1,0),(0,1),(-1,0),(0,-1))
        Allycolor= 'w' if self.whiteToMove else 'b'
        for m in range(8):
            
            endRow= r + kingMoves[m][0]
            endCol= c + kingMoves[m][1]
            if 0 <= endRow <8 and 0 <= endCol <8:
                endPiece= self.board[endRow][endCol]
                if endPiece[0] != Allycolor:
                    moves.append(Move((r,c), (endRow, endCol), self.board))
  
    
                    
class Move():
    ranksToRows= {"1":7, "2":6, "3":5, "4":4,
                  "5":3, "6":2, "7":1, "8":0}
    
    rowsToRank = {v:k for k ,v in ranksToRows.items()}
    
    filesToCols = {"a":0, "b":1,"c":2, "d":3,
                   "e":4, "f":5, "g":6, "h":7}
    
    ColsToFiles ={v:k for k , v in filesToCols.items()}
    
    def __init__(self, startSq, endSq, board):
        self.startRow = startSq[0]
        self.startCol= startSq[1]
        self.endRow =endSq[0]
        self.endCol =endSq[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured= board[self.endRow][self.endCol]
        self.MoveID = self.startRow *1000 + self.startCol*100+ self.endRow*10+ self.endCol
        
    def __eq__(self, other):
        if isinstance(other, Move):
            return self.MoveID == other.MoveID
        return False
    def getChesNotation(self):
        #you can add to make this real chees notation
        return self.getrankfile(self.startRow, self.startCol) + self.getrankfile(self.endRow, self.endCol)
    
    def getrankfile(self, r,c):
        return self.ColsToFiles[c] +self.rowsToRank[r]    
        
if __name__ == "__main__":
    gs= GameState()