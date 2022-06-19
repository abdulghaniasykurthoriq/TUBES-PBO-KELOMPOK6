import pygame, sys, time, random
from pygame.locals import *
import math
import sys


direction = "RIGHT"
change_to = "RIGHT"
snake_pos = [100, 50]
snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]

pygame.mixer.init()
eating = pygame.mixer.Sound('resources/audio/eatsong.wav')

size_x = 720
size_y = 480

class GameController:
    def __init__(self, player):
        self.player = player
        self.keys = {
            "top": False,
            "bottom": False,
            "left": False,
            "right": False,
            "shoot": False
        }

    def keyboard_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == K_w:
                    self.keys["top"] = True
                elif event.key == K_a:
                    self.keys["left"] = True
                elif event.key == K_s:
                    self.keys["bottom"] = True
                elif event.key == K_d:
                    self.keys["right"] = True
            if event.type == pygame.KEYUP:
                if event.key == K_w:
                    self.keys["top"] = False
                elif event.key == K_a:
                    self.keys["left"] = False
                elif event.key == K_s:
                    self.keys["bottom"] = False
                elif event.key == K_d:
                    self.keys["right"] = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.player.shoot()

        if self.keys["top"]:
            self.player.move_up()
        elif self.keys["bottom"]:
            self.player.move_down()
        if self.keys["left"]:
            self.player.move_left()
        elif self.keys["right"]:
            self.player.move_right()