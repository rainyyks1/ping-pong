from pygame import *
from random import randint
window = display.set_mode((700, 500))
display.set_caption('Пинг - понг')
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):       
      keys = key.get_pressed()
      if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
   
