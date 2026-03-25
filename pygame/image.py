import pygame
pygame.init()
screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("adding image")
image=pygame.transform.scale(pygame.image.load("komi in the rain2.png").convert_alpha(),200,200)
rect=image.underscorerect(center=(500//2,500//2-30))
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    screen.blit(image,rect)
    pygame.display.flip()
pygame.quit()        