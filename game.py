import pygame
import math
import random
pygame.init()
SIZE = (width,height) = (1000,700)
screen = pygame.display.set_mode(SIZE)

#setting fonts
fontHello = pygame.font.SysFont("Times New Roman",45)  
font2 = pygame.font.SysFont("Times New Roman", 24)
font3 = pygame.font.SysFont("Helvetica", 70)

#setting colours
GREEN = (0,255,0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0,0,0)
LIGHTBLUE = (153,204,255)
PINK = (255, 204, 255)
MAGENTA = (255, 153, 255)
WHITE = (255, 255, 255)
GREY = (139, 140, 143)
DARKGREY = (107, 108, 112)
BROWN = (153, 102, 51)

backgroundPic = pygame.image.load("outdoors background.jpg") #upload a tennis logo image
trashPic1 = pygame.image.load("trash bag.png")
trashPic2 = pygame.image.load("can.png")
trashList = [trashPic1, trashPic2]

lives = 3
ballX = 500
ballY = 350
ballRadius = 50

ballSpeedX = 0
ballSpeedY = 0
ballSpeed = 1

choice1Rect = pygame.Rect(250, 220, 500, 75)
choice2Rect = pygame.Rect(250, 320, 500, 75)
choice3Rect = pygame.Rect(250, 420, 500, 75)

choiceList = [choice1Rect, choice2Rect,choice3Rect]

STATE_1 = 0
STATE_2 = 1
STATE_3 = 2
STATE_4 = 3

state = STATE_1


def drawMenu(screen, mx, my, button):
    global state, randomCard
    screen.fill(LIGHTBLUE)
    gameName = font3.render ("Garbage Collector", 1, BLACK)
    screen.blit (gameName, (270, 100))
           
    displayList = ["PLAY","INSTRUCTIONS", "QUIT"] #list of button titles that are displayed on the menu
    for i in range(len(choiceList)):
        rect = choiceList[i]
        pygame.draw.rect(screen, GREY, rect)
        mouse = pygame.mouse.get_pos()
           
        if 250 + 500 > mouse[0] > 250 and 220+75 > mouse[1] > 220:
            pygame.draw.rect (screen, DARKGREY, (250,220,500,75))
        elif 250+500 > mouse[0] > 250 and 320+75 > mouse[1] > 320:
            pygame.draw.rect (screen, DARKGREY, (250,320,500,75))
        elif 250+500 > mouse[0] > 250 and 420+75 > mouse[1] > 420:
            pygame.draw.rect (screen, DARKGREY, (250,420,500,75))
        else:
            for i in range(len(choiceList)):
                rect = choiceList[i]
                pygame.draw.rect(screen, GREY, rect)      
     
        addTitle = fontHello.render(displayList[0], 1, BLACK)
        screen.blit(addTitle,(445,230))
        deleteTitle = fontHello.render(displayList[1],1, BLACK)
        screen.blit(deleteTitle,(350,332))
        reportsTitle = fontHello.render(displayList[2],1, BLACK)
        screen.blit( reportsTitle, (445,430))
    
        #allows the states to change:
        if rect.collidepoint(mx, my) == True and button == 1:
            if i == 0:
                state = STATE_2
                randomCard = random.choice(trashList)
            elif i == 1:
                state = STATE_3
            elif i == 2:
                state = STATE_4
               
def drawPlatform():
    pygame.draw.rect(screen, BROWN, (0,550,300,20))
    pygame.draw.rect(screen, BROWN, (400,500,280,20))

trash_collectables = [pygame.Rect(100,460,100,200), pygame.Rect(150,200,100,200)]

def playGame():
    global ballX, ballY, y_change, ballLives, jumping, acc, randomCard
    screen.blit(backgroundPic, (0,0,1000,700))  
    screen.blit(randomCard, (450,50))
    pygame.draw.circle(screen, BLUE, (ballX, ballY), ballRadius)
    for collect in trash_collectables:
        screen.blit(trashPic1, collect)
    text = fontHello.render("Lives: " + str(lives) , 1, BLACK)
    screen.blit(text,(800,10))
    drawPlatform()
    if jumping == True:
        ballY -= acc
        acc -= 1
        if ballY >= height:
            jumping = False
            acc = 0  
    if ballX + ballRadius > width:
        ballX = 950
    elif ballX - ballRadius < 0:
        ballX = 50
    if ballY > height:
        ballY = height - ballRadius
    if ballY - ballRadius < 0:
        ballY = 0
   
    timer = fontHello.render("Timer: " + str("%i"%(seconds)) , 1, BLACK)
    screen.blit(timer,(540,10))
   
    platformRect1 = pygame.Rect (0,550,300,20)
    platformRect2 = pygame.Rect (400,500,280,20)
    platformList = [platformRect1, platformRect2]
    circleRect = pygame.Rect (ballX, ballY,70,30)
    plasticRect = pygame.Rect (100,460,100,100)
    plasticX = 100
    canRect = pygame.Rect (150,200,100,103)
    trashRect = [plasticRect, canRect]
   
    if circleRect.colliderect(platformRect1):
        ballY = 500
        y_change = 0
           
    for i in trash_collectables:
        if circleRect.colliderect(i):
            trash_collectables.remove(i)
   
running = True
myClock = pygame.time.Clock()
mx = my = 0
#making text boxes
textBox = pygame.Rect(600, 400, 140, 32)
textBox2 = pygame.Rect(700,500,140,32)

jumping = False
x_change = 0
y_change = 0
acc = 20
start_ticks=pygame.time.get_ticks() #starter tick
platformRect1 = pygame.Rect (0,550,300,20)
platformRect2 = pygame.Rect (400,500,280,20)
platformList = [platformRect1, platformRect2]
circleRect = pygame.Rect (ballX-40, ballY-40,70,30)
plasticRect = pygame.Rect (100,460,100,100)
plasticX = 100
canRect = pygame.Rect (150,200,100,103)
trashRect = [plasticRect, canRect]

while running:  #this is the game loop
    mx = my = 0
    button = 0
    seconds=(pygame.time.get_ticks()-start_ticks)/1000 #calculate how many seconds
    if seconds > 6: # if more than 10 seconds close the game
        randomCard = random.choice(trashList)
        start_ticks=pygame.time.get_ticks()
           
    #Check all the events that happen
    for evnt in pygame.event.get():
        if evnt.type == pygame.KEYDOWN:
            if evnt.key == pygame.K_LEFT:
                x_change = -5
            elif evnt.key == pygame.K_RIGHT:
                x_change = 5
                               
            if evnt.key == pygame.K_UP:
                if jumping == False:
                    jumping = True
                    acc = 20
        if evnt.type == pygame.KEYUP:
            if evnt.key == pygame.K_LEFT or evnt.key == pygame.K_RIGHT or evnt.key == pygame.K_DOWN:
                x_change = 0
                y_change = 0      
        elif evnt.type == pygame.MOUSEMOTION:
            mx, my = evnt.pos
            leftButton = evnt.buttons[1]
        elif evnt.type == pygame.MOUSEBUTTONDOWN:
            mx, my = evnt.pos
            button = evnt.button
        if evnt.type == pygame.MOUSEMOTION: #checks if the mouse moves
            mx, my = evnt.pos
            leftButton = evnt.buttons[1]
        if evnt.type == pygame.MOUSEBUTTONDOWN: #checks if the mouse is pressed down
            mx, my = evnt.pos
            button = evnt.button
        if button == 3: #if the right mouse key is pressed, takes you back to main menu
            state = STATE_1
        
        #if the user tries to close the window, then raise the "flag"
        if evnt.type == pygame.QUIT:
            running = False
   
    if state == STATE_1: #determines if state is the main menu
        drawMenu(screen, mx, my, button)
    elif state == STATE_2:#determines if state is the view page
        playGame()   
    elif state == STATE_3:
        pygame.draw.rect(screen, PINK, (0,0,width, height))
    elif state == STATE_4:
        running = False
                         
    ballX += x_change
    ballY += y_change    
    pygame.display.flip()

    # waits long enough to have 60 fps
    myClock.tick(60)
pygame.quit()  