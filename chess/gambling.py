import random
import chessEngine
import pygame as p
import chessMain
class Gambling():
    def __init__(self):
        self.WIDTH = self.HEIGHT  = 512
        self.BOTTOM_SQ_SIZE = self.WIDTH//3
        self.WHITE = (255, 255, 255) 
        self.BLACK = (0, 0, 0) 
        self.GRAY = (128, 128, 128)
        
    def gamb(self,screen):
    
        self.r_ad=['wp', 'wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR','bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR','bp']
        self.resimler = [ i + '.png' for i in self.r_ad]
            
        rastgele_resim_dosyaları = random.sample(self.resimler, 3)

        self.ras_res = [p.image.load(dosya) for dosya in rastgele_resim_dosyaları]
        r_w = r_h= 200
        #for i, res in enumerate(self.ras_res):
            #screen.blit(self.ras_res[i], p.Rect(150 + i * 300, 200, r_w, r_h))

    def draw_bottom_squares(self, screen):
        for i in range(3):
              #if True:
            #p.draw.rect(screen, self.GRAY, p.Rect(i * self.BOTTOM_SQ_SIZE, self.HEIGHT - self.BOTTOM_SQ_SIZE, self.BOTTOM_SQ_SIZE, self.BOTTOM_SQ_SIZE)) 
                screen.blit( self.ras_res[i], p.Rect(i *  self.BOTTOM_SQ_SIZE, self.HEIGHT - self.BOTTOM_SQ_SIZE, self.BOTTOM_SQ_SIZE, self.BOTTOM_SQ_SIZE))
#The enumerate() function in Python adds a counter to an iterable and returns it as an enumerate object. This is
# particularly useful when you need both the index and the value while iterating over
# a list, tuple, or any other iterable



if __name__ == "__main__":
    chessMain.GameState()
    chessEngine.main()
    
    
    
    
    

    