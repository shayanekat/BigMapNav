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
#  DONE - changer le joueur de bloc à petit cercle
#  DONE - ajouter des couleurs
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

# fonts
pygame.font.init()
font = pygame.font.SysFont("Times", 20)
WinFont = pygame.font.SysFont("Times", 20)

# map design
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
                pygame.draw.rect(screen, (255, 255, 255), (i*BlockSize, j*BlockSize, BlockSize, BlockSize))
                
            elif MapToRender[j][i] == "P": # P = Player
                PlayerPos = [i, j]
                pygame.draw.rect(screen, (0, 0, 255), (i*BlockSize, j*BlockSize, BlockSize, BlockSize))

            elif MapToRender[j][i] == "S": # S = Sortie
                Exit = [i, j]
                pygame.draw.rect(screen, (0, 255, 0), (i*BlockSize, j*BlockSize, BlockSize, BlockSize))
    
    pygame.display.flip()


# =========================FRONTEND=========================
# init window
pygame.init()
screen = pygame.display.set_mode((WindowSize, WindowSize))
pygame.display.set_caption("My Game")

render(Floor1)

# main loop
running = True
while running:

    # events check
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # check for closing window
            running = False
