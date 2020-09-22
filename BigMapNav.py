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
#  DONE - implémenter le mouvement du joueur
#  DONE - implémenter les collisions
#  DONE - reduire la distance d'affichage 
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
WindowSize = 500
BlockSize = 250
MapSizeBlock = 20
Walls = []
PlayerPos = []
player = ""
Exit = []

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
                # can.create_rectangle((i-8.5)*BlockSize, (j-9.5)*BlockSize, (i-7.5)*BlockSize, (j-8.5)*BlockSize, fill="white")
                Walls.append([i, j])
                
            elif MapToRender[j][i] == "P": # P = Player
                # player = can.create_rectangle((i-8.5)*BlockSize, (j-9.5)*BlockSize, (i-7.5)*BlockSize, (j-8.5)*BlockSize, fill="blue")
                PlayerPos = [i, j]

            elif MapToRender[j][i] == "S": # S = Sortie
                # can.create_rectangle((i-8.5)*BlockSize, (j-9.5)*BlockSize, (i-7.5)*BlockSize, (j-8.5)*BlockSize, fill="green")
                Exit = [i, j]

def LocalRender(MapToRender):
    """
    Function to Render what should be displayed on the screen
    """
    can.delete('all')

    can.create_rectangle(WindowSize/4, WindowSize/4, WindowSize/4+BlockSize, WindowSize/4+BlockSize, fill="blue")

    if [PlayerPos[0]-1, PlayerPos[1]-1] in Walls: # Up Left
        can.create_rectangle(0, 0, WindowSize/4, WindowSize/4, fill="White")

    if [PlayerPos[0], PlayerPos[1]-1] in Walls: # Up 
        can.create_rectangle(WindowSize/4, 0, WindowSize/4+BlockSize, WindowSize/4, fill="White")

    if [PlayerPos[0]+1, PlayerPos[1]-1] in Walls: # Up Right
        can.create_rectangle(WindowSize/4+BlockSize, 0, WindowSize, WindowSize/4, fill="White")

    if [PlayerPos[0]+1, PlayerPos[1]] in Walls: # Right
        can.create_rectangle(WindowSize/4+BlockSize, WindowSize/4, WindowSize, WindowSize/4+BlockSize, fill="White")

    if [PlayerPos[0]+1, PlayerPos[1]+1] in Walls: # Down Right
        can.create_rectangle(WindowSize/4+BlockSize, WindowSize/4+BlockSize, WindowSize, WindowSize, fill="White")

    if [PlayerPos[0], PlayerPos[1]+1] in Walls: # Down 
        can.create_rectangle(WindowSize/4, WindowSize/4+BlockSize, WindowSize/4+BlockSize, WindowSize, fill="White")

    if [PlayerPos[0]-1, PlayerPos[1]+1] in Walls: # Down Left
        can.create_rectangle(0, WindowSize/4+BlockSize, WindowSize/4, WindowSize, fill="White")

    if [PlayerPos[0]-1, PlayerPos[1]] in Walls: # Left
        can.create_rectangle(0, WindowSize/4, WindowSize/4, WindowSize/4+BlockSize, fill="White")

    can.create_text(WindowSize/2, 18, text="[{}, {}]".format(PlayerPos[0], PlayerPos[1]), fill="#808080")
    can.update()



def GoUp(event):
    """
    Thread run when Z button is pressed to go up in the maze
    """
    global player, txt, Exit
    if ([PlayerPos[0], PlayerPos[1] - 1]) not in Walls :
        PlayerPos[1] -= 1
        # can.delete(player)
        LocalRender(Map)
        if PlayerPos == Exit:
            can.create_text(WindowSize/2, WindowSize/2, text="Congratulation, you found the exit".upper(), font="Times 18 bold", fill="black", width=BlockSize, justify=CENTER)
        # player = can.create_rectangle(PlayerPos[0]*BlockSize, PlayerPos[1]*BlockSize, (PlayerPos[0]+1)*BlockSize, (PlayerPos[1]+1)*BlockSize, fill="blue")


def GoDown(event):
    """
    Thread run when s button is pressed to go down in the maze
    """
    global player, txt, Exit
    if ([PlayerPos[0], PlayerPos[1] + 1]) not in Walls :
        PlayerPos[1] += 1
        # can.delete(player)
        LocalRender(Map)
        if PlayerPos == Exit:
            can.create_text(WindowSize/2, WindowSize/2, text="Congratulation, you found the exit".upper(), font="Times 18 bold", fill="black", width=BlockSize, justify=CENTER)
        # player = can.create_rectangle(PlayerPos[0]*BlockSize, PlayerPos[1]*BlockSize, (PlayerPos[0]+1)*BlockSize, (PlayerPos[1]+1)*BlockSize, fill="blue")


def GoLeft(event):
    """
    Thread run when q button is pressed to go left in the maze
    """
    global player, txt, Exit
    if ([PlayerPos[0] - 1, PlayerPos[1]]) not in Walls :
        PlayerPos[0] -= 1
        # can.delete(player)
        LocalRender(Map)
        if PlayerPos == Exit:
            can.create_text(WindowSize/2, WindowSize/2, text="Congratulation, you found the exit".upper(), font="Times 18 bold", fill="black", width=BlockSize, justify=CENTER)
        # player = can.create_rectangle(PlayerPos[0]*BlockSize, PlayerPos[1]*BlockSize, (PlayerPos[0]+1)*BlockSize, (PlayerPos[1]+1)*BlockSize, fill="blue")


def GoRight(event):
    """
    Thread run when d button is pressed to right down in the maze
    """
    global player, txt, Exit
    if ([PlayerPos[0] + 1, PlayerPos[1]]) not in Walls :
        PlayerPos[0] += 1
        # can.delete(player)
        LocalRender(Map)
        if PlayerPos == Exit:
            can.create_text(WindowSize/2, WindowSize/2, text="Congratulation, you found the exit".upper(), font="Times 18 bold", fill="black", width=BlockSize, justify=CENTER)
        # player = can.create_rectangle(PlayerPos[0]*BlockSize, PlayerPos[1]*BlockSize, (PlayerPos[0]+1)*BlockSize, (PlayerPos[1]+1)*BlockSize, fill="blue")

# =========================FRONTEND=========================
root = Tk()
root.title("BigMapNav")

can = Canvas(root, width=WindowSize, height=WindowSize, bg="black")
root.bind("z", GoUp)
root.bind("s",GoDown)
root.bind("q", GoLeft)
root.bind("d",GoRight)
can.pack(padx=5, pady=5)

render(Map)
print(Exit)
LocalRender(Map)

root.mainloop()