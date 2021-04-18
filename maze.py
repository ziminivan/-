#создай игру "Лабиринт"!
from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, image1, speed1, x, y):
        super().__init__()
        self.image = transform.scale(image.load(image1), (65, 65))
        self.speed = speed1
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 630:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 430:
            self.rect.y += self.speed

class Enemy(GameSprite):
    way = 'left'
    def update(self):
        if self.rect.x <= 470:
            self.way = 'right'
        if self.rect.x >= 610:
            self.way= 'left'
        if self.way == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, r, g, b, width, height, x, y):
        super().__init__()
        self.r = r
        self.g = g
        self.b = b
        self.width = width
        self.height = height
        self.image = Surface((self.width, self.height))
        self.image.fill((r, g, b))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#создай окно игры
window = display.set_mode((700, 500))
display.set_caption("Лабиринт")
background = transform.scale(image.load("background.jpg"), (700, 500))

#музыка 
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

musik_win = mixer.Sound('money.ogg')
musik_lose = mixer.Sound('kick.ogg')
#спрайты
player = Player('hero.png',10,0,0)
monster = Enemy('cyborg.png',2,450,400)
final = GameSprite('treasure.png', 0, 580, 420)

#стены
w1 = Wall(154, 205, 230, 100, 20, 450, 10)
w2 = Wall(154, 205, 230, 400, 20, 70, 10)
w3 = Wall(154, 205, 230, 400, 20, 70, 110)
w4 = Wall(154, 205, 230, 100, 20, 550, 10)
w5 = Wall(154, 205, 230, 20, 600, 650, 10)
w6 = Wall(154, 205, 230, 100, 20, 450, 110)
w7 = Wall(154, 205, 230, 20, 200, 540, 110)
w8 = Wall(154, 205, 230, 100, 20, 450, 10)
w9 = Wall(154, 205, 230, 100, 20, 450, 10)
w10 = Wall(154, 205, 230, 100, 20, 450, 10)





font.init()
font = font.Font(None, 100)
win = font.render('YOU WIN!', True, (255, 215, 0))
lose = font.render('YOU LOSE!', True, (180, 0, 0))


clock = time.Clock()
FPS = 60
game = True 
finish = False
while game:

    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background,(0, 0))
        monster.update()
        player.update()
        monster.reset()
        player.reset()
        final.reset()
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        w8.draw_wall()
        w9.draw_wall()
        w10.draw_wall()
        w2.draw_wall()
        w2.draw_wall()
        
        if sprite.collide_rect(player, final):
            finish = True
            window.blit(win, (150,150))
            musik_win.play()
        if sprite.collide_rect(player, monster) or sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2) or sprite.collide_rect(player, w3) or sprite.collide_rect(player, w4) or sprite.collide_rect(player, w5) or sprite.collide_rect(player, w6) or sprite.collide_rect(player, w7) or sprite.collide_rect(player, w7) or sprite.collide_rect(player, w8) or sprite.collide_rect(player, w9) or sprite.collide_rect(player, w10):
            finish = True
            window.blit(lose, (150,150))
            musik_win.play()
    display.update()   
    clock.tick(FPS)  