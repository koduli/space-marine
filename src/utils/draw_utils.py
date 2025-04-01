import pygame
from src.config.settings import WIDTH, HEIGHT, FONT_SIZE, FONT_COLOR, HEALTH_BAR_COLOR, HEALTH_BAR_BG_COLOR

def draw_health_bar(window, health):
    if health < 0: health = 0
    health_bar_length = 200
    health_bar_height = 30
    fill = (health / 100) * health_bar_length
    outline_rect = pygame.Rect(30, 30, health_bar_length, health_bar_height)
    fill_rect = pygame.Rect(30, 30, fill, health_bar_height)
    empty_rect = pygame.Rect(30 + fill, 30, health_bar_length - fill, health_bar_height)
    pygame.draw.rect(window, (255, 255, 255), outline_rect, 3)
    pygame.draw.rect(window, (0, 255, 0), fill_rect)
    pygame.draw.rect(window, (255, 255, 255), empty_rect, 3)
    pygame.draw.rect(window, (255, 0, 0), empty_rect)
    font = pygame.font.SysFont(None, 30)
    health_text = font.render(f"Health: {health}", True, (255, 255, 255))
    text_x = 30 + health_bar_length + 10
    text_y = 30 + (health_bar_height - health_text.get_height()) // 2
    window.blit(health_text, (text_x, text_y))

def draw_game(window, background, player, objects, offset_x):
    window.fill((255, 255, 255))
    window.blit(background, (0, 0))
    for obj in objects:
        obj.draw(window, offset_x)
    player.draw(window, offset_x)
    draw_health_bar(window, player.health)
    pygame.display.update()

def draw_end_screen(window, background):
    window.blit(background, (0, 0))
    font = pygame.font.SysFont(None, 100)
    
    restart_text = font.render("Restart", True, (0, 255, 0))
    quit_text = font.render("Quit", True, (255, 0, 0))
    
    restart_rect = restart_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
    quit_rect = quit_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 200))

    window.blit(restart_text, restart_rect)
    window.blit(quit_text, quit_rect)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if restart_rect.collidepoint(mouse_pos):
                    return True
                elif quit_rect.collidepoint(mouse_pos):
                    pygame.quit()
                    quit() 