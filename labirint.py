from pygame import*
window = display.set_mode((1000,750))
b = (0,204,204)
display.set_caption('Моя игра')   
finish = False
run = True
y_speed = 0
win = transform.scale(image.load('thumb.jpg'),(1000,750))
class GameSprite(sprite.Sprite):
    def __init__(self,picture,w,h,x,y):
        super().__init__()
        self.image = transform.scale(image.load(picture),(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def __init__(self,picture,w,h,x,y,x_speed,y_speed):
        super().__init__(picture,w,h,x,y)
        self.x_speed = x_speed
        self.y_speed = y_speed
    def update(self):
        self.rect.x += self.x_speed
        platforms_touched = sprite.spritecollide(self,barriers,False)
        if self.x_speed > 0:
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left)
        elif self.x_speed < 0:
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right)
        self.rect.y += self.y_speed
        platforms_touched = sprite.spritecollide(self,barriers,False)
        if self.y_speed > 0:
            for p in platforms_touched:
                self.rect.bottom = min(self.rect.bottom, p.rect.top)
        elif self.y_speed < 0:
            for p in platforms_touched:
                self.rect.top = max(self.rect.top, p.rect.bottom)
    def fire(self):
        bullet = Bullet('weapon.png',50,45, self.rect.right,self.rect.centery,15)
        bullets.add(bullet)
class Enemy(GameSprite):
    side = 'left'
    def __init__(self,player_image,player_x,player_y,size_x,size_y,player_speed,a,win_width):
        GameSprite.__init__(self,player_image,player_x,player_y,size_x,size_y)
        self.speed = player_speed
        self.a = a 
        self.win_width = win_width
    def update(self): 
        if self.rect.x <= self.a: 
            self.side = 'right' 
        if self.rect.x >= self.win_width - 85:
            self.side = 'left'
        if self.side == 'left':
            self.rect.x -= self.speed
        else: 
            self.rect.x += self.speed
class Bullet(GameSprite):
    def __init__(self,picture,w,h,x,y,speed):
        super().__init__(picture,w,h,x,y) 
        self.speed = speed
    def update(self):
        self.rect.x += self.speed
        if self.rect.x > 1000:
            self.kill()
wall = GameSprite('platform_v.png',54,655,350,97)
wall2 = GameSprite('platform_h.png',260,50,100,270)
wall3 = GameSprite('platform_v.png',54,750,-55,3)
wall4 = GameSprite('platform_h.png',1000,50,1,750)
wall5 = GameSprite('platform_h.png',1000,50,1,-55)
wall6 = GameSprite('platform_v.png',54,1000,1000,3)
wall7 = GameSprite('platform_v.png',54,485,700,-5)
#строкой ниже левая верхняя стена
wall8 = GameSprite('platform_h.png',280,50,-4,80)
wall9 = GameSprite('platform_h.png',200,50,550,430)
wall10 = GameSprite('platform_v.png',54,170,700,580)
wall11 = GameSprite('platform_h.png',220,30,699,560)
wall12 = GameSprite('platform_v.png',45,490,890,100)
player = Player('hero.png',60,65,30,600,0,0)
player2 = Enemy('enemy.png',70,65,600,300,6,400,720)
player3 = Player('enemy2.png',100,85,820,620,0,0)
player4 = Enemy('enemy.png',70,65,600,100,9,400,720)
player5 = Enemy('enemy.png',70,65,600,200,12,400,720)
player6 = Enemy('enemy.png',70,65,100,400,7,0,375)
player7 = Enemy('enemy.png',70,65,100,200,8,0,375)
player8 = Enemy('enemy.png',70,65,600,500,10,400,720)
player9 = Enemy('enemy.png',70,65,100,500,11,0,375)
player10 = Enemy('enemy.png',70,65,700,40,10,740,1023)
#player11 = Enemy('enemy.png',70,65,700,180,7,740,915)
#player12 = Enemy('enemy.png',70,65,700,380,6,740,915)
#bullet = Bullet('weapon.png',50,45,100,20,15)
bullets = sprite.Group()
#bullets.add(bullet)
monsters = sprite.Group()
monsters.add(player2)
monsters.add(player4)
monsters.add(player5)
monsters.add(player6)
monsters.add(player7)
monsters.add(player8)
monsters.add(player9)
monsters.add(player10)
#monsters.add(player11)
#monsters.add(player12)   
barriers = sprite.Group()
barriers.add(wall)
barriers.add(wall2)
barriers.add(wall3)
barriers.add(wall4)
barriers.add(wall5)
barriers.add(wall6)
barriers.add(wall7)
barriers.add(wall8)
barriers.add(wall9)
barriers.add(wall10)
barriers.add(wall11)
barriers.add(wall12)
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        if e.type == KEYDOWN:
            if e.key == K_UP or e.key == K_w:
                player.y_speed = -13
            elif e.key == K_DOWN or e.key == K_s:
                player.y_speed = 13
            elif e.key == K_LEFT or e.key == K_a:
                player.x_speed = -13
            elif e.key == K_RIGHT or e.key == K_d:
                player.x_speed = 13
            elif e.key == K_SPACE:
                player.fire()
        elif e.type == KEYUP:
            player.y_speed = 0
            player.x_speed = 0
    if sprite.collide_rect(player,player3):
        finish = True
        win = transform.scale(image.load('thumb.jpg'),(1000,750))
    elif sprite.spritecollide(player,monsters,True):
        finish = True
        win = transform.scale(image.load('game-over_1.png'),(1000,750))
    if finish == False:
        sprite.groupcollide(bullets,barriers,True,False)
        sprite.groupcollide(bullets,monsters,True,True)
        window.fill((64,224,208))
        bullets.update()
        bullets.draw(window)
        player3.reset()
        monsters.update()
        monsters.draw(window)
        player.reset()
        player.update()
        barriers.draw(window)
    else:
        window.fill((255,255,255))
        window.blit(win,(0,0))
    time.delay(50)
    display.update()