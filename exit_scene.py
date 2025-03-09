import pygame

def exit_screen(screen, clock, fps, player_score):
    screen.fill("black")
    # Show scores
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Your Score: {player_score}", True, (255, 255, 255))
    # An exit button
    exit_button = pygame.Rect(screen.get_width() // 2 - 50, screen.get_height() // 2 + 50, 100, 50)
    # Check for exit button click
    running = True
    while running:
        screen.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button.collidepoint(event.pos):
                    running = False
        # Draw exit button
        pygame.draw.rect(screen, (255, 0, 0), exit_button)
        screen.blit(font.render("Exit", True, (255, 255, 255)), (exit_button.x + 25, exit_button.y + 12))
        
        # Draw score
        screen.blit(score_text, (screen.get_width() // 2 - score_text.get_width() // 2, screen.get_height() // 2 - 20))
        pygame.display.flip()
        clock.tick(fps)
    
    