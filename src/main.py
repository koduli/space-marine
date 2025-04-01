import pygame
import sys
from src.config.settings import WIDTH, HEIGHT, FPS, PLAYER_VEL, ASSETS_DIR, FONT_SIZE, FONT_COLOR
from src.utils.sprite_utils import get_background
from src.utils.draw_utils import draw_game, draw_end_screen
from src.entities.player import Player
from src.entities.level import Level

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Platformer")
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.font = pygame.font.Font(None, FONT_SIZE)
        
        self.background = get_background()
        self.game_over_img = pygame.image.load(f'src/{ASSETS_DIR}/Background/game_over.png').convert()
        self.you_won_img = pygame.image.load(f'src/{ASSETS_DIR}/Background/you_won.png').convert()
        
        self.level = Level()
        self.player = self.level.player
        self.offset_x = 0
        self.scroll_area_width = 200
        self.game_state = "playing"
        self.restart_button = pygame.Rect(WIDTH//2 - 100, HEIGHT//2 + 50, 200, 50)
        self.restart_text = self.font.render("Restart", True, FONT_COLOR)
        self.restart_text_rect = self.restart_text.get_rect(center=self.restart_button.center)

    def handle_vertical_collision(self, player, objects, dy):
        collided_objects = []
        for obj in objects:
            if pygame.sprite.collide_mask(player, obj):
                if dy > 0:
                    player.rect.bottom = obj.rect.top
                    player.landed()
                elif dy < 0:
                    player.rect.top = obj.rect.bottom
                    player.hit_head()
                collided_objects.append(obj)
        return collided_objects

    def handle_move(self, player, objects):
        keys = pygame.key.get_pressed()
        player.x_vel = 0

        if player.rect.left < 0:
            player.rect.left = 0
        elif player.rect.right > WIDTH:
            player.rect.right = WIDTH

        if keys[pygame.K_LEFT] and player.rect.left > 0:
            player.move_left(PLAYER_VEL)
        if keys[pygame.K_RIGHT] and player.rect.right < WIDTH:
            player.move_right(PLAYER_VEL)

        vertical_collide = self.handle_vertical_collision(player, objects, player.y_vel)
        for obj in vertical_collide:
            if obj and obj.name == "fire":
                player.take_damage(25)

    def handle_end_screen(self, image, run, playing):
        restart_rect, quit_rect = draw_end_screen(self.screen, image)
        waiting_for_input = True

        while waiting_for_input:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    playing = False
                    run = False
                    waiting_for_input = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if restart_rect.collidepoint(mouse_pos):
                        run = False
                        waiting_for_input = False
                    elif quit_rect.collidepoint(mouse_pos):
                        playing = False
                        run = False
                        waiting_for_input = False

        return run, playing

    def run(self):
        playing = True
        while playing:
            player = Player(300, 800, 50, 50)
            level = Level()
            offset_x = 0
            run = True

            while run:
                self.clock.tick(FPS)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        playing = False
                        run = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE and player.jump_count < 2:
                            player.jump()

                if player.rect.right >= WIDTH:
                    if draw_end_screen(self.screen, self.you_won_img):
                        run = False
                    else:
                        playing = False
                        run = False
                        continue

                if player.health <= 0:
                    if draw_end_screen(self.screen, self.game_over_img):
                        run = False
                    else:
                        playing = False
                        run = False
                        continue

                player.loop(FPS)
                for obj in level.objects:
                    if hasattr(obj, 'loop'):
                        obj.loop()
                self.handle_move(player, level.objects)
                draw_game(self.screen, self.background, player, level.objects, offset_x)

        pygame.quit()
        sys.exit()

def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main() 