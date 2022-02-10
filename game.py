import pygame

pygame.init()

screen_width = 1000
screen_height = 1000

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('JWorld')



#load images
sun
run = True
while run == True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()

