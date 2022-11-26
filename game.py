import pygame
from random import randint
from settings import WIDTH, HEIGHT, PULSE, FONT_URL, FONT_SIZE, BG_MUSIC_URL, CRASH_MUSIC_URL, BG_MUSIC_VOLUME, CRASH_MUSIC_VOLUME
from background import Background
from terrain import Ground
from aeroplane import Aeroplane
from obstacles import Obstacle

"""
This module is used to run the flappy-plane game.
"""


class Game:
    """
    Game Engine.
    """

    def __init__(self):

        # Initializing pygame
        pygame.init()

        # Creating the game screen
        self.display_surface = pygame.display.set_mode((WIDTH, HEIGHT))

        # Creating the clock instance
        self.clock = pygame.time.Clock()
        self.start_offset = self.clock.tick()

        # Pause and play flag
        self.is_paused = False

        # Setting the window/title caption
        pygame.display.set_caption("Flappy Plane")

        # Creating sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

        # Font
        self.font = pygame.font.Font(FONT_URL, FONT_SIZE)

        # Creating the sprite objects
        Background([self.all_sprites])
        Ground([self.all_sprites, self.collision_sprites])

        # Creating timer
        self.obstacle_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.obstacle_timer, PULSE)

        # Music
        self.music = pygame.mixer.Sound(BG_MUSIC_URL)
        self.music.set_volume(BG_MUSIC_VOLUME)
        self.music.play(loops=-1)

        # Creating the aeroplane sprite
        self.aeroplane = Aeroplane([self.all_sprites])

        self.score = 0

        self.is_alive = True

    def display_score(self):
        """
        This method is used to display the score on the screen.
        """

        if self.is_alive and not self.is_paused:
            self.score = (pygame.time.get_ticks() - self.start_offset) // 1000
        score_surf = self.font.render(str(self.score), True, "black")
        score_rect = score_surf.get_rect(midtop=(WIDTH / 2, HEIGHT / 10))
        self.display_surface.blit(score_surf, score_rect)

    def check_collision(self) -> bool:
        if (
            pygame.sprite.spritecollide(
                self.aeroplane,
                self.collision_sprites,
                False,
                pygame.sprite.collide_mask,
            )
            or self.aeroplane.rect.top <= 0
        ):
            crash_music = pygame.mixer.Sound(CRASH_MUSIC_URL)
            crash_music.set_volume(CRASH_MUSIC_VOLUME)
            crash_music.play()
            self.is_alive = False
            self.is_paused = True
            return True
        else:
            return False

    def restart(self):
        """
        This method is used to reset the parameters and restart the game.
        """

        for sprite in self.collision_sprites.sprites():
            if type(sprite) == Obstacle:
                sprite.kill()
        self.aeroplane.kill()
        self.aeroplane = Aeroplane([self.all_sprites])
        self.score = 0
        self.is_alive = True
        self.is_paused = False
        self.start_offset = pygame.time.get_ticks()

    def toggle_pause_and_play(self):
        """
        This method looks after pausing/playing the game.
        """

        self.is_paused = not self.is_paused

    def play(self):
        """
        This method is used to run the game.
        """

        while True:
            delta_time = self.clock.tick() * 1e-3
            for event in pygame.event.get():
                match event.type:
                    case pygame.MOUSEBUTTONDOWN:
                        if self.is_alive and not self.is_paused:
                            self.aeroplane.move_up()
                        elif not self.is_alive:
                            self.restart()
                    case pygame.KEYDOWN:
                        if pygame.key.get_pressed()[pygame.K_SPACE] and self.is_alive:
                            self.toggle_pause_and_play()
                    case self.obstacle_timer:
                        if self.is_alive:
                            Obstacle(
                                [self.all_sprites, self.collision_sprites],
                                scale_factor=randint(10, 15) * 1e-1,
                            )
                    case pygame.QUIT:
                        pygame.quit()
                        exit(0)
            if self.is_alive:
                self.check_collision()
            if not self.is_paused:
                self.music.set_volume(BG_MUSIC_VOLUME)
                self.all_sprites.update(delta_time)
                self.all_sprites.draw(self.display_surface)
                self.display_score()
                pygame.display.update()
            else:
                self.music.set_volume(0)


if __name__ == "__main__":
    game = Game()
    game.play()
