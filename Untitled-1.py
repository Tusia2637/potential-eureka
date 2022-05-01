from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self, image1, x, y, speed, width, height):
        self.image = transform.scale(image.load(image1),(width, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_right(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys[K_DOWN] and self.rect.y < 420:
            self.rect.y += self.speed

    def update_left(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys[K_s] and self.rect.y < 420:
            self.rect.y += self.speed

win = display.set_mode((600,500))
back = (123, 104, 238)
win.fill(back)

font.init()
font1 = font.Font(None, 35)
lose = font1.render('Game Over', 1, (139, 0, 139))

racket_right = Player('ggg.png', 520, 200, 8, 50, 150)
racket_left = Player('ggg.png', 20, 200, 8, 50, 150)
ball = GameSprite('ppp.png', 200, 200, 7, 50, 50)

speed_x = 5
speed_y = 5

game = True

while game:
    for i in event.get():
        if i.type == QUIT:
            game = False

    win.fill(back)
    racket_right.update_right()
    racket_left.update_left()

    ball.rect.x += speed_x
    ball.rect.y += speed_y

    if ball.rect.y < 0 or ball.rect.y > 450:
        speed_y *= -1

    if sprite.collide_rect(racket_right, ball) or sprite.collide_rect(racket_left, ball):
        speed_x *= -1

    if ball.rect.x < 0 or ball.rect.x > 500:
        game = False
        win.blit(lose, (200, 200))


    racket_right.reset()
    racket_left.reset()
    ball.reset()

    display.update()
    time.delay(50)
display.update()


