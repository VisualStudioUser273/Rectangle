import pygame
pygame.init()

screen=pygame.display.set_mode((500,750))

play=True
while play:

  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play=False

    class Rectangle():
        def __init__(self,color,dimensions):
            self.c=color
            self.d=dimensions
            self.s=screen
          
            

        def draw(self):
            pygame.draw.rect(self.s,self.c,self.d)    

    screen.fill("orchid 4")
    rect1=Rectangle((255,0,0),(50,20,100,100))
    rect2=Rectangle((255,0,0),(10,40,130,100))
    rect1.draw()
    rect2.draw()
    pygame.display.update()
