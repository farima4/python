from pygame import *
from random import *
from pygame import mixer
from sys import exit
from dvd_path import path, audio_path

init()

width, height = 1320, 700

screen = display.set_mode((width, height))
display.set_caption('DVD screensaver :)')

clock = time.Clock()

colors = [path + 'blue.png', path + 'cyan.png',
          path + 'darkblue.png', path + 'green.png',
          path + 'lime.png', path + 'orange.png',
          path + 'pink.png', path + 'purple.png',
          path + 'red.png', path + 'yellow.png']

hit_audio = mixer.Sound(audio_path + 'hit.wav')
def hit():
    hit_audio.play()
    
class DVD(sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image.load(choice(colors)).convert_alpha()
        self.rect = self.image.get_rect(center = (width / 2, height / 2))
        self.x, self.y = self.rect.center[0], self.rect.center[1]
        self.ver = choice(('up', 'down'))
        self.hor = choice(('left', 'right'))
        
    def move(self):
        if self.hor =='left':
            self.x -= 3
        if self.hor =='right':
            self.x += 3
                 
        if self.ver =='up':
            self.y -= 3
        if self.ver =='down':
            self.y += 3
            
        self.rect.center = (self.x, self.y)
        
        # ~~~~~~~~~~ RESTRICTIONS
        
        if self.rect.top < 0:
            hit()
            self.image = image.load(choice(colors))
            self.ver = 'down'
        if self.rect.bottom > height:
            hit()
            self.image = image.load(choice(colors))
            self.ver = 'up'
            
        if self.rect.left < 0:
            hit()
            self.image = image.load(choice(colors))
            self.hor = 'right'
        if self.rect.right > width:
            hit()
            self.image = image.load(choice(colors))
            self.hor = 'left'
        
logo = DVD()    
dvdg = sprite.Group()
dvdg.add(logo)

bg = Surface((width, height))
bg.fill('black')
     
       
while True:
    for e in event.get():
        if e.type == QUIT:
            exit()
            
    screen.blit(bg, (0, 0))
            
    dvdg.draw(screen)
    logo.move()
        
    display.update()
    clock.tick(60)
            
        
        