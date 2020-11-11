import pygame

"""
PROGRAMME BIG MAP NAVIGATION
C'est un projet pour simuler la navigation sur une grande map vu de haut, avec la camera qui regarde
uniquement les allentours du joueur toujours au cente
"""



# =========================BACKEND=========================
# constant & parameters
WindowSize = 500
BlockSize = 25
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
Lev = []
Levers = ("L", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0")

# fonts
pygame.font.init()
font = pygame.font.SysFont("Times", 20)
WinFont = pygame.font.SysFont("Times", 20)

# map design
Floor2 = ["WWWWWWWWWWWWWWWWWWWW",
          "WP W        W   W 2W",
          "WW W WWWW W W W W WW",
          "W    W  W W W W W  W",
          "W WWWW    W W W    W",
          "W    WWWWWW W WWWWWW",
          "WWW       W W      W",
          "WWWWWWWWW W WWWWWW W",
          "W         W        W",
          "W WWWWWWWWWWWWWWWW W",
          "W         W        W",
          "WWWWWWWWW W WWWWWWWW",
          "W       W W W      W",
          "W WWWWW W W W WWWWWW",
          "W     W W W W W    W",
          "WWWWW W W W W W W  W",
          "W     W W W   W W WW",
          "W WW WW W WWWWW W  W",
          "W1W  W          WWSW",
          "WWWWWWWWWWWWWWWWWWWW"]


def render(MapToRender):
    """
    Render function
    Render the level design
    """
    global PlayerPos, player, txt, Exit, Lev

    for i in range(MapSizeBlock):
        for j in range(MapSizeBlock):

            if MapToRender[j][i] == "W": # W = Walls
                Walls.append([i, j])
                pygame.draw.rect(screen, (255, 255, 255), (i*BlockSize, j*BlockSize, BlockSize, BlockSize))
                
            elif MapToRender[j][i] == "P": # P = Player
                PlayerPos = [i, j]
                pygame.draw.rect(screen, (0, 0, 255), (i*BlockSize, j*BlockSize, BlockSize, BlockSize))

            elif MapToRender[j][i] == "S": # S = Sortie
                Exit = [i, j]
                pygame.draw.rect(screen, (0, 255, 0), (i*BlockSize, j*BlockSize, BlockSize, BlockSize))
            
            elif MapToRender[j][i] in Levers: # Lever
                Lev = [i, j]
                pygame.draw.rect(screen, (255, 255, 0), (i*BlockSize, j*BlockSize, BlockSize, BlockSize))
    
    pygame.display.flip()


# =========================FRONTEND=========================
# init window
pygame.init()
screen = pygame.display.set_mode((WindowSize, WindowSize))
pygame.display.set_caption("My Game")

render(Floor2)

# main loop
running = True
while running:

    # events check
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # check for closing window
            running = False
