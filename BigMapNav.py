from tkinter import *

"""
PROGRAMME BIG MAP NAVIGATION
C'est un projet pour simuler la navigation sur une grande map vu de haut, avec la camera qui regarde
uniquement les allentours du joueur toujours au cente
"""

# TODO (21/09/2020): 
#  DONE - initialiser la fenetre
#  DONE - faire le design de la big map
#  DONE - afficher la BigMap en entier
#   - implémenter le mouvement du joueur
#   - implémenter les collisions
#   - reduire la distance d'affichage 
# ============== V1 Fini =====================
#   - ajouter des couleurs
#   - ajouter l'implementation d'étages
#   - implémentation de lumiere
#   - implémentation de dynamique light
#   - implémentation des ombres
# ============== V2 Fini =====================
#   - exporter de tkinter vers pygame
#   - optimiser le code
#   - ajouter des IAs (dans un premier temps dans un fichier test pour inclure du pathfinding)
# ============== V3 Fini =====================


# =========================BACKEND=========================
# constant & parameters
WindwSize = 500
BlockSize = 25
MapSizeBlock = 20
Walls = []
PlayerPos = []
player = ""

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


def render(MapToRender):
    """
    Render function
    Render the level design
    """
    global PlayerPos, player

    for i in range(MapSizeBlock):
        for j in range(MapSizeBlock):

            if MapToRender[j][i] == "W": # W = Walls
                can.create_rectangle(i*BlockSize, j*BlockSize, (i+1)*BlockSize, (j+1)*BlockSize, fill="white")
                Walls.append([i,j])
                
            elif MapToRender[j][i] == "P": # P = Player
                player = can.create_rectangle(i*BlockSize, j*BlockSize, (i+1)*BlockSize, (j+1)*BlockSize, fill="blue")
                PlayerPos = [i,j]

            elif MapToRender[j][i] == "S": # S = Sortie
                can.create_rectangle(i*BlockSize, j*BlockSize, (i+1)*BlockSize, (j+1)*BlockSize, fill="green")


def GoUp(event):
    """
    Thread run when Z button is pressed to go up in the maze
    """
    global player
    if (PlayerPos[1] - 1) not in Walls :
        PlayerPos[1] -= 1
        can.delete(player)
        player = can.create_rectangle(PlayerPos[0]*BlockSize, PlayerPos[1]*BlockSize, (PlayerPos[0]+1)*BlockSize, (PlayerPos[1]+1)*BlockSize, fill="blue")


def GoDown(event):
    """
    Thread run when s button is pressed to go down in the maze
    """
    global player
    if (PlayerPos[1] + 1) not in Walls :
        PlayerPos[1] += 1
        can.delete(player)
        player = can.create_rectangle(PlayerPos[0]*BlockSize, PlayerPos[1]*BlockSize, (PlayerPos[0]+1)*BlockSize, (PlayerPos[1]+1)*BlockSize, fill="blue")


def GoLeft(event):
    """
    Thread run when q button is pressed to go left in the maze
    """
    global player
    if (PlayerPos[0] - 1) not in Walls :
        PlayerPos[0] -= 1
        can.delete(player)
        player = can.create_rectangle(PlayerPos[0]*BlockSize, PlayerPos[1]*BlockSize, (PlayerPos[0]+1)*BlockSize, (PlayerPos[1]+1)*BlockSize, fill="blue")


def GoRight(event):
    """
    Thread run when d button is pressed to right down in the maze
    """
    global player
    if (PlayerPos[0] + 1) not in Walls :
        PlayerPos[0] += 1
        can.delete(player)
        player = can.create_rectangle(PlayerPos[0]*BlockSize, PlayerPos[1]*BlockSize, (PlayerPos[0]+1)*BlockSize, (PlayerPos[1]+1)*BlockSize, fill="blue")

# =========================FRONTEND=========================
root = Tk()
root.title("BigMapNav")

can = Canvas(root, width=WindwSize, height=WindwSize, bg="black")
root.bind("z", GoUp)
root.bind("s",GoDown)
root.bind("q", GoLeft)
root.bind("d",GoRight)
can.pack(padx=5, pady=5)

render(Map)

root.mainloop()