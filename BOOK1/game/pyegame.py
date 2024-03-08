import sys
import pygame
from PIL import Image
from PIL import ImageDraw

pygame.init()

screen = pygame.display.set_mode((1280,720))

clock = pygame.time.Clock()
image= pygame.image.load('')
rect = image.get_rect()

while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Do logical updates here. 
    # ...
    

    screen.fill("black")  # Fill the display with a solid color

    # Render the graphics here. #방향키 렌더링 
    # ...
    screen.blit(image,rect)

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)
    