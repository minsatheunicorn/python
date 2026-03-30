import pygame
pygame.init()
screen=pygame.display.set_mode((400,400))
screen.fill((255,255,255))
done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    pygame.draw.circle(screen,(0,255,0),(300,300),50)
    pygame.draw.circle(screen,(0,255,0),(100,100),50,3)
    pygame.display.flip