from pygame import *

window = display.set_mode((700, 500))
display.set_caption('Ping-pong')

font.init()

font1 = font.Font(None, 36)

lost = 0
clock = time.Clock()


FPS = 60
class Game_sprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(Game_sprite):
    def update1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= 10
        if keys_pressed[K_s] and self.rect.y < 432:
            self.rect.y += 10
    def update2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= 16
        if keys_pressed[K_DOWN] and self.rect.y < 432:
            self.rect.y += 16



game = True
finish = False
font = font.Font(None, 90)
win = font.render('You win!', True, (250, 215, 0))
lose = font.render('You lose', True, (250, 215, 0))
platform = Player('platform.png', 5, 240, 10, 65, 65)
platform2 = Player('platform.png', 630, 240, 10, 65, 65)

while game:

    for e in event.get():
        if e.type == QUIT:
            game = False

        if finish != True:
            window.fill((134, 56, 106))
            platform.reset()
            platform2.reset()
            platform.update1()
            platform2.update2()
            
           




    display.update()
    clock.tick(FPS)
