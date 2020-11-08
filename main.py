import pygame

"""
Shayane Katchera
PROGRAMME BIG MAP NAVIGATION
C'est un projet pour simuler la navigation sur une grande map vu de haut, avec la camera qui regarde
uniquement les allentours du joueur toujours au cente
"""

# TODO (04/10/2020):
#   - add level with more than one lever
#   - add level with levers to activate in an exact order
#   - add level wil lot of lever, but not all necessary to finish level
#   - add monsters with basical movment, and a way to defeeat them


# =========================BACKEND=========================
# constant & parameters
WindowSize = 500
BlockSize = 250
MapSizeBlock = 20
WalkDistance = 25
PlayerInBlockPos = [BlockSize//2, BlockSize//2]
n = 0
WalkCount = 0
left = False
right = False
PlayerWidth = 32
PlayerHeight = 48
clock = pygame.time.Clock()
lvl = 0
Opened = False
SetLever = False
BottomTextSpace = 50
count = 0


# init
Walls = []
PlayerPos = []
player = ""
Exit = []
Levels = []
Lev = []
LeverLevels = [2, 3]


# fonts
pygame.font.init()
font = pygame.font.SysFont("Times", 20)
WinFont = pygame.font.SysFont("Times", 20)
ExplainFont = pygame.font.SysFont("Times", 18)


# map design
rdc = ["WWWWWWWWWWWWWWWWWWWW",
       "W   W              W",
       "W W W WWWWWWWWWWWW W",
       "W W W W            W",
       "W W   W W WWWWWWWWWW",
       "W WWWWW W W        W",
       "W W     W   WWWWWW W",
       "W W WWWWWWWWW    W W",
       "W W           WW W W",
       "W WWWWWWWWWWWWWW W W",
       "W        P   W   W W",
       "W WWWWWWWWWW W WWW W",
       "W          W W   W W",
       "W WWWWWWWW W WWWWW W",
       "W W        W W   W W",
       "W W  WWWWWWW W W W W",
       "W WW W     W W W   W",
       "W  WWW W WWW W WWWWW",
       "WW     W     W     S",
       "WWWWWWWWWWWWWWWWWWWW"]
Levels.append(rdc)

Floor1 = ["WWWWWWWWWWWWWWWWWWWW",
          "WSW                W",
          "W WWWWWWWWWWWWWWWW W",
          "W        W         W",
          "W WWWWWW W WWWWWWWWW",
          "W W      W         W",
          "W WWWWWWWWWWWWWWWW W",
          "W                W W",
          "W WWWWWWWWWWWWWW W W",
          "W W   W   W      W W",
          "WWW W   W   WWWWWW W",
          "W W WWWWWWW W   W  W",
          "W W W       W W W WW",
          "W W W WWWWWWW W W  W",
          "W W W         W  W W",
          "W W WWWWWWWWWWWW W W",
          "W W            W   W",
          "W WWWWWWWWWWWWWWWW W",
          "W                 PW",
          "WWWWWWWWWWWWWWWWWWWW"]
Levels.append(Floor1)

Floor2 = ["WWWWWWWWWWWWWWWWWWWW",
          "WP                 W",
          "W WWWWWWWWWWWWWWWW W",
          "W W         W   W  W",
          "W W WWWWWWW   W W WW",
          "W W       WWWWW    W",
          "W WWWWWWW     WWWW W",
          "W       WWWWW  W W W",
          "WWW WWW W   WW   W W",
          "W W W   W W  WWWWW W",
          "W W W  WW WW     W W",
          "W W WW W   WWWWW W W",
          "W W  W W W W   W W W",
          "W WW W W W   W W W W",
          "W W  W   WWWWW W W W",
          "W W WWW WW   W W W W",
          "W W     W  W   W W W",
          "W WWWWW W WWWWWW W W",
          "W       WLW      WSW",
          "WWWWWWWWWWWWWWWWWWWW"]
Levels.append(Floor2)

Floor3 = ["WWWWWWWWWWWWWWWWWWWW",
          "WSW              WLW",
          "W W WWWWWWWWWWWW W W",
          "W W W            W W",
          "W W W WWWWWWWWWWWW W",
          "W W W W     W   WW W",
          "W   W W WWW W W W  W",
          "WWW W W W   W W W WW",
          "W   W   W WWW W W  W",
          "W WWWWWWW WWW W WW W",
          "W W       W   W    W",
          "W W WWWWWWWWWWW WWWWW",
          "W W W   W   W      W",
          "W W W W W W W WWWW W",
          "W W   W   W   W    W",
          "W WWWWWWWWWWWWW WWWW",
          "W W   W   W   W    W",
          "W W W W W W W WWWW W",
          "WL  W   W   W      W",
          "WWWWWWWWWWWWWWWWWWWW"]
Levels.append(Floor3)


# images
walkRight = [pygame.image.load('Images\\R1.png'), pygame.image.load('Images\\R2.png'), pygame.image.load('Images\\R3.png'), pygame.image.load('Images\\R4.png'), pygame.image.load('Images\\R5.png'), pygame.image.load('Images\\R6.png'), pygame.image.load('Images\\R7.png'), pygame.image.load('Images\\R8.png'), pygame.image.load('Images\\R9.png')]
walkLeft = [pygame.image.load('Images\\L1.png'), pygame.image.load('Images\\L2.png'), pygame.image.load('Images\\L3.png'), pygame.image.load('Images\\L4.png'), pygame.image.load('Images\\L5.png'), pygame.image.load('Images\\L6.png'), pygame.image.load('Images\\L7.png'), pygame.image.load('Images\\L8.png'), pygame.image.load('Images\\L9.png')]
char = pygame.image.load('Images\\standing.png')

wall = pygame.image.load('Images\\bricks.png')
background = pygame.image.load('Images\\bg.png')
stair = pygame.image.load('Images\\stairs.png')

light = pygame.image.load('Images\\grad.png')
light = pygame.transform.scale(light, (WindowSize, WindowSize))

lever = pygame.image.load('Images\\lever.png')
lever=pygame.transform.scale(lever, (BlockSize, BlockSize))


# functions
def render(MapToRender):
    """
    Render function
    Render the level design
    """
    global PlayerPos, player, txt, Exit, Walls, Lev

    # reset
    Walls = [] 

    # get init data
    for i in range(MapSizeBlock):
        for j in range(MapSizeBlock):

            if MapToRender[j][i] == "W": # W = Walls
                Walls.append([i, j])
                
            elif MapToRender[j][i] == "P": # P = Player
                PlayerPos = [i, j]

            elif MapToRender[j][i] == "S": # S = Sortie
                Exit = [i, j]
            
            elif MapToRender[j][i] == "L": # Lever
                Lev.append([i, j])


def LocalRender(MapToRender):
    """
    Function to Render what should be displayed on the screen
    """
    global WalkCount
    # main needed informations
    # inblock coordinates of player
    x = PlayerInBlockPos[0]
    y = PlayerInBlockPos[1]

    #width and height of UpLeft block
    xUL = WindowSize//2 - x 
    yUL = WindowSize//2 - y

    # right blocks and down blocks coordinates
    xU = WindowSize//2 + (BlockSize-x)
    yL = WindowSize//2 + (BlockSize-y)

    # right blocks and down blocks width and height
    WUR = BlockSize-xUL
    HDL = BlockSize-yUL

    # Textures Rendering
    # upleft
    if [int(PlayerPos[0]-1), int(PlayerPos[1]-1)] in Walls:
        screen.blit(wall, (xUL-BlockSize, yUL-BlockSize))
    elif [int(PlayerPos[0]-1), int(PlayerPos[1]-1)] == Exit:
        screen.blit(stair, (xUL-BlockSize, yUL-BlockSize))
    else:
        screen.blit(background, (xUL-BlockSize, yUL-BlockSize))
    if [int(PlayerPos[0]-1), int(PlayerPos[1]-1)] == Lev:
        screen.blit(lever, (xUL-BlockSize, yUL-BlockSize))

    # up
    if [int(PlayerPos[0]), int(PlayerPos[1]-1)] in Walls:
        screen.blit(wall, (xUL, yUL-BlockSize))
    elif [int(PlayerPos[0]), int(PlayerPos[1]-1)] == Exit:
        screen.blit(stair, (xUL, yUL-BlockSize))
    else:
        screen.blit(background, (xUL, yUL-BlockSize))
    if [int(PlayerPos[0]+1), int(PlayerPos[1])] == Lev:
        screen.blit(lever, (xUL, yUL-BlockSize))

    # upright
    if [int(PlayerPos[0]+1), int(PlayerPos[1]-1)] in Walls: 
        screen.blit(wall, (xUL+BlockSize, yUL-BlockSize))
    elif [int(PlayerPos[0]+1), int(PlayerPos[1]-1)] == Exit:
        screen.blit(stair, (xUL+BlockSize, yUL-BlockSize))
    else:
        screen.blit(background, (xUL+BlockSize, yUL-BlockSize))
    if [int(PlayerPos[0]+1), int(PlayerPos[1]-1)] == Lev:
        screen.blit(lever, (xUL+BlockSize, yUL-BlockSize))

    # right
    if [int(PlayerPos[0]+1), int(PlayerPos[1])] in Walls:
        screen.blit(wall, (xUL+BlockSize, yUL))
    elif [int(PlayerPos[0]+1), int(PlayerPos[1])] == Exit:
        screen.blit(stair, (xUL+BlockSize, yUL))
    else:
        screen.blit(background, (xUL+BlockSize, yUL))
    if [int(PlayerPos[0]+1), int(PlayerPos[1])] == Lev:
        screen.blit(lever, (xUL+BlockSize, yUL))

    # downright
    if [int(PlayerPos[0]+1), int(PlayerPos[1]+1)] in Walls: 
        screen.blit(wall, (xUL+BlockSize, yUL+BlockSize))
    elif [int(PlayerPos[0]+1), int(PlayerPos[1]+1)] == Exit:
        screen.blit(stair, (xUL+BlockSize, yUL+BlockSize))
    else:
        screen.blit(background, (xUL+BlockSize, yUL+BlockSize))
    if [int(PlayerPos[0]+1), int(PlayerPos[1]+1)] == Lev:
        screen.blit(lever, (xUL+BlockSize, yUL+BlockSize))

    # down
    if [int(PlayerPos[0]), int(PlayerPos[1]+1)] in Walls: 
        screen.blit(wall, (xUL, yUL+BlockSize))
    elif [int(PlayerPos[0]), int(PlayerPos[1]+1)] == Exit:
        screen.blit(stair, (xUL, yUL+BlockSize))
    else:
        screen.blit(background, (xUL, yUL+BlockSize))
    if [int(PlayerPos[0]), int(PlayerPos[1]+1)] == Lev:
        screen.blit(lever, (xUL, yUL+BlockSize))

    # downleft
    if [int(PlayerPos[0]-1), int(PlayerPos[1]+1)] in Walls:
        screen.blit(wall, (xUL-BlockSize, yUL+BlockSize))
    elif [int(PlayerPos[0]-1), int(PlayerPos[1]+1)] == Exit:
        screen.blit(stair, (xUL-BlockSize, yUL+BlockSize))
    else:
        screen.blit(background, (xUL-BlockSize, yUL+BlockSize))
    if [int(PlayerPos[0]-1), int(PlayerPos[1]+1)] == Lev:
        screen.blit(lever, (xUL-BlockSize, yUL+BlockSize))

    # left
    if [int(PlayerPos[0]-1), int(PlayerPos[1])] in Walls:
        screen.blit(wall, (xUL-BlockSize, yUL))
    elif [int(PlayerPos[0]-1), int(PlayerPos[1])] == Exit:
        screen.blit(stair, (xUL-BlockSize, yUL))
    else:
        screen.blit(background, (xUL-BlockSize, yUL))
    if [int(PlayerPos[0]-1), int(PlayerPos[1])] == Lev:
        screen.blit(lever, (xUL-BlockSize, yUL))

    # middle background
    screen.blit(background, (xUL, yUL))

    # Sprite display
    if WalkCount + 1 >= 27:
        WalkCount = 0
    if left:
        screen.blit(walkLeft[WalkCount//3], (WindowSize//2-PlayerWidth, WindowSize//2-PlayerHeight))
        WalkCount += 1
    elif right:
        screen.blit(walkRight[WalkCount//3], (WindowSize//2-PlayerWidth, WindowSize//2-PlayerHeight))
        WalkCount +=1
    else:
        screen.blit(char, (WindowSize//2-PlayerWidth, WindowSize//2-PlayerHeight))
    
    # light display
    filter = pygame.surface.Surface((WindowSize, WindowSize))
    filter.fill(pygame.color.Color('Black')) # Black will give dark unlit areas, Grey will give you a fog
    filter.blit(light,(0, 0)) # blit light to the filter surface -400 is to center effect
    screen.blit(filter, (0, 0), special_flags=pygame.BLEND_RGBA_MIN) # blit filter surface but with a blend

    # hud text
    text = font.render("[{}, {}]".format(int(PlayerPos[0]), int(PlayerPos[1])), True, (255, 255, 255))
    text2 = font.render("[{}, {}]".format(int(PlayerInBlockPos[0]), int(PlayerInBlockPos[1])), True, (255, 255, 255))
    text3 = font.render("FPS : {}".format(int(clock.get_fps())), True, (255, 255, 255))
    text4 = font.render("Level : {}".format(lvl), True, (255, 255, 255))

    screen.blit(text, (WindowSize//2, 20)) 
    screen.blit(text2, (WindowSize//2, 40))
    screen.blit(text4, (WindowSize-100, 20))


    # update display
    pygame.display.flip()


def GoUp():
    """
    Thread run when Z button is pressed to go up in the maze
    """
    global player, txt, Exit, right, left, WalkCount, lvl, Opened, text5
    # wall collision check
    if (([PlayerPos[0], int(PlayerPos[1] - (WalkDistance/BlockSize))]) not in Walls) or (PlayerInBlockPos[1] - WalkDistance >= PlayerHeight//2) :
        # update data
        WalkCount += 1
        right = True
        PlayerInBlockPos[1] -= WalkDistance
        if PlayerInBlockPos[1] < 0:
            PlayerPos[1] -= 1
            PlayerInBlockPos[1] += BlockSize

        # lever collision check
        if SetLever:
            if PlayerPos in Lev:
                if len(Lev) < 2: # found all levers
                    Opened = True
                else:
                    Lev.pop(Lev.index(PlayerPos))
                    pygame.display.flip()

        # exit point collision check
        if PlayerPos == Exit:
            if SetLever:
                if Opened:
                    lvl += 1
                    try:
                        render(Levels[lvl])
                    except IndexError:
                        text = WinFont.render("Congratulation, you found the exit".upper(), True, (255, 255, 255))
                        screen.blit(text, (0, 0))
                        pygame.display.flip()
                        return(0) # force exit function
                else:
                    pass # complete this part later
            else:
                lvl += 1
                try:
                    render(Levels[lvl])
                except IndexError:
                    text = WinFont.render("Congratulation, you found the exit".upper(), True, (255, 255, 255))
                    screen.blit(text, (WindowSize//4, WindowSize//2-10))
                    pygame.display.flip()
                    return(0) # force exit function

        # update display
        LocalRender(Levels[lvl])



def GoDown():
    """
    Thread run when s button is pressed to go down in the maze
    """
    global player, txt, Exit, right, left, WalkCount, lvl, Opened, text5
    # wall collision check
    if (([PlayerPos[0], int(PlayerPos[1] + (WalkDistance/BlockSize) + 1)]) not in Walls) or (PlayerInBlockPos[1] + WalkDistance <= BlockSize-PlayerHeight//2) :
        # update data
        WalkCount += 1
        left = True
        PlayerInBlockPos[1] += WalkDistance
        if PlayerInBlockPos[1] > BlockSize:
            PlayerPos[1] += 1
            PlayerInBlockPos[1] -= BlockSize
        
        # lever collision check
        if SetLever:
            if PlayerPos in Lev:
                if len(Lev) < 2: # found all levers
                    Opened = True
                else:
                    Lev.pop(Lev.index(PlayerPos))
                    pygame.display.flip()
                    

        # exit point collision check
        if PlayerPos == Exit:
            if SetLever:
                if Opened:
                    lvl += 1
                    try:
                        render(Levels[lvl])
                    except IndexError:
                        text = WinFont.render("Congratulation, you found the exit".upper(), True, (255, 255, 255))
                        screen.blit(text, (0, 0))
                        pygame.display.flip()
                        return(0) # force exit function
                else:
                    pass # complete this part later
            else:
                lvl += 1
                try:
                    render(Levels[lvl])
                except IndexError:
                    text = WinFont.render("Congratulation, you found the exit".upper(), True, (255, 255, 255))
                    screen.blit(text, (WindowSize//4, WindowSize//2-10))
                    pygame.display.flip()
                    return(0) # force exit function

        # update display
        LocalRender(Levels[lvl])


def GoLeft():
    """
    Thread run when q button is pressed to go left in the maze
    """
    global player, txt, Exit, WalkCount, left, right, lvl, Opened, text5
    # wall collision check
    if (([int(PlayerPos[0] - (WalkDistance/BlockSize)), PlayerPos[1]]) not in Walls) or (PlayerInBlockPos[0] - WalkDistance >= PlayerWidth) :
        # update data
        WalkCount += 1
        left = True
        PlayerInBlockPos[0] -= WalkDistance
        if PlayerInBlockPos[0] < 0:
            PlayerPos[0] -= 1
            PlayerInBlockPos[0] += BlockSize
        
        # lever collision check
        if SetLever:
            if PlayerPos in Lev:
                if len(Lev) < 2: # found all lever
                    Opened = True
                else:
                    Lev.pop(Lev.index(PlayerPos))
                    pygame.display.flip()

        # exit point collision check
        if PlayerPos == Exit:
            if SetLever:
                if Opened:
                    lvl += 1
                    try:
                        render(Levels[lvl])
                    except IndexError:
                        text = WinFont.render("Congratulation, you found the exit".upper(), True, (255, 255, 255))
                        screen.blit(text, (0, 0))
                        pygame.display.flip()
                        return(0) # force exit function
                else:
                    pass # complete this part later
            else:
                lvl += 1
                try:
                    render(Levels[lvl])
                except IndexError:
                    text = WinFont.render("Congratulation, you found the exit".upper(), True, (255, 255, 255))
                    screen.blit(text, (WindowSize//4, WindowSize//2-10))
                    pygame.display.flip()
                    return(0) # force exit function

        # update display
        LocalRender(Levels[lvl])


def GoRight():
    """
    Thread run when d button is pressed to right down in the maze
    """
    global player, txt, Exit, WalkCount, right, left, lvl, Opened, text5
    # wall collision check
    if (([int(PlayerPos[0] + (WalkDistance/BlockSize) + 1), PlayerPos[1]]) not in Walls) or (PlayerInBlockPos[0] + WalkDistance <= BlockSize-PlayerWidth) :
        # update data
        WalkCount += 1
        right = True
        PlayerInBlockPos[0] += WalkDistance
        if PlayerInBlockPos[0] > BlockSize:
            PlayerPos[0] += 1
            PlayerInBlockPos[0] -= BlockSize
        
        # lever collision check
        if SetLever:
            if PlayerPos in Lev:
                if len(Lev) < 2: # found all levers
                    Opened = True
                    
                    
                else:
                    
                    Lev.pop(Lev.index(PlayerPos))
                    pygame.display.flip()

        # exit point collision check
        if PlayerPos == Exit:
            if SetLever:
                if Opened:
                    lvl += 1
                    try:
                        render(Levels[lvl])
                    except IndexError:
                        text = WinFont.render("Congratulation, you found the exit".upper(), True, (255, 255, 255))
                        screen.blit(text, (0, 0))
                        pygame.display.flip()
                        return(0) # force exit function
                else:
                    pass # complete this part later
            else:
                lvl += 1
                try:
                    render(Levels[lvl])
                except IndexError:
                    text = WinFont.render("Congratulation, you found the exit".upper(), True, (255, 255, 255))
                    screen.blit(text, (WindowSize//4, WindowSize//2-10))
                    pygame.display.flip()
                    return 0 # force exit function

        # update display
        LocalRender(Levels[lvl])



# =========================FRONTEND=========================
# init window
pygame.init()
screen = pygame.display.set_mode((WindowSize, WindowSize+BottomTextSpace))
pygame.display.set_caption("My Game")

# init data & display
render(Levels[lvl])
LocalRender(Levels[lvl])

# main loop
running = True
while running:

    # events check
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # check for closing window
            running = False
    
    # movement keys
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        GoUp()
    elif keys[pygame.K_s]:
        GoDown()
    elif keys[pygame.K_a]:
        GoLeft()
    elif keys[pygame.K_d]:
        GoRight()

    # FPS update display
    text3 = font.render("FPS : "+str(int(clock.get_fps())), True, (255, 255, 255))
    screen.blit(text3, (10, 10))
    clock.tick(60)

    # update data 
    if lvl in LeverLevels:
        SetLever = True
    else:
        SetLever = False

    # Bottom text
    pygame.draw.rect(screen, (0, 0, 0), (0, WindowSize, WindowSize, BottomTextSpace))
    if lvl == 0:
        text5 = ExplainFont.render("Welcome in the MazeGame. To pass this level, find the stairs", True, (255, 255, 255))
        text5bis = ExplainFont.render("", True, (255, 255, 255))
    elif lvl == 1:
        text5 = ExplainFont.render("Welcome in the Level 2. To pass this level, find the stairs", True, (255, 255, 255))
        text5bis = ExplainFont.render("", True, (255, 255, 255))
    elif lvl == 2:
        if Opened:
            text5 = ExplainFont.render("Now, to pass this level, find the stairs", True, (255, 255, 255))
            text5bis = ExplainFont.render("", True, (255, 255, 255))
        else:
            text5 = ExplainFont.render("Welcome in the Level 3. To pass this level, find the lever,", True, (255, 255, 255))
            text5bis = ExplainFont.render("and then find the stairs", True, (255, 255, 255))
    elif lvl == 3:
        if not Opened:
            text5 = ExplainFont.render("Welcome in the Level 4. To pass this level, find the levers,", True, (255, 255, 255))
            text5bis = ExplainFont.render("and then find the stairs", True, (255, 255, 255))
        else:
            text5 = ExplainFont.render("Now, to pass this level, find the stairs", True, (255, 255, 255))
            text5bis = ExplainFont.render("", True, (255, 255, 255))

    screen.blit(text5, (20, WindowSize+5))
    screen.blit(text5bis, (20, WindowSize+30))

    pygame.display.flip()