import pygame

"""
PROGRAMME BIG MAP NAVIGATION
C'est un projet pour simuler la navigation sur une grande map vu de haut, avec la camera qui regarde
uniquement les allentours du joueur toujours au cente
"""

# TODO (21/09/2020): 
#  DONE - initialiser la fenetre
#  DONE - faire le design de la big map
#  DONE - afficher la BigMap en entier
#  DONE - implémenter le mouvement du joueur
#  DONE - implémenter les collisions
#  DONE - reduire la distance d'affichage 
# ============== V1 Fini =====================
#  DONE - exporter de tkinter vers pygame
#   - changer le joueur de bloc à petit cercle
#   - ajouter des couleurs
#   - ajouter l'implementation d'étages
#   - implémentation de lumiere
#   - implémentation de dynamique light
#   - implémentation des ombres
# ============== V2 Fini =====================
#   - optimiser le code
#   - ajouter des IAs (dans un premier temps dans un fichier test pour inclure du pathfinding)
# ============== V3 Fini =====================

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

# init
Walls = []
PlayerPos = []
player = ""
Exit = []

# fonts
pygame.font.init()
font = pygame.font.SysFont("Times", 20)
WinFont = pygame.font.SysFont("Times", 20)

# map design
Map = ["WWWWWWWWWWWWWWWWWWWW",
       "W   W              W",
       "W W W WWWWWWWWWWWW W",
       "W W W W            W",
       "W W   W W WWWWWWWWWW",
       "W WWWWW W W        W",
       "W W     W   WWWWWW W",
       "W W WWWWWWWWW    W W",
       "W W           WW W W",
       "W WWWWWWWWWWWWWW W W",
       "W        p P W   W W",
       "W WWWWWWWWWW W WWW W",
       "W          W W   W W",
       "W WWWWWWWW W WWWWW W",
       "W W        W W   W W",
       "W W  WWWWWWW W W W W",
       "W WW W     W W W   W",
       "W  WWW W WWW W WWWWW",
       "WW     W     W     S",
       "WWWWWWWWWWWWWWWWWWWW"]

# images
walkRight = [pygame.image.load('Images\\R1.png'), pygame.image.load('Images\\R2.png'), pygame.image.load('Images\\R3.png'), pygame.image.load('Images\\R4.png'), pygame.image.load('Images\\R5.png'), pygame.image.load('Images\\R6.png'), pygame.image.load('Images\\R7.png'), pygame.image.load('Images\\R8.png'), pygame.image.load('Images\\R9.png')]
walkLeft = [pygame.image.load('Images\\L1.png'), pygame.image.load('Images\\L2.png'), pygame.image.load('Images\\L3.png'), pygame.image.load('Images\\L4.png'), pygame.image.load('Images\\L5.png'), pygame.image.load('Images\\L6.png'), pygame.image.load('Images\\L7.png'), pygame.image.load('Images\\L8.png'), pygame.image.load('Images\\L9.png')]
char = pygame.image.load('Images\\standing.png')
wall = pygame.image.load('Images\\bricks.png')
background = pygame.image.load('Images\\bg.png')


def render(MapToRender):
    """
    Render function
    Render the level design
    """
    global PlayerPos, player, txt, Exit

    for i in range(MapSizeBlock):
        for j in range(MapSizeBlock):

            if MapToRender[j][i] == "W": # W = Walls
                Walls.append([i, j])
                
            elif MapToRender[j][i] == "P": # P = Player
                PlayerPos = [i, j]

            elif MapToRender[j][i] == "S": # S = Sortie
                Exit = [i, j]


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

    # Render
    if [int(PlayerPos[0]-1), int(PlayerPos[1]-1)] in Walls: # Up Left
        screen.blit(wall, (xUL-BlockSize, yUL-BlockSize))
    else:
        screen.blit(background, (xUL-BlockSize, yUL-BlockSize))

    if [int(PlayerPos[0]), int(PlayerPos[1]-1)] in Walls: # Up 
        screen.blit(wall, (xUL, yUL-BlockSize))
    else:
        screen.blit(background, (xUL, yUL-BlockSize))

    if [int(PlayerPos[0]+1), int(PlayerPos[1]-1)] in Walls: # Up Right
        screen.blit(wall, (xUL+BlockSize, yUL-BlockSize))
    else:
        screen.blit(background, (xUL+BlockSize, yUL-BlockSize))

    if [int(PlayerPos[0]+1), int(PlayerPos[1])] in Walls: # Right
        screen.blit(wall, (xUL+BlockSize, yUL))
    else:
        screen.blit(background, (xUL+BlockSize, yUL))

    if [int(PlayerPos[0]+1), int(PlayerPos[1]+1)] in Walls: # Down Right
        screen.blit(wall, (xUL+BlockSize, yUL+BlockSize))
    else:
        screen.blit(background, (xUL+BlockSize, yUL+BlockSize))

    if [int(PlayerPos[0]), int(PlayerPos[1]+1)] in Walls: # Downd
        screen.blit(wall, (xUL, yUL+BlockSize))
    else:
        screen.blit(background, (xUL, yUL+BlockSize))

    if [int(PlayerPos[0]-1), int(PlayerPos[1]+1)] in Walls: # Down Left
        screen.blit(wall, (xUL-BlockSize, yUL+BlockSize))
    else:
        screen.blit(background, (xUL-BlockSize, yUL+BlockSize))

    if [int(PlayerPos[0]-1), int(PlayerPos[1])] in Walls: # Left
        screen.blit(wall, (xUL-BlockSize, yUL))
    else:
        screen.blit(background, (xUL-BlockSize, yUL))

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


    text = font.render("[{}, {}]".format(int(PlayerPos[0]), int(PlayerPos[1])), True, (0, 0, 0))
    text2 = font.render("[{}, {}]".format(int(PlayerInBlockPos[0]), int(PlayerInBlockPos[1])), True, (0, 0, 0))
    text3 = font.render("FPS : {}".format(int(clock.get_fps())), True, (0, 0, 0))
    screen.blit(text, (WindowSize//2, 20)) 
    screen.blit(text2, (WindowSize//2, 40))
    
    pygame.display.flip()


def GoUp():
    """
    Thread run when Z button is pressed to go up in the maze
    """
    global player, txt, Exit, n, right, left, WalkCount
    if (([PlayerPos[0], int(PlayerPos[1] - (WalkDistance/BlockSize))]) not in Walls) or (PlayerInBlockPos[1] - WalkDistance >= PlayerHeight//2) :
        WalkCount += 1
        right = True
        left = False
        PlayerInBlockPos[1] -= WalkDistance
        if PlayerInBlockPos[1] < 0:
            PlayerPos[1] -= 1
            PlayerInBlockPos[1] += BlockSize

        LocalRender(Map)

        if PlayerPos == Exit:
            text = WinFont.render("Congratulation, you found the exit".upper(), True, (0, 0, 0))
            screen.blit(text, (WindowSize//4, WindowSize//4))
            pygame.display.flip()


def GoDown():
    """
    Thread run when s button is pressed to go down in the maze
    """
    global player, txt, Exit, right, left, WalkCount
    if (([PlayerPos[0], int(PlayerPos[1] + (WalkDistance/BlockSize) + 1)]) not in Walls) or (PlayerInBlockPos[1] + WalkDistance <= BlockSize-PlayerHeight//2) :
        WalkCount += 1
        left = True
        right = False
        PlayerInBlockPos[1] += WalkDistance
        if PlayerInBlockPos[1] > BlockSize:
            PlayerPos[1] += 1
            PlayerInBlockPos[1] -= BlockSize
        
        LocalRender(Map)
        
        if PlayerPos == Exit:
            text = WinFont.render("Congratulation, you found the exit".upper(), True, (0, 0, 0))
            screen.blit(text, (WindowSize//4, WindowSize//4))
            pygame.display.flip()


def GoLeft():
    """
    Thread run when q button is pressed to go left in the maze
    """
    global player, txt, Exit, WalkCount, left, right
    if (([int(PlayerPos[0] - (WalkDistance/BlockSize)), PlayerPos[1]]) not in Walls) or (PlayerInBlockPos[0] - WalkDistance >= PlayerWidth) :
        WalkCount += 1
        left = True
        right = False
        PlayerInBlockPos[0] -= WalkDistance
        if PlayerInBlockPos[0] < 0:
            PlayerPos[0] -= 1
            PlayerInBlockPos[0] += BlockSize
        
        LocalRender(Map)
        
        if PlayerPos == Exit:
            text = WinFont.render("Congratulation, you found the exit".upper(), True, (0, 0, 0))
            screen.blit(text, (WindowSize//4, WindowSize//4))
            pygame.display.flip()


def GoRight():
    """
    Thread run when d button is pressed to right down in the maze
    """
    global player, txt, Exit, WalkCount, right, left
    if (([int(PlayerPos[0] + (WalkDistance/BlockSize) + 1), PlayerPos[1]]) not in Walls) or (PlayerInBlockPos[0] + WalkDistance <= BlockSize-PlayerWidth) :
        WalkCount += 1
        right = True
        left = False
        PlayerInBlockPos[0] += WalkDistance
        if PlayerInBlockPos[0] > BlockSize:
            PlayerPos[0] += 1
            PlayerInBlockPos[0] -= BlockSize
        
        LocalRender(Map)
        
        if PlayerPos == Exit:
            text = WinFont.render("Congratulation, you found the exit".upper(), True, (0, 0, 0))
            screen.blit(text, (WindowSize//4, WindowSize//4))
            pygame.display.flip()

# =========================FRONTEND=========================
# init window
pygame.init()
screen = pygame.display.set_mode((WindowSize, WindowSize))
pygame.display.set_caption("My Game")

render(Map)
LocalRender(Map)

# main loop
running = True
while running:

    # events check
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # check for closing window
            running = False
    
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
    text3 = font.render("FPS : "+str(int(clock.get_fps())), True, (0, 0, 0))
    screen.blit(text3, (10, 10))
    clock.tick(60)
    pygame.display.flip()
