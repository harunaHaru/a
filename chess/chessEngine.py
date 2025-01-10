import pygame as p
import chessMain
import gambling
WIDTH = HEIGHT  = 512
DIMENSION= 8
SQ_SIZE= HEIGHT// DIMENSION
MAX_FPS=15
IMAGES={}

def loadImage():
    pieces=['wp', 'wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR','bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR','bp']
    for  piece in pieces:     
        IMAGES[piece] =p.transform.scale(p.image.load(piece + ".png"), (SQ_SIZE, SQ_SIZE)) #pygame is here as p
        pass
def main():
    p.init()
    screen= p.display.set_mode((WIDTH, HEIGHT+200))   
    clock= p.time.Clock()
    screen.fill(p.Color("white"))
    gs= chessMain.GameState()
    #gamb= gambling.Gambling()
    validMoves =gs.getValidmoves()
    loadImage()
    
    moveMade= False
    running= True
    sqselected= () #no square is selected, keep track of the last click of the user 
    playerClick= [] #keep track of player clicks (two tuples: [(4,4), (6,4)])
    
    while running:
       
        for e in p.event.get():
            if e.type ==p.QUIT:
                running=False
            elif e.type == p.MOUSEBUTTONDOWN:
                location= p.mouse.get_pos()#(x,y) location of mouse
                col= location[0] //SQ_SIZE
                row = location[1] //SQ_SIZE
                if sqselected == (row,col): #the user clicked the same square twice
                    sqselected=() #deselcted
                    playerClick=[] #clear player clicks
                else:
                    sqselected =(row, col)
                    playerClick.append(sqselected)
                if len(playerClick) ==2: #after 2nd click
                    move = chessMain.Move(playerClick[0], playerClick[1], gs.board)
                    print(move.getChesNotation())
                    if move in validMoves:
                        gs.makemove(move)
                        moveMade=True
                        sqselected= ()
                        playerClick=[]
                    else:
                        playerClick = [sqselected]
            elif e.type == p.KEYDOWN:
                if e.key == p.K_z: #undo when 'z' is pressed
                    gs.undo()   
                    moveMade=True     
        if moveMade:
            validMoves= gs.getValidmoves()
            moveMade= False
                
        drawGameState(screen, gs)#gamb
        clock.tick(MAX_FPS)
        
        p.display.flip()
        
            
def drawGameState(screen, gs ):#gamb
    drawBoard(screen)
    drawPieces(screen, gs)# draw pieces on top pf those squart
    #gamb.gamb(screen)
    #gamb.draw_bottom_squares(screen)
    
    
def drawBoard(screen):
    colors= [p.Color("white"), p.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color= colors[((r+c) % 2)]
            p.draw.rect(screen,color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE,SQ_SIZE))   
            
def drawPieces(screen, gs):
   for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = gs.board[r][c]
            if piece != "--":
                screen.blit( IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE,SQ_SIZE))

if __name__ == "__main__":
    main()