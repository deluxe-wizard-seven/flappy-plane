from pygame import Surface
from pygame.sprite import Sprite
from pygame.math import Vector2 as Vec2D
from pygame.image import load
from pygame.transform import scale
from pygame.transform import rotozoom
from pygame.mask import from_surface
from pygame.mixer import Sound
from settings import (
    AEROPLANE_IMG_URLS,
    AEROPLANE_IMG_SCALE_FACTOR,
    ANIMATION_RATE,
    UP_STEP,
    GRAVITY,
    ROTO_ZOOM_FACTOR,
    AEROPLANE_INITIAL_POS,
    JUMP_MUSIC_URL,
    JUMP_MUSIC_VOLUME,
)

"""
This module will contain the implementation details of the aeroplane sprite.
"""


class Aeroplane(Sprite):
    """
    Sprite Aeroplane.
    """

    def __init__(self, group):
        super().__init__(group)
        self.frame_index = 0
        img = load(AEROPLANE_IMG_URLS[self.frame_index]).convert_alpha()
        self.image = scale(
            img,
            (
                img.get_width() * AEROPLANE_IMG_SCALE_FACTOR,
                img.get_height() * AEROPLANE_IMG_SCALE_FACTOR,
            ),
        )
        self.surf = Surface((img.get_width(), img.get_height()))
        self.surf.blit(img, (0, 0))
        self.direction = 0
        self.rect = self.surf.get_rect(midleft=AEROPLANE_INITIAL_POS)
        self.pos = Vec2D(self.rect.topleft)

        # mask
        self.mask = from_surface(self.image)

    def move_up(self):
        """
        This method will move the aeroplane in upwards direction, when the
        user clicks on the screen.
        """

        jump_music = Sound(JUMP_MUSIC_URL)
        jump_music.set_volume(JUMP_MUSIC_VOLUME)
        jump_music.play()
        self.direction = -UP_STEP

    def apply_gravity(self, dt):
        """
        This method will emulate the application of gravity on the aeroplane.
        """

        self.direction += GRAVITY * dt
        self.pos.y += self.direction * dt
        self.rect.y = self.pos.y

    def rotate(self):
        """
        This method is used to rotate the image of the aeroplane when it
        is moved up (by clicking) or down (by the appliction of gravity).
        """

        rotated_aeroplane = rotozoom(self.image, -self.direction * ROTO_ZOOM_FACTOR, 1)
        self.image = rotated_aeroplane

    def animate(self, dt):
        """
        This method will animate the aeroplane sprite.
        """

        self.frame_index += round(ANIMATION_RATE * dt)
        self.frame_index %= len(AEROPLANE_IMG_URLS)
        img = load(AEROPLANE_IMG_URLS[self.frame_index])
        self.image = scale(
            img,
            (
                img.get_width() * AEROPLANE_IMG_SCALE_FACTOR,
                img.get_height() * AEROPLANE_IMG_SCALE_FACTOR,
            ),
        )

    def update(self, dt):
        """
        This method updates the background.
        """

        self.apply_gravity(dt)
        self.animate(dt)
        self.rotate()
