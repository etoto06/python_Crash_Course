import pygame
import sys

import setting
from util import init, create_bullet, handle_key_event, update_bullets, render

screen, clock, image, screen_rect, ship_rect, bullets = init()

while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            handle_key_event(ship_rect, bullets, event) 
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
    new_bullets = update_bullets(screen_rect, bullets)

    screen.fill("purple")  # Fill the display with a solid color

    # Render the graphics here.
    render(screen, image, ship_rect, new_bullets)
    
    pygame.display.flip()  # Refresh on-screen display
    clock.tick(setting.FRAME_PER_SECOND)         # wait until next frame (at 60 FPS)