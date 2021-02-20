import pygame
import random
import time
from random_word import RandomWords as rm

#these words will be used in the absence of an internet connection
words = ("computer","science","database","variable","community","python","programmer","brogrammer","machine","neuralnetworks","amzon","likewise","hangman","mathematics",)
#initializing variables for the actual game
rm = rm()
word = " "
while(" " in word or "-" in word):
    try:
        word = rm.get_random_word()
    except:
        word = random.choice(words)
        print("[ERROR]: No internet")
    
word = word.lower()
checker = word
print(word)

#creating the display with height and width and perrforming initialisation
pygame.init()
display_width = 900
display_height = 800
if len(word) > 10:
    display_width += (len(word) - 10)*50
display = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('HANGMAN')
clock = pygame.time.Clock()

gameOver = False

#intialize colours
black = (0,0,0)
white = (255,255,255)

#initialize imagesi
folder = "images/"
dead = pygame.image.load(folder + 'dead.png')
empty = pygame.image.load(folder + 'empty.png')
face = pygame.image.load(folder + 'faceOnly.png')
hands = pygame.image.load(folder + 'hands.png')
legs = pygame.image.load(folder + 'legsToo.png')
body = pygame.image.load(folder + 'body.png')
winner = pygame.image.load(folder + 'winner.png')
states = list((empty,face,body,hands,legs,dead))

#define the position for the image
x = display_height * 0.01
y = display_height * 0.000001

def displayImage(state):
    display.blit(state,(x,y))

#create the text stuff
font = pygame.font.Font('freesansbold.ttf',20)

i = 0
letters = list()
letterRects = list()
userWord = list()
positions = list()

wordPosX = 470
wordPosY = 350
def endScreen(state):
    intro = True
    if not state:
        dispText = "GOOD JOB"
    else:
        dispText = "GAME OVER"
        
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == 13:
                    intro = False
                
        display.fill(white)
        titleFont = pygame.font.Font('freesansbold.ttf',115)
        font = titleFont.render(dispText,True,black)
        fontRect = font.get_rect()
        fontRect.center = (display_width/2,display_height/2-50)
        display.blit(font,fontRect)
        titleFont = pygame.font.Font('freesansbold.ttf',30)
        font = titleFont.render("press ENTER to quit",True,black)
        fontRect = font.get_rect()
        fontRect.center = (display_width/2,display_height/2+50)
        display.blit(font,fontRect)
        pygame.display.update()
        clock.tick(60)
        
def startScreen():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == 13:
                    intro = False
                
        display.fill(white)
        titleFont = pygame.font.Font('freesansbold.ttf',115)
        font = titleFont.render("HANGMAN",True,black)
        fontRect = font.get_rect()
        fontRect.center = (display_width/2,display_height/2-50)
        display.blit(font,fontRect)
        titleFont = pygame.font.Font('freesansbold.ttf',30)
        font = titleFont.render("press ENTER to start playing",True,black)
        fontRect = font.get_rect()
        fontRect.center = (display_width/2,display_height/2+50)
        display.blit(font,fontRect)
        pygame.display.update()
        clock.tick(60)

startScreen()

while not gameOver:
    pygame.display.update()
    clock.tick(60)
    
    display.fill(white)
    
    try:
        r = 0
        for letter in letters:
            display.blit(letters[r],letterRects[r])
            r+=1
    except IndexError:
        pass
    except NameError:
        pass

    currentImage = states[i]
    displayImage(currentImage)

    # DPI stands for Dash Position Increment
    DPI = 0
    CPI = 0
    spaces = list()

    for r,letter in enumerate(word):
        #pygame.draw.line(display,black,(wordPosX + DPI,wordPosY),(wordPosX + 20 + DPI,wordPosY),1)
        pygame.draw.rect(display,black,(wordPosX + DPI,wordPosY,25,30),2)
        DPI += 40



    
    for event in pygame.event.get():
        #loop exit things
        if states[i] == dead:
            pygame.mixer.music.load("sounds/lose.mp3")
            pygame.mixer.music.play(0)
            time.sleep(0.7)
            gameOver = True


        if len(checker) <= 0:
            displayImage(winner)
            pygame.display.update()
            pygame.mixer.music.load("sounds/win.mp3")
            pygame.mixer.music.play(0)
            time.sleep(2)
            gameOver = True

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            enteredUnicode = event.unicode
            enteredChar = chr(event.key)
            if (event.key >= 65 and event.key <=90) or (event.key >= 97 and event.key<= 122):
                if enteredChar in word:
                    CPI = 0
                    pos = 0
                    for currentLetter in word:
                        if enteredChar == currentLetter:
                            text = font.render(enteredChar.upper(),True,black)
                            letters.append(text)
                            textRect = text.get_rect()
                            textRect.center = (wordPosX+12.5+CPI,wordPosY+17)
                            letterRects.append(textRect)
                            userWord.append(enteredChar)
                            positions.append(pos)

                            checker = checker.replace(currentLetter,"")
                        pos += 1
                        CPI += 40

                else:
                    i += 1

        

            
    


endScreen(len(checker))

pygame.quit()
quit()
