from pygame import *
font.init()
#from random import randint

window = display.set_mode((900, 450))
display.set_caption("Пинг Понг")
background = transform.scale(image.load("field.png"), (900, 450))


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, hight):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, hight))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed
    def updateL(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 400:
            self.rect.y += self.speed

racket1 = Player("platformA.png", 20, 20, 5, 10, 70)
racket2 = Player("platformB.png", 880, 20, 5, 10, 70)
ball = GameSprite("ball.png", 400, 100, 50, 50, 50)
finish = False
game = True
speed_x = 3
speed_y = 3
while game:
    
    

    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background, (0, 0))
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
        if ball.rect.y > 400:
            speed_y *= -1
        if ball.rect.y < 0:
            speed_y *= -1
        


        racket1.updateL()
        racket1.reset()
        racket2.update()
        racket2.reset()
        ball.update()
        ball.reset()

    display.update()
    time.delay(10)
