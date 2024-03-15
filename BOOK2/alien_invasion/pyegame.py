import sys
import pygame
from PIL import Image
from PIL import ImageDraw

pygame.init()

screen = pygame.display.set_mode((1280,720))

clock = pygame.time.Clock()



bullet = pygame_rect(0,0,5,50)

for bullet in bullets:
    bullet top -=1
    
screen_rect = screen.get_rect()

image= pygame.image.load('images/ship.bmp')
image_rect = image.get_rect()

image_rect.midbottom = screen_rect.midbottom

image_rect.midbottom = screen15

while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.QUIT:
            if event.key == pygame.K_LEFT:
                image_rect.left -=1
            elif event.key == pygame.K_RIGHT:
                image_rect.left +=1
            elif event.key == pygame.K_UP:
                image_rect.top +=1
            elif event.key == pygame.K_DOWN:
                image_rect.top -=1
            elif event.key == pygame.K_SPACE:
                b = create_bullet(ship_rect)
    # Do logical updates here. 
    # ...
    

    screen.fill("black")  # Fill the display with a solid color

    # Render the graphics here. #방향키 렌더링 
    # ...
    screen.blit(image,image.get_rect())
    pygame.display.flip()  # Refresh on-screen display
    new_var = 60
    clock.tick(new_var)         # wait until next frame (at 60 FPS)
    
    