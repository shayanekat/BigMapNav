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
PlayerRadius = 20
WalkDistance = 20
PlayerInBlockPos = [BlockSize//2, BlockSize//2]

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
       "W        p   W   W W",
       "W WWWWWWWWWW W WWW W",
       "W          W W   W W",
       "W WWWWWWWW W WWWWW W",
       "W W        W W   W W",
       "W W  WWWWWWW W W W W",
       "W WW W     W W W   W",
       "W  WWW W WWW W WWWWW",
       "WW     W     W    PS",
       "WWWWWWWWWWWWWWWWWWWW"]

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
    screen.fill((0, 0, 0))

    pygame.draw.circle(screen, (0, 0, 255), (WindowSize//2, WindowSize//2), PlayerRadius)

    if [int(PlayerPos[0]-1), int(PlayerPos[1]-1)] in Walls: # Up Left
        pygame.draw.rect(screen, (255, 255, 255), (0, 0, WindowSize//2-PlayerInBlockPos[0], WindowSize//2-PlayerInBlockPos[1])) 

    if [int(PlayerPos[0]), int(PlayerPos[1]-1)] in Walls: # Up 
        pygame.draw.rect(screen, (255, 255, 255), (WindowSize//2-PlayerInBlockPos[0], 0, BlockSize, WindowSize//2-PlayerInBlockPos[1]))

    if [int(PlayerPos[0]+1), int(PlayerPos[1]-1)] in Walls: # Up Right
        pygame.draw.rect(screen, (255, 255, 255), (WindowSize//2+(BlockSize-PlayerInBlockPos[0]), 0, WindowSize-(WindowSize//2+(BlockSize-PlayerInBlockPos[0])), WindowSize//2-PlayerInBlockPos[1]))

    if [int(PlayerPos[0]+1), int(PlayerPos[1])] in Walls: # Right
        pygame.draw.rect(screen, (255, 255, 255), (WindowSize//2+(BlockSize-PlayerInBlockPos[0]), WindowSize//2-PlayerInBlockPos[1], WindowSize-(WindowSize//2+(BlockSize-PlayerInBlockPos[0])), BlockSize))

    if [int(PlayerPos[0]+1), int(PlayerPos[1]+1)] in Walls: # Down Right
        pygame.draw.rect(screen, (255, 255, 255), (WindowSize//2+(BlockSize-PlayerInBlockPos[0]), WindowSize//2+(BlockSize-PlayerInBlockPos[1]), WindowSize-(WindowSize//2+(BlockSize-PlayerInBlockPos[0])), WindowSize-(WindowSize//2+(BlockSize-PlayerInBlockPos[1]))))

    if [int(PlayerPos[0]), int(PlayerPos[1]+1)] in Walls: # Down
        pygame.draw.rect(screen, (255, 255, 255), (WindowSize//2-PlayerInBlockPos[0], WindowSize//2+(BlockSize-PlayerInBlockPos[1]), BlockSize, WindowSize-(WindowSize//2+(BlockSize-PlayerInBlockPos[1]))))

    if [int(PlayerPos[0]-1), int(PlayerPos[1]+1)] in Walls: # Down Left
        pygame.draw.rect(screen, (255, 255, 255), (0, WindowSize//2+(BlockSize-PlayerInBlockPos[1]), WindowSize//2-PlayerInBlockPos[0], WindowSize-(WindowSize//2+(BlockSize-PlayerInBlockPos[1]))))

    if [int(PlayerPos[0]-1), int(PlayerPos[1])] in Walls: # Left
        pygame.draw.rect(screen, (255, 255, 255), (0, WindowSize//2-PlayerInBlockPos[1], WindowSize//2-PlayerInBlockPos[0], BlockSize))

    text = font.render("[{}, {}]".format(int(PlayerPos[0]), int(PlayerPos[1])), True, (128,128,128))
    screen.blit(text, (WindowSize//2, 20)) 
    
    pygame.display.flip()


def GoUp():
    """
    Thread run when Z button is pressed to go up in the maze
    """
    global player, txt, Exit
    if ([PlayerPos[0], int(PlayerPos[1] - (WalkDistance/BlockSize))]) not in Walls :
        PlayerPos[1] -= (WalkDistance/BlockSize)
        
        PlayerInBlockPos[1] -= WalkDistance
        LocalRender(Map)
        if PlayerPos == Exit:
            text = WinFont.render("Congratulation, you found the exit".upper(), True, (0, 0, 0))
            screen.blit(text, (WindowSize//4, WindowSize//4))
            pygame.display.flip()


def GoDown():
    """
    Thread run when s button is pressed to go down in the maze
    """
    global player, txt, Exit
    if ([PlayerPos[0], int(PlayerPos[1] + (WalkDistance/BlockSize))]) not in Walls :
        PlayerPos[1] += (WalkDistance/BlockSize)
        PlayerInBlockPos[1] += WalkDistance
        LocalRender(Map)
        if PlayerPos == Exit:
            text = WinFont.render("Congratulation, you found the exit".upper(), True, (0, 0, 0))
            screen.blit(text, (WindowSize//4, WindowSize//4))
            pygame.display.flip()


def GoLeft():
    """
    Thread run when q button is pressed to go left in the maze
    """
    global player, txt, Exit
    if ([int(PlayerPos[0] - (WalkDistance/BlockSize)), PlayerPos[1]]) not in Walls :
        PlayerPos[0] -= (WalkDistance/BlockSize)
        PlayerInBlockPos[0] -= WalkDistance
        LocalRender(Map)
        if PlayerPos == Exit:
            text = WinFont.render("Congratulation, you found the exit".upper(), True, (0, 0, 0))
            screen.blit(text, (WindowSize//4, WindowSize//4))
            pygame.display.flip()


def GoRight():
    """
    Thread run when d button is pressed to right down in the maze
    """
    global player, txt, Exit
    if ([int(PlayerPos[0] + (WalkDistance/BlockSize)), PlayerPos[1]]) not in Walls :
        PlayerPos[0] += (WalkDistance/BlockSize)
        PlayerInBlockPos[0] += WalkDistance
        LocalRender(Map)
        if PlayerPos == Exit:
            text = WinFont.render("Congratulation, you can exit", True.upper(), (0, 0, 0))
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
        if event.type == pygame.KEYDOWN: # button pressed on keyboard
            if event.key == pygame.K_w:
                GoUp()
            if event.key == pygame.K_s:
                GoDown()
            if event.key == pygame.K_a:
                GoLeft()
            if event.key == pygame.K_d:
                GoRight()
