from pygame import *

window = display.set_mode((700,500))
window.fill((212, 212, 212))

#шар
class GameSprite(sprite.Sprite):
    def __init__(self, color, image_name, speed, x, y, w, h):
        super().__init__()
        self.color = color
        self.speed = speed
        self.image = transform.scale(image.load(image_name),(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#блоки
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 500:
            self.rect.y += self.speed
    def update2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 500:
            self.rect.y += self.speed
       
voron = Player(None, 'voron.png', 10, 10, 200, 130, 130)
voron2 = Player(None, 'voron2.png', 10, 570, 200, 130, 130)
apple = GameSprite(None, 'apple.png' , 10, 320, 200, 60, 60)

clock = time.Clock()
game = True

speed_x=3
speed_y=3

while game:
    window.fill((212, 212, 212))
    voron.update()
    voron2.update2()
    voron.reset()
    voron2.reset()
    apple.reset()
    # if finish != True:
    apple.rect.x += speed_x
    apple.rect.y += speed_y
    if apple.rect.y > 500 - 50 or apple.rect.y < 0:
        speed_y *= -1
    if sprite.collide_rect(voron, apple) or sprite.collide_rect(voron2, apple):
        speed_x *= -1
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()    
    clock.tick(40)
