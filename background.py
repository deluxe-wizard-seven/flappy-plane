from pygame import Surface
from pygame.sprite import Sprite
from pygame.math import Vector2 as Vec2D
from pygame.image import load
from pygame.transform import scale
from settings import BG_IMG_URL, HEIGHT, BG_VELOCITY, ACCELERATION

"""
This module will contain the implementation details of the background sprite.
"""


class Background(Sprite):
    """
    Background Sprite.
    """

    def __init__(self, group):
        super().__init__(group)
        bg_img = load(BG_IMG_URL)
        scale_factor = HEIGHT / bg_img.get_height()
        self.image = scale(bg_img, (bg_img.get_width() * scale_factor, HEIGHT))
        self.surf = Surface((bg_img.get_width() * 2, bg_img.get_height()))
        self.surf.blit(bg_img, (0, 0))
        self.surf.blit(bg_img, (bg_img.get_width(), 0))
        self.rect = self.surf.get_rect(topleft=(0, 0))
        self.pos = Vec2D(self.rect.topleft)

    def update(self, dt):
        """
        This method updates the background.
        """

        self.pos.x -= BG_VELOCITY * dt + 0.5 * ACCELERATION * dt**2
        if self.rect.centerx <= 0:
            self.pos.x = 0
        self.rect.x = round(self.pos.x)
