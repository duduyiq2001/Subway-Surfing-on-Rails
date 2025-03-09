import pygame

def start_screen(screen, fps, clock):
    # Constants
    MIDDLE_X = 550
    TITLE_Y = 150
    Color_WHITE = (255, 255, 255)
    Color_RED = (255, 0, 0)
    Color_GREEN = (0, 255, 0)
    
    screen.fill("black")
    # input box
    input_box = pygame.Rect(MIDDLE_X+100, 500, 140, 32)
    text = ''
    input_box_active = False
    font = pygame.font.Font(None, 32)
    title_font = pygame.font.Font(None, 64)
    # button
    button_single = pygame.Rect(MIDDLE_X, 300, 200, 32)
    button_multi = pygame.Rect(MIDDLE_X, 400, 200, 32)
    single_text = font.render("Single Player", True, Color_WHITE)
    multi_text = font.render("Multi Player", True, Color_WHITE)
    
    while True:
        screen.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            # input box
            if event.type == pygame.MOUSEBUTTONUP:
                if input_box.collidepoint(event.pos):
                    input_box_active = True
                else:
                    input_box_active = False
            if event.type == pygame.KEYDOWN:
                if input_box_active:
                    if event.key == pygame.K_RETURN:
                        pass
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode  
            # button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_single.collidepoint(event.pos):
                    print("Single Player")
                    return text, "single"
                elif button_multi.collidepoint(event.pos):
                    print("Multi Player")
                    return text, "multi"
        # draw title
        screen.blit(title_font.render("Subway Surfing on Rails", True, Color_WHITE), (MIDDLE_X-150, TITLE_Y))
        
        # draw text before input box
        screen.blit(font.render("Enter Player Id:", True, Color_WHITE), (MIDDLE_X-95, 505))
        
        # draw input box
        color = Color_RED if input_box_active else Color_WHITE
        pygame.draw.rect(screen, color, input_box, 2)
        
        # draw text
        text_surface = font.render(text, True, color)
        screen.blit(text_surface, (input_box.x+5, input_box.y+5))

        # draw button
        pygame.draw.rect(screen, Color_GREEN, button_single)
        pygame.draw.rect(screen, Color_GREEN, button_multi)
        screen.blit(single_text, (button_single.x+25, button_single.y+5))
        screen.blit(multi_text, (button_multi.x+25, button_multi.y+5))
        
        pygame.display.flip()                
        clock.tick(fps)