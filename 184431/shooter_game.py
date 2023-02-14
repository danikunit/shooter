#Создай собственный Шутер!
import pygame
import random
screen = pygame.display.set_mode((1000,800))
pygame.init()
pygame.display.set_caption('Shooter')
background =pygame.image.load('galaxy.jpg')
isTrue = True
aliens = []
bullets = []
xp = 50
asteroids = []
timer_btw_spawn = pygame.USEREVENT + 1  
pygame.time.set_timer(timer_btw_spawn, 6000)
hp = 1
label_exemplar = pygame.font.SysFont('verdana', 20)
asteroid = pygame.image.load('asteroid.png')
class Sprites():
    def __init__(self, x, y, width, heigth, speed, sprite):
        self.image = pygame.transform.scale(pygame.image.load(sprite), (width, heigth))
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(topleft=(self.x,self.y))
        self.speed = speed
    def show_sprite(self):
        screen.blit(self.image, (self.x, self.y))
rocket = Sprites(450,600,100,150,2,'rocket.png')
def strike(bullet_img, bullet_x,bullet_y):
    bullets.append(bullet_img.get_rect(topleft=(bullet_x, bullet_y)))
def alien_spawn(image, x,y):
    aliens.append(pygame.image.load(image).get_rect(topleft=(x,y)))


while isTrue:
    label_hp = label_exemplar.render('Coins:' + str(hp), True, (255,255,255))
    label_xp = label_exemplar.render('Hp:' + str(xp), True, (255,255,255))
    keys = pygame.key.get_pressed()
    screen.blit(background,(0,0))
    rocket.show_sprite()
    if keys[pygame.K_a] and rocket.x > 0 or keys[pygame.K_LEFT]and rocket.x >0:
        rocket.x -= rocket.speed
    elif keys[pygame.K_d] and rocket.x < 800 or keys[pygame.K_RIGHT] and rocket.x < 800:
        rocket.x += rocket.speed
    elif keys[pygame.K_SPACE]:
        strike(pygame.image.load('bullet.png'), rocket.x + 50, rocket.y)
    for el in bullets:
        if el.y <= 0:
            blit = False
        else:
            blit = True
        if blit == True:
            screen.blit(pygame.transform.scale(pygame.image.load('bullet.png'), (20,20)),(el.x,el.y))
        if blit == True:
            for en in aliens:
                
                if en.colliderect(el):
                    aliens.remove(en)
                    bullets.remove(el)
                    hp = int(hp)
                    hp += 1
                    hp = str(hp)
        if el.y <= 0:
            el.y = rocket.y
            blit = False
            bullets.remove(el)
        el.y -= 5 
    for el in aliens:
        if el.y >= 800:
            blit = False
        else:
            blit = True
        if blit == True:
            screen.blit(pygame.transform.scale(pygame.image.load('ufo.png'), (100,100)), (el.x,el.y))
        if el.y >= 800:
            blit= False
            aliens.remove(el)
        if el.y == rocket.rect.y:
            aliens.remove(el)
            xp-=1
        el.y += 2
    for el in asteroids:
        if el.y >= 800:
            blit = False
        else:
            blit = True
        if blit == True:
            screen.blit(pygame.transform.scale(pygame.image.load('asteroid.png'), (100,100)), (el.x,el.y))
            el.y += 3
        if el.y >= rocket.rect.y:
            asteroids.remove(el)
            xp-=1
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            isTrue = False
            pygame.exit()
        if e.type == timer_btw_spawn:
            alien_spawn('ufo.png', (random.randint(0,1000)), 0)
            asteroids.append(asteroid.get_rect(topleft=(random.randint(0,900), -200)))
            
        
    screen.blit(label_hp,(0,0))
    screen.blit(label_xp,(0,50))

    pygame.display.update()
        
