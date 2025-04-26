from pygame import *
back = (200, 255, 255)
win_width = 700
win_height = 500

clock = time.Clock()
FPS = 60
speed = 5
game = True
finish = False
class GameSprite(sprite.Sprite):
    def __init__(self, player_speed, player_image, player_x, player_y, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player1(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys_passed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_passed[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys_passed = key.get_pressed()

        if keys_passed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_passed[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

window = display.set_mode((win_width, win_height))
window.fill(back)
display.set_caption('Ping-Pong game')
hero1 = Player1(5, 'racket.png', 10, 250, 50, 65)
hero2 = Player2(5, 'racket.png', 650, 250, 50, 65)
ball = Player1(5, 'tennis-ball.png', 350, 250, 50, 50)
speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
    if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
        speed_x *= 1
        speed_y *= 1
    if ball.rect.y > win_height-59 or ball.rect.y < 0:
        speed_y *= 1
    if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (200,200))
        game_over = True
    if ball.rect.x > win_width:
        finish = True
        window.blit(lose2, (200,200))
        game_over = True
    
racket1 = Player('racket.png', 30, 200, 4, 50, 150)
racket2 = Player('racket.png', 520, 200, 4, 50, 150)
ball = GameSprite('tennis-ball.png', 200, 200, 4, 50, 50)

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))
    racket1.reset()
    racket2.reset()
    hero1.update()
    hero1.reset()
    ball.update()
    ball.reset()
    hero2.update()
    hero2.reset()
    displat.update()
    clock.tick(FPS)   



        
        


