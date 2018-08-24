import pygame
import math
import random
import sys

img = pygame.image.load('agarback.png')#import the background image

background = pygame.image.load('agarback.png')
#for i in range(0,10):
 #   background[i] = screen[i]
  #  print (screen)
#playerpos = 3
#screen[playerpos] = 8
 #   print (screen)
    
class Controller(object):#Base controller class for ai and player
    def __init__(self, colour, speed = 1, mass = 1, position = (0,0), touching = [], splitTime = 0.0):
        self.colour = colour
        self.speed = speed
        self.mass = mass
        self.position = position
        self.touching = touching
        self.splitTime = splitTime
    
class GameController(object):#Controls the total mass in the game
    def __init__(self, totalMass = 0):
        self.totalMass = totalMass

class Player(Controller):#player inherits from the base controller class which created the variables
    def __init__(self,playerColour, playerSpeed = 1, playerMass = 1, touching = [], splitTime = 0.0, playerPosition = (0,0), playerPositionX = 0, playerPositionY = 0):
        self.playerSpeed = playerSpeed#initialize all variables
        self.playerMass = playerMass
        self.touching = touching
        self.playerColour = playerColour
        self.splitTime = splitTime
        self.playerPosition = playerPosition
        self.playerPositionX = playerPositionX
        self.playerPositionY = playerPositionY
    def split(self):#split function to split the player when called
        #Clone current shape using mass
        if self.mass > 25:
            print()
    def eaten(self, playerMass, aiMass):#eat function run when collision is detected with the ai. inherits playerMass, as well as the aiMass to compare the two
        global eatResult
        if playerMass < aiMass:#If the player's mass+1 is greater than the players
            eatResult = 'playerEat'
        if playerMass > aiMass:
            eatResult = 'aiEat'        

        return eatResult#return the result
            
#Enemy(AI) Class
class ai(Controller):
    def __init__(self, aiColour=(0,0,0), aiSpeed = 0, aiMass = 0, aiTouching = [], aiSplitTime = 0.0, aiPosition = (0,0), aiPositionX = 0, aiPositionY = 0):
        self.aiColour = aiColour
        self.aiSpeed = aiSpeed
        self.aiMass = aiMass
        self.aiTouching = aiTouching
        self.aiSplitTime = aiSplitTime
        self.aiPosition = aiPosition
        self.aiPositionX = aiPositionX
        self.aiPositionY = aiPositionY
    
    
    def aiMovement(self, playerMass,foodEaten):
        if self.aiMass > 10+playerMass:# 10 + playermass to allow ai to eat some food..
            aiPosition = []
            aiPosition.append(self.aiPositionX)
            aiPosition.append(self.aiPositionY) 
            '''
            if self.aiPositionX < width+180:
                self.aiPositionX += self.aiSpeed
            if self.aiPositionX > width+180:
                self.aiPositionX -= self.aiSpeed   
            if self.aiPositionY < height-220:
                self.aiPositionY += self.aiSpeed
            if self.aiPositionY > height:
                self.aiPositionY -= self.aiSpeed
            '''
            if self.aiPositionX > playerObject.playerPositionX:
                self.aiPositionX -= self.aiSpeed
            if self.aiPositionX < playerObject.playerPositionX:
                self.aiPositionX += self.aiSpeed
            if self.aiPositionY-200 > playerObject.playerPositionY:
                self.aiPositionY -= self.aiSpeed
            if self.aiPositionY-200 < playerObject.playerPositionY:
                self.aiPositionY += self.aiSpeed
                
        else:
            if foodTickCount > 3000:
                closestFoodX = foodList[0].posX
                closestFoodY = foodList[0].posY
                if self.aiPositionX < closestFoodX:
                    self.aiPositionX += self.aiSpeed
                if self.aiPositionX > closestFoodX:
                    self.aiPositionX -= self.aiSpeed
                if self.aiPositionY < closestFoodY:
                    self.aiPositionY += self.aiSpeed
                if self.aiPositionY > closestFoodY:
                    self.aiPositionY -= self.aiSpeed   


''' ----Pseudocode----
def aiDesisions(self, playerMass)
    if aiMass > playerMass:
        move towards player
    if aiMass < playerMass:
        move towards closest food pellet
        if distanceBetweenPlayer <= x:
            move away from player
    
'''      
#Define colours in RGB
RED = (255,0,0)
YELLOW = (255,200,51)
WHITE = (250,255,255)
GREEN = (0, 255, 0)
BLUE = (0,0, 255)
ORANGE = (255,102,0)
colours = [RED,YELLOW,GREEN,BLUE]

#Food Class
gameFoodRect = []
class Food(object):
#self, size, color, mass (Total mass of game)
    def __init__(self, size, color, posX, posY, foodRect):
        self.size = size
        self.color = color
        self.posX = posX
        self.posY = posY
        self.foodRect = foodRect
    def spawnFood(self, size, color, posX, posY):
        global foodRect1
        pygame.draw.circle(screen, color, (posX,posY), 6, 0)#draw the food
        foodRect1 = pygame.draw.rect(screen, color, (posX-1, posY-1, 3,3))#draw the hidden rect
        
        return foodRect1



#Game Code
height = 800
width = 600

#Initialize pygame
pygame.init()
gameClock = pygame.time.Clock()

screen = pygame.display.set_mode((800,600), 0, 32)
currentScene = 'menu'

#Create Player and Ai Objects
playerObject = Player(YELLOW, 3, 10, touching = [], splitTime = 0.0, playerPosition = (50,50), playerPositionX = 50, playerPositionY = 50)#create player object
drawPlayer = pygame.draw.circle(screen, YELLOW, (60, 250), playerObject.playerMass)#set the drawn circle to drawPlayer
drawHiddenPlayer = pygame.draw.rect(screen, YELLOW, (0,0,100,50))#set the "hidden" rectangle to player

mainControlObject = GameController(1)#Creat the maincontroller object

aiObject = ai(YELLOW, 3, 10, aiTouching = [], aiSplitTime = 0.0, aiPosition = (100,350), aiPositionX = 100, aiPositionY = 350)#create the ai object
drawAi = pygame.draw.circle(screen, YELLOW, (100, 350), aiObject.aiMass)#set the drawn ai circle to drawai
drawHiddenAi = pygame.draw.rect(screen, YELLOW, (0,0,100,50)) #set the "hidden" rectangle to hiddenai  

sizes = [[], [], [], [], [], [], [], [], [], [], [5,194], [5,194], [4,194],
[2,192], [2,192], [2,192], [2,192],[2,190],[1,190],[-2,190],[-2,190],
[-3,188],[-3,188],[-3,188],[-4,186],[-4,186],[-6,186],[-6,184],[-6,184],
[-6,183],[-7,183],[-8,180],[-9,182],[-9,182],[-11,179],[-11,179],[-11,179],
[-11,179],[-13,177],[-13,177],[-13,175],[-13,175],[-13,175],[-13,173],[-13,173],
[-15,170],[-17,170],[-18,170],[-17,170],[-18,170],[-18,170],[-18,170],[-18,170],[-19,167],
[-20,164],[-21,164],[-22,162],[-23,160],[-24,160],[-25,160],[-26,158],[-27,157],[-28,157],
[-29,157],[-30,155],[-31,154],[-32,153],[-33,153],[-34,153],[-35,153],[-36,150],[-37,150],
[-38,150],[-39,150],[-39,150],[-39,150],[-39,150],[-39,150],[-35,150],[-35,150],[-35,150],
[-35,150],[-35,150],[-35,150],[-35,150],[-35,150],[-35,150],[-35,150],[-35,150],[-35,150],
[-35,150],[-35,150],[-35,150],[-35,150],[-35,150],[-35,150],[-35,150],[-35,150],[-35,150],
[-35,150],[-35,150],[-35,150],[-35,150],[-35,150],[-35,150],[-35,150],[-35,150],[-30,150],
[-30,150],[-30,150],[-30,150],[-30,150],[-40,150],[-40,150],[-40,150],[-40,150],[-40,150],
[-60,130],[-60,130],[-60,130],[-60,130],[-60,130],[-60,130]]#store positions for collider detection
                                                #10         #11   #12         #13   #14       #15      #16         #17  #18      #19   #20         #21   #22       #23     #24         #25     #26    #27       #28     #29         #30      #31   #32       #33     #34         #35     #36         #37       #38     #39         #40
#The sizes dictionary is used to store the correct positions to be used when drawing the hidden player rectangle for collision detection
#Check for collisons using shapename.colliderect(objectname)
#call update function in player


#Defining movement variables
playerLeft = False
playerRight = False
playerUp = False
playerDown = False
doSplit = False

#defining fonts
font = pygame.font.SysFont("Comic Sans", 30)
smallFont = pygame.font.SysFont("Comic Sans", 20)
tinyFont = pygame.font.SysFont("Comic Sans", 20)

#define tickcount to count seconds in the game
tickCount = 0
foodTickCount = 0

#define lists for use with food
foodList = []
hitList = []

#define the eat result when touching the ai
eatResult = False
foodEaten = 0

#while the game is running
while True:
    screen.fill(WHITE)#set background to white
    for event in pygame.event.get():#for events in the pygame window
        if event.type == pygame.QUIT:#Close pygame on quit
            pygame.quit()
            sys.exit()

    if currentScene == 'menu':#if the scene is menu, display the menu screen
        screen.blit(img,(0,0))#add the graph background
        label = font.render("Welcome to Agar.io", 1, (RED))#define a label
        screen.blit(label,(300,200))#display the defined label
        label2 = smallFont.render("Change your cell's direction with the arrow keys", 1, (0,0,0))
        screen.blit(label2,(240,220))
        label2 = smallFont.render("Eat cells that are smaller than you", 1, (0,0,0))
        screen.blit(label2,(280,240))
        label2 = smallFont.render("Press space while moving to split", 1, (0,0,0))
        screen.blit(label2,(280,260))
        label2 = smallFont.render("Avoid cells bigger than you!", 1, (0,0,0))
        screen.blit(label2,(295,280))
        label = font.render("Press SPACE to start!", 1, (RED))
        screen.blit(label,(280,310))
        pygame.display.update()#update the screen to display new items
        if event.type == pygame.KEYDOWN:#if there is a key down
            if event.key == pygame.K_SPACE:#if the key pressed is space
                currentScene = 'game'#change the scene to game

    if currentScene == 'deadMenu':
        screen.blit(img,(0,0))
        label = font.render("You died!", 1, (RED))
        screen.blit(label,(300,200))
        label2 = smallFont.render("Press SPACE to play again!", 1, (RED))
        screen.blit(label2,(240,220))
        playerObject.playerMass = 10
        playerObject.playerSpeed = 3
        aiObject.aiSpeed = 3
        aiObject.aiMass = 11
        tempPosX = random.randint(100,500)
        tempPosY = random.randint(100,500)
        aiObject.aiPositionX = tempPosX
        aiObject.aiPositionY = tempPosY
        aiObject.aiPosition = (tempPosX,tempPosY)
        pygame.display.update()#update the screen to display new items
        if event.type == pygame.KEYDOWN:#if there is a key down
            if event.key == pygame.K_SPACE:#if the key pressed is space
                currentScene = 'game'#change the scene to game

    if currentScene == 'game':#if the scene is the game scene
        screen.blit(img,(0,0))#add the graph background
        if event.type == pygame.KEYDOWN:#Check for keypresses
            if event.key == pygame.K_RIGHT:#if right arrow key is pressed
                playerLeft = False#set player movement variables to true or false depending on keys hit
                playerRight = True
            if event.key == pygame.K_LEFT:
                playerLeft = True
                playerRight = False
            if event.key == pygame.K_UP:
                playerUp = True
                playerDown = False
            if event.key == pygame.K_DOWN:
                playerUp = False
                playerDown = True
            if event.key == pygame.K_SPACE:
                doSplit = True
                print(playerObject.playerMass)
        if event.type == pygame.KEYUP:#set movement variables to false if key is not pressed
            if event.key == pygame.K_RIGHT:
                playerRight = False
            if event.key == pygame.K_LEFT:
                playerLeft = False
            if event.key == pygame.K_UP:
                playerUp = False
            if event.key == pygame.K_DOWN:
                playerDown = False
    
        #Ai Movement function:
        aiObject.aiMovement(playerObject.playerMass, foodEaten)#move the ai
    
        #aiObject.aiPosition = drawAi.center
        drawAi = pygame.draw.circle(screen, BLUE, (aiObject.aiPositionX, aiObject.aiPositionY), aiObject.aiMass)#draw the ai
        drawHiddenAi = pygame.draw.rect(screen, BLUE, (aiObject.aiPositionX+sizes[aiObject.aiMass][0]-9,aiObject.aiPositionY+sizes[aiObject.aiMass][1]-200,aiObject.aiMass+2,aiObject.aiMass+2))
        #^ draw the hidden rectangle for the ai. Hidden rectangles are used to detect collision and pygame's collision detection works with rectangles not circles

        #Player move code here
        playerObject.playerPosition = drawPlayer.center#set the player object's position to the actual drawn object's position
        drawPlayer = pygame.draw.circle(screen, YELLOW, playerObject.playerPosition, playerObject.playerMass)#draw the player's circle
        drawHiddenPlayer = pygame.draw.rect(screen, YELLOW, (playerObject.playerPositionX+sizes[playerObject.playerMass][0],playerObject.playerPositionY+sizes[playerObject.playerMass][1],playerObject.playerMass*1.3,playerObject.playerMass*1.3))
        #^ draw the hidden rectangle for the player
        massLabel = tinyFont.render(str(playerObject.playerMass), 1, GREEN)#draw the player's mass in their circle
        screen.blit(massLabel, (playerObject.playerPosition))#display the player's mass label

        aiObject.aiPosition = drawAi.center
        aiMassLabel = tinyFont.render(str(aiObject.aiMass), 1, RED)
        screen.blit(aiMassLabel, (aiObject.aiPosition))



        
        direction = ''
        if playerDown is True and drawPlayer.bottom < height-200:#If player is moving down and they are not at the bottom
            drawPlayer.top += playerObject.playerSpeed#add to the player's Y coordinate to move the player down
            playerObject.playerPositionY += playerObject.playerSpeed
            direction = 'down'#set the direction the player is moving in to determine where to split towards
        if playerUp is True and drawPlayer.top > 0:
            drawPlayer.top -= playerObject.playerSpeed
            playerObject.playerPositionY -= playerObject.playerSpeed
            direction = 'up'
        if playerLeft is True and drawPlayer.left > 0:
            drawPlayer.left -= playerObject.playerSpeed
            playerObject.playerPositionX -= playerObject.playerSpeed
            direction = 'left'
        if playerRight is True and drawPlayer.right < width+200:
            drawPlayer.right += playerObject.playerSpeed
            playerObject.playerPositionX += playerObject.playerSpeed
            direction = 'right'
            #print('AI:', aiObject.aiPositionX)
            #print('Player:', playerObject.playerPositionX)
            
        #radius + radius = size + size
        #
        #add 200 to playerPositionY when comparing
        #
        #dist = math.hypot(aiObject.aiPositionX-playerObject.playerPositionX,aiObject.aiPositionY-playerObject.playerPositionY+200)#use pythagorean theorem to find distance between circles find
        #^instead of using pyhagorean theorem to find the distances, I drew hidden rectangles inside each circle to use pygame's built in rectangle collision detection
        
        #Spawn the food
        if mainControlObject.totalMass < 100:#if there is less mass in the game than 100
            foodRect1 = ''
            mainControlObject.totalMass += 1#add 1 to the game's mass
            foodList.append(Food(5, random.choice(colours), random.randint(10,725),random.randint(10,580), 'hi'))#append a food object to the foodList
        hitList = []#clear the hitList
        for stuff in foodList:#for the objects in the foodList
            stuff.spawnFood(stuff.size, stuff.color, stuff.posX, stuff.posY)#draw the food
            hitList.append(foodRect1)#append to the hitList based on the amount of food drawn. this is done to determine the index each foodObject is located at
            
        for foodStuff in hitList:#food hit detection
            foodIndex = hitList.index(foodStuff)#set the food index to the index of the hitlist item currently being looked at
            if drawHiddenPlayer.colliderect(foodStuff):#if the player is touching the food
                print('Food Touched')
                del foodList[foodIndex]#delete the food object from the foodlist
                playerObject.playerMass += 1#add 1 to the player's mass
            if drawHiddenAi.colliderect(foodStuff):#if the ai is touching the food, do the same thing for the ai
                print('AI Food Touched')
                del foodList[foodIndex]
                foodEaten += 1
                aiObject.aiMass += 1
                
        #ai and player collision detection
        if drawHiddenPlayer.colliderect(drawHiddenAi):#if the player's detection rect is touching the ai's collision rect
            playerObject.eaten(playerObject.playerMass, aiObject.aiMass)#run the playerObject's function named eaten
            if eatResult == 'aiEat':#determine action based onthe result of the eaten function
                print('dead')
                playerObject.playerMass += aiObject.aiMass
                aiObject.aiMass = 10
                xTemp = random.randint(100,500)
                yTemp = random.randint(100,500)
                aiObject.aiPosition = (xTemp,yTemp)
                aiObject.aiPositionX = xTemp
                aiObject.aiPositionY = yTemp
                eatResult = ''
            elif eatResult == 'playerEat':
                print('Player Dead')
                currentScene = 'deadMenu'
                eatResult = ''
                
        #lose mass overtime
        if tickCount >= 5000:#after 5 seconds
            print('mass lost')
            if playerObject.playerMass > 30 and playerObject.playerMass < 35:#if the player has more than 30 mass
                mainControlObject.totalMass -= 1#lose 2 mass
                playerObject.playerMass -=1
            if playerObject.playerMass > 35 and playerObject.playerMass < 45:
                mainControlObject.totalMass -= 2
                playerObject.playerMass -=2
            if playerObject.playerMass > 40 and playerObject.playerMass < 60:
                mainControlObject.totalMass -= 3
                playerObject.playerMass -=3
            if playerObject.playerMass > 60 and playerObject.playerMass < 80:
                mainControlObject.totalMass -= 4
                playerObject.playerMass -=4
            if playerObject.playerMass > 80:
                mainControlObject.totalMass -= 5
                playerObject.playerMass -=5
            if aiObject.aiMass > 30 and aiObject.aiMass < 35:#if the ai has more than 30 mass
                mainControlObject.totalMass -= 1#lose 2 mass
                aiObject.aiMass -=1
            if aiObject.aiMass > 35 and aiObject.aiMass < 45:
                mainControlObject.totalMass -= 2
                aiObject.Mass -=2
            if aiObject.aiMass > 40 and aiObject.playerMass < 60:
                mainControlObject.totalMass -= 3
                aiObject.aiMass -=3
            if aiObject.aiMass > 60 and aiObject.playerMass < 80:
                mainControlObject.totalMass -= 4
                aiObject.aiMass -=4
            if aiObject.aiMass > 80:
                mainControlObject.totalMass -= 5
                aiObject.aiMass -=5
            tickCount = 0#reset the counter
            

        #speed monitor
        #player
        if playerObject.playerMass > 20 and playerObject.playerMass < 30:
            playerObject.playerSpeed = 2
        if playerObject.playerMass > 40:
            playerObject.playerSpeed = 1
        #ai
        if aiObject.aiMass > 20 and aiObject.aiMass < 30:
            aiObject.aiSpeed = 2
        if aiObject.aiMass > 40:
            aiObject.aiSpeed = 1
            
        #if the split variable is true
        if doSplit is True:
            if direction == 'down':
                doSplit = False
            if direction == 'up':
                doSplit = False
            if direction == 'right':
                doSplit = False
            if direction == 'left':
                doSplit = False
        
        tickCount += 40#add to the counter
        foodTickCount += 40
        pygame.display.update()#update the game's display
        gameClock.tick(40)#add to the game clock
        
