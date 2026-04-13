"""
Program Name: Alien Invasion Game (Custom Mechanics - Milestone 1)
Author: Abdullah Rashid
Purpose: Modify the original Alien Invasion game by changing ship movement,
         position, and bullet direction to create new gameplay mechanics.
Starter Code: Based on Alien Invasion starter repo
https://github.com/RedBeard41/alien_Invasion_starter.git
Date: April 2026
"""
import pygame
from pathlib import Path


class Ship:
    """A class to manage the player's ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load image using pathlib
        BASE_DIR = Path(__file__).resolve().parent
        image_path = BASE_DIR / "images" / "ship.bmp"
        self.image = pygame.image.load(image_path)

        self.rect = self.image.get_rect()

        # LEFT SIDE POSITION
        self.rect.midleft = self.screen_rect.midleft

        # Movement flags
        self.moving_up = False
        self.moving_down = False

        self.speed = 3

    def update(self):
        """Update the ship's position based on movement flags."""
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= self.speed

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.speed

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)