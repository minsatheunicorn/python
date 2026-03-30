import pygame
def main():
    pygame.init()
    s_w,s_h=500,500
    screen=pygame.display.set_mode((s_w,s_h))
    colors={
        "red":pygame.Color("red"),
        "green":pygame.Color("green"),
        "blue":pygame.Color("blue"),
        "yellow":pygame.Color("yellow"),
        "white":pygame.color("white")
    }