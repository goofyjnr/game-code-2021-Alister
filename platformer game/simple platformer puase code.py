#simple platformer puase code

#set up of our game


import pygame #Imports Pygame alowing us to make a game
from pygame.locals import *  #this gives the all the local varabials e.g. pygame.quit
import sys #imports the sys
import random #imports random alowing for randomnes to happen
from pygame.mixer import pause

pygame.init() #sets up the Pygame to be used for the game

vec = pygame.math.Vector2 #2 for two dimensional



HEIGHT = 450 #sets the size of the screen 
WIDTH = 400 #sets the size of the screen
ACC = 0.5  #sets the variable of  
FRIC = -0.12 #sets the Friction as a variable
FPS = 60 #sets the frames per second


#---------------------------------------------------------------#
#colour varbails
P1_Colour = (8,126,139)
P2_Colour = (231,90,124)
PT1_Colour = (251,176,45)
platform_colour = (30, 176, 35)
Background_colour = (39,39,39)

#--------------------------------------------------------------#


pause = False  #sets pause variable as false

FramePerSec = pygame.time.Clock() #sets up the clock

displaysurface = pygame.display.set_mode((WIDTH, HEIGHT)) #sets up the surface that the game is played on
pygame.display.set_caption("Platformer game :(") #sets up the name of the window the game is played on

#----------------------------------------------------------------------------------#
#class for player 1

class Player1(pygame.sprite.Sprite): #this is the over all class for all of the player 1 things this also sets up the sprite of the player
    def __init__(self):
        super().__init__() #this starts up the spite
        #self.image = pygame.image.load("character.png")  #Im not useing this 
        self.surf = pygame.Surface((30, 30))#tells where on the surface it is
        self.surf.fill((P1_Colour)) #changes the colour of the sptite
        self.rect = self.surf.get_rect() #makes it a rectangle

        self.pos = vec((390, 360)) #X and Y cords of the player at the start 
        self.vel = vec(0,0) #sets the velsoity of the player moving
        self.acc = vec(0.5,0) #sets the acceleration
        self.jumping = False #sets up the jumping
        self.score = 0       #Sets the score of zero at the start of the game
        self.restart()

    def move(self):
        self.acc = vec(0,0.5) #sets how fast the player can move

        pressed_keys = pygame.key.get_pressed() #this checks if the keys are presed to move
            
        if pressed_keys[K_LEFT]: #this means if the left button is clicked it will do the code
            self.acc.x = -ACC
        if pressed_keys[K_RIGHT]: #This means if the Right button is cliked it will do the 
            self.acc.x = ACC
                
        self.acc.x += self.vel.x * FRIC 
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH
            
        self.rect.midbottom = self.pos

    def jump(self): #sets up what a jump is
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits and not self.jumping:
            self.jumping = True 
            self.vel.y = -18

    def cancel_jump(self): #sets up  cancel jump 
        if self.jumping:
            if self.vel.y < -3:
                self.vel.y = -3

    def update(self): #sets up points system for player one
        hits = pygame.sprite.spritecollide(self ,platforms, False) #sets up what a collision is
        if self.vel.y > 0:        
            if hits:
                if self.pos.y < hits[0].rect.bottom:
                    if hits[0].point == True:   ##
                        hits[0].point = False   ##
                        self.score += 1         ##                
                    self.pos.y = hits[0].rect.top +1
                    self.vel.y = 0
                    self.jumping = False
    def restart(self):
        self.pos = vec((390, 360))       #spawn position on a x,y axis
        self.vel = vec(0,0)             #velocity on a x,y axis
        self.acc = vec(0,0)             #acceleration
        self.jumping = False            #sets jumping as false
        self.score = 0                  #sets the score to zero to start with



#----------------------------------------------------------------------------------------------------------#

#class for player 2

class Player2(pygame.sprite.Sprite): #this is the over all class for all of the player 2 things this also sets up the sprite of the player
    def __init__(self):
        super().__init__() #this starts up the spite
        #self.image = pygame.image.load("character.png")  #Im not useing this at the moment but i might
        self.surf = pygame.Surface((30, 30))#tells where on the surface it is
        self.surf.fill((P2_Colour)) #changes the colour of the sptite
        self.rect = self.surf.get_rect() #makes it a rectangle
        self.pos = vec((10, 360)) #X and Y cords of the player at the start 
        self.vel = vec(0,0) #sets the velsoity of the player moving
        self.acc = vec(0.5,0) #sets the acceleration
        self.jumping = False #sets up the jumping
        self.score = 0       #Sets the score of zero at the start of the game
        self.restart()

    def move(self):
        self.acc = vec(0,0.5)
        pressed_keys = pygame.key.get_pressed() #this checks if the keys are presed to move
            
        if pressed_keys[K_a]: #this means if the left button is clicked it will do the code
            self.acc.x = -ACC
        if pressed_keys[K_d]: #This means if the Right button is cliked it will do the 
            self.acc.x = ACC
                
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH
            
        self.rect.midbottom = self.pos

    def jump(self): 
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits and not self.jumping:
            self.jumping = True 
            self.vel.y = -18

    def cancel_jump(self):
        if self.jumping:
            if self.vel.y < -3:
                self.vel.y = -3

    def update(self): #sets up points system for player two
        hits = pygame.sprite.spritecollide(self ,platforms, False) #sets up what a collision is
        if self.vel.y > 0:        
            if hits:
                if self.pos.y < hits[0].rect.bottom:
                    if hits[0].point == True:   
                        hits[0].point = False   
                        self.score += 1                        
                    self.pos.y = hits[0].rect.top +1
                    self.vel.y = 0
                    self.jumping = False
    def restart(self):
        self.pos = vec((10, 360))  #spawn position on a axis
        self.vel = vec(0,0)  #velocity 
        self.acc = vec(0,0) #acceleration
        self.jumping = False  #sets jumping as false
        self.score = 0  #sets the score to zero to start with
                    
#-------------------------------------------------------------------------------#

#class for the platforms

class platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((random.randint(50,100), 12))
        self.surf.fill((platform_colour)) #sets the colour of the main platform
        self.rect = self.surf.get_rect(center = (random.randint(0,WIDTH-10), random.randint(0, HEIGHT-30))) # sets how big the platforms can be
        self.point = True #alows platfoms to count for points
        self.speed = random.randint(-1, 3) #this sets the speed of the platforms to ramdom between -1 and 3
        self.moving = True #alows the platforms to move

    def move(self): #code for platform movment
        if self.moving == True:  
            self.rect.move_ip(self.speed,0)
            if self.speed > 0 and self.rect.left > WIDTH:
                self.rect.right = 0
            if self.speed < 0 and self.rect.right < 0:
                self.rect.left = WIDTH
    def restart(self):
        self.surf = pygame.Surface((WIDTH, 20))#size of the platform
        self.surf.fill((PT1_Colour))#bottom platform colour
        self.rect = self.surf.get_rect(center = (WIDTH/2, HEIGHT - 10))#platform location
        self.moving = False #stops platform from moving
        self.point = False
        
        all_sprites.add(PT1) #adds platform
        platforms.add(PT1)

def check(platform, groupies):
    if pygame.sprite.spritecollideany(platform,groupies):
        return True
    else:
        for entity in groupies:
            if entity == platform:
                continue
            if (abs(platform.rect.top - entity.rect.bottom) < 40) and (abs(platform.rect.bottom - entity.rect.top) < 40):
                return True
        C = False

def plat_gen(): #sets up the code for platform genration tell the game what it need to do
    while len(platforms) < 6:
        width = random.randrange(50,100)
        p  = platform()      
        C = True
        
        while C:
            p = platform()
            p.rect.center = (random.randrange(0, WIDTH - width),
                            random.randrange(-50, 0))
            C = check(p, platforms)
        platforms.add(p)
        all_sprites.add(p)

def button (msg, x, y, w, h, ic, ac, action=None): #makes button work -- inside button() it has message/text, x axis, y axis, width, height, background colour 1, backgound colour 2, and function
    mouse =pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(displaysurface, ac, (x,y,w,h)) #draws background rectangle -- has selected colour, location and size
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(displaysurface, ic, (x,y,w,h))#draws background rectangle -- has colour, location and size
    font = pygame.font.Font('Exo2-italic.ttf', 20)  #variable for font type and text size
    text = font.render(msg, True, (0,0,0)) #varible for text and text colour
    displaysurface.blit(text, (x, y))  #prints text and text location

def quitgame():  #quits game function
    pygame.quit()
    quit()

def unpaused(): #unpause game function
    global pause #changes pause variable across the whole code
    pause = False #changes pause variable to False

def paused(): #pause game function
    font = pygame.font.Font("Tourney-Italic.ttf", 70)  #font type and size
    text = font.render("Paused", True, (255,255,255))#text and font colour
    textlocation = text.get_rect(center=(WIDTH/2,HEIGHT/4))

    while pause:  #while True loop works when pause is changed to True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        displaysurface.fill((Background_colour)) #changes screen colour
        displaysurface.blit(text, (textlocation)) #print text and text location

        button("Continue", 75, 190, 100, 60, (14,229,57), (131,198,144), unpaused)#runs in this order -- text, background x axis location, background y axis location, width of background, height of background, background colour, background on hover colour, unpause function
        button("Quit", 225, 190, 100, 60, (200,3,3), (100,3,3), quitgame)#runs quitgame function

        pygame.display.update() #updates screen

#------------------------------------------------------------------------------------#
#sets up the varibles that are used in the games

#PT1 is the main platform that the player spawns on
    
PT1 = platform() #sets PT1 as a platform class 
PT1.point = False #stops the main platform from giving you points 
P1 = Player1() #sets player 1 as the player class
P2 = Player2() # sets up player 2 as the player 2 class

#-------------------------------------------------------------------------------#
#sets up the main platform that the players spawn on

PT1.surf = pygame.Surface((WIDTH, 20))
PT1.surf.fill((PT1_Colour)) #this sets the colour of the main platform
PT1.rect = PT1.surf.get_rect(center = (WIDTH/2, HEIGHT - 10))
PT1.moving = False #this stops the main bottom platfor form moving

#-----------------------------------------------------------------------------#
#sprites code

#sets up all of the sprites that are needed for the game
all_sprites = pygame.sprite.Group()
all_sprites.add(PT1)
all_sprites.add(P1)
all_sprites.add(P2)

platforms = pygame.sprite.Group()
platforms.add(PT1)

#------------------------------------------------------------------------------#
#Sets up platform genration

for x in range(random.randint(4,19)):
    C = True
    pl = platform()
    while C:
        pl = platform()
        C = check(pl, platforms)
    platforms.add(pl)
    all_sprites.add(pl)

#---------------------------------------------------------------------------------#
#restarting game function

def reset():                
    global playeralive1 #changes playeralive variable across the whole code
    global playeralive2         
    global pause
    playeralive1 = True #sets playeralive as true
    playeralive2 = True #sets playeralive as true

    P1.restart()  #resets player 1 location
    PT1.restart() #resets floor platform location so it it at the bottom of the screen
    P2.restart()  #resets player 2 location

    while playeralive1 or playeralive2:
        P1.update()
        P2.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()#quits game
                sys.exit()#ends program
            if event.type == pygame.KEYDOWN:#only works when the key is being held down
                if event.key == pygame.K_UP: #up arrow key pressed down
                    P1.jump() #runs jump function
                if event.key == pygame.K_w:
                    P2.jump()
                elif event.key == pygame.K_p:#p key is pressed down
                    pause = True
                    paused() #runs pause function
            if event.type == pygame.KEYUP: #stops working when the key isn't being held down
                if event.key == pygame.K_UP: #up arrow key is no longer pressed down
                    P1.cancel_jump()  #runs cancel jump function
                if event.key == pygame.K_w:#w arrow key is no longer pressed down
                    P2.cancel_jump()    
#-----------------------------------------------------------------#
#code that kills player
        if P1.rect.top <= HEIGHT / 3:
            P1.pos.y += abs(P1.vel.y)
            for plat in platforms:
                plat.rect.y += abs(P1.vel.y)
                if plat.rect.top >= HEIGHT:
                    plat.kill()

        if P1.rect.top > HEIGHT:
            for entity in all_sprites:
                playeralive1 = False

        if P2.rect.top <= HEIGHT / 3:
            P2.pos.y += abs(P2.vel.y)
            for plat in platforms:
                plat.rect.y += abs(P2.vel.y)
                if plat.rect.top >= HEIGHT:
                    plat.kill()

        if P2.rect.top > HEIGHT:
            for entity in all_sprites:
                playeralive2 = False

#------------------------------------------------------------------#
        plat_gen()          #platform generation

        displaysurface.fill((Background_colour))   #sets the background colour

        f = pygame.font.SysFont("Verdana", 20)                  #score font and size
        g  = f.render(str(P1.score), True, (8,126,139))        #score colour
        displaysurface.blit(g, (WIDTH/1.25, 10))                   #score location and prints score

        f = pygame.font.SysFont("Verdana", 20)     #sets the font and size
        j  = f.render(str(P2.score), True, (231,90,124))   #Sets up the points system that can go u
        displaysurface.blit(j, (WIDTH/5, 10))   #sets up the placement of the text
        
        for entity in all_sprites:
            displaysurface.blit(entity.surf, entity.rect)
            entity.move()

        pygame.display.update()
        FramePerSec.tick(FPS)
#------------------------------------------------------------------------------------------#
#game over screen function

def gameover():             
    font = pygame.font.Font("Tourney-Italic.ttf", 70)#font type and size
    text = font.render("Game over", True, (255,255,255))#text and font colour
    textlocation = text.get_rect(center=(WIDTH/2,HEIGHT/4))

    while not playeralive1 or playeralive2: #while True loop works when pause is changed to True
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        displaysurface.fill((Background_colour))  #changes screen colour
        displaysurface.blit(text, (textlocation))      #print text and text location
        

        button("Continue?", 75, 190, 100, 70, (50,255,25), (25,150,15), reset) #runs in this order -- text, background x axis location, background y axis location, width of background, height of background, background colour, background on hover colour, reset function
        button("Quit?", 225, 190, 100, 70, (255,0,0), (100,0,0), quitgame)  #same as above except runs quitgame function

        pygame.display.update()         #updates screen
#---------------------------------------------------------------------------------#
#game loop

while True:         #game loop
    playeralive1 = True
    playeralive2 = True
    
    while playeralive1 or playeralive2:
        P1.update()
        P2.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()       #quits game
                sys.exit()          #ends program
            if event.type == pygame.KEYDOWN:        #only works when the key is being held down
                if event.key == pygame.K_UP:        #up arrow key pressed down
                    P1.jump()               #runs jump function
                if event.key == pygame.K_w:
                    P2.jump()
                elif event.key == pygame.K_p:       #p key is pressed down
                    pause = True
                    paused()                #runs pause function
            if event.type == pygame.KEYUP:          #stops working when the key isn't being held down
                if event.key == pygame.K_UP:        #up arrow key is no longer pressed down
                    P1.cancel_jump()        #runs cancel jump function
                if event.key == pygame.K_w:        #up arrow key is no longer pressed down
                    P2.cancel_jump() 

        if P1.rect.top <= HEIGHT / 3:
            P1.pos.y += abs(P1.vel.y)
            for plat in platforms:
                plat.rect.y += abs(P1.vel.y)
                if plat.rect.top >= HEIGHT:
                    plat.kill()

        if P1.rect.top > HEIGHT:
            for entity in all_sprites:
                playeralive1 = False       

        if P2.rect.top <= HEIGHT / 3:
            P2.pos.y += abs(P1.vel.y)
            for plat in platforms:
                plat.rect.y += abs(P1.vel.y)
                if plat.rect.top >= HEIGHT:
                    plat.kill()

        if P2.rect.top > HEIGHT:
            for entity in all_sprites:
                playeralive2 = False


        plat_gen()          #platform generation

        displaysurface.fill((Background_colour))      

        f = pygame.font.SysFont("Verdana", 20)                  #score font and size
        g  = f.render(str(P1.score), True, (8,126,139))        #score colour
        displaysurface.blit(g, (WIDTH/1.25, 10))                   #score location and prints score

         #sets up the points system for player 2
        f = pygame.font.SysFont("Verdana", 20)     #sets the font and size
        j  = f.render(str(P2.score), True, (231,90,124))   #Sets up the points system that can go u
        displaysurface.blit(j, (WIDTH/5, 10))   #sets up the placement of the text
        
        for entity in all_sprites:
            displaysurface.blit(entity.surf, entity.rect)
            entity.move()

        pygame.display.update()     #updates screen
        FramePerSec.tick(FPS)
    
    gameover()#runs gameover function