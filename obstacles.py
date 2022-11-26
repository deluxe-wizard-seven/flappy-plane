from pygame.sprite import Sprite
from pygame.math import Vector2 as Vec2D
from pygame.image import load
from pygame.transform import scale, flip
from pygame.mask import from_surface
from random import randint
from settings import (
    WIDTH,
    HEIGHT,
    OBSTACLE_IMG_URLS,
    OBSTACLE_DIST_LIMITS,
    OBSTACLE_HEIGHT_LIMITS,
    OBSTACLE_VELOCITY,
    SIGHT_LIMIT,
    ACCELERATION,
)

"""
This module will contain the implementation details of the obstacle sprites.
"""


class Obstacle(Sprite):
    """
    Obstacle Sprite.
    """

    def __init__(self, groups, scale_factor):
        super().__init__(groups)
        choice = randint(0, 1)
        self.image = load(OBSTACLE_IMG_URLS[choice]).convert_alpha()
        self.image = scale(self.image, Vec2D(self.image.get_size()) * scale_factor)
        x = WIDTH + randint(*OBSTACLE_DIST_LIMITS)
        horizontal_flip = randint(0, 1) == 0
        self.image = flip(self.image, horizontal_flip, choice)
        if choice:
            y = randint(-OBSTACLE_HEIGHT_LIMITS[1], -OBSTACLE_HEIGHT_LIMITS[0])
            self.rect = self.image.get_rect(midtop=(x, y))
        else:
            y = HEIGHT + randint(*OBSTACLE_HEIGHT_LIMITS)
            self.rect = self.image.get_rect(midbottom=(x, y))
        self.pos = Vec2D(self.rect.topleft)

        # mask
        self.mask = from_surface(self.image)

    def out_of_sight(self) -> bool:
        """
        This method checks whether the obstacle is still visible in the
        screen or not.
        """

        return self.rect.right <= SIGHT_LIMIT

    def update(self, dt):
        """
        This method updates the background.
        """

        self.pos.x -= OBSTACLE_VELOCITY * dt + 0.5 * ACCELERATION * dt**2
        self.rect.x = round(self.pos.x)

        if self.out_of_sight():
            self.kill()
