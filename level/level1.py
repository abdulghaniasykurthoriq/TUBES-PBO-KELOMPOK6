import pygame
# from oop.enemies.scorpion import Scorpion
# from oop.level import Level
# from oop.levels.castle.castle1 import Castle
# from oop.enemies.mouse import Mouse


class Level1():
    ''' Level 1 - berlatar belakang rerumputan '''

    def setup(self):
        pass
        # self.castle = Castle(self.screen)
        # self.enemy = [Mouse, Scorpion]
        # self.sprites = self.get_sprites()

    def background_sound(self, volume=0.25):
        pygame.mixer.init()


    def tiles(self):
        # return self.sprites
        pass
      
    def get_sprites(self):
       return pygame.image.load('resources/img/grass.png')
        
