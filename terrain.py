from pygame import Surface
from pygame.sprite import Sprite
from pygame.image import load
from pygame.math import Vector2 as Vec2D
from pygame.mask import from_surface
from settings import HEIGHT, TERRAIN_IMG_URL, TERRAIN_VELOCITY, ACCELERATION

"""
This module will contain the implementation details of the ground (terrain)
sprite.
"""


class Ground(Sprite):
    """
    Sprite Ground.
    """

    def __init__(self, group):
        super().__init__(group)
        self.image = load(TERRAIN_IMG_URL).convert_alpha()
        self.surf = Surface((self.image.get_width(), self.image.get_height()))
        self.rect = self.surf.get_rect(bottomleft=(0, HEIGHT - self.image.get_height()))
        self.pos = Vec2D(self.rect.topleft)

        # mask
        self.mask = from_surface(self.image)

    def update(self, dt):
        """
        This method updates the position of the ground (terrain).
        """

        self.pos.x -= TERRAIN_VELOCITY * dt + 0.5 * ACCELERATION * dt**2
        if self.rect.centerx <= 0:
            self.pos.x = 0
        self.rect.x = round(self.pos.x)
