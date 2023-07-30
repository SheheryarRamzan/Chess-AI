import copy

class Player:
    name:str #queen rokkie etc
    position:(int,int)
    isDead:bool
    firstMove:bool
    def __init__(self,name:str,pos:(int,int),isDead:bool=False):
        super().__init__()
        self.name = name
        self.position = pos
        self.isDead = isDead
        self.firstMove = True;

class WhiteTeam:
    #Small
    Team:Player = [
        Player("r",  (7,0)),
        Player("n",  (7,1)),
        Player("b",  (7,2)),
        Player("q",  (7,3)),
        Player("k",  (7,4)),
        Player("b",  (7,5)),
        Player("n",  (7,6)),
        Player("r",  (7,7)),

        Player("p",  (6,0)),
        Player("p",  (6,1)),
        Player("p",  (6,2)),
        Player("p",  (6,3)),
        Player("p",  (6,4)),
        Player("p",  (6,5)),
        Player("p",  (6,6)),
        Player("p",  (6,7)),
    ]

class BlackTeam:
    #Capital
    Team:Player = [
        Player("R",  (0,0)),
        Player("N",  (0,1)),
        Player("B",  (0,2)),
        Player("Q",  (0,3)),
        Player("K",  (0,4)),
        Player("B",  (0,5)),
        Player("N",  (0,6)),
        Player("R",  (0,7)),

        # Player("P",  (1,0)),
        Player("P",  (4,0)),

        Player("P",  (1,1)),
        Player("P",  (1,2)),
        Player("P",  (1,3)),
        Player("P",  (1,4)),
        Player("P",  (1,5)),
        Player("P",  (1,6)),
        Player("P",  (1,7)),
    ]

def getPlayerOnLocation(location:(int,int)) -> Player:
    for i in WhiteTeam.Team:
        if i.position == location:
            return i
    for i in BlackTeam.Team:
        if i.position == location:
            return i
    return None

def getPlayer(player:str) -> Player:
    for i in WhiteTeam.Team:
        if i.name == player:
            return i
    for i in BlackTeam.Team:
        if i.name == player:
            return i

Board = [ # 0 = white and 1 = black
    [0,1,0,1,0,1,0,1],
    [1,0,1,0,1,0,1,0],
    [0,1,0,1,0,1,0,1],
    [1,0,1,0,1,0,1,0],
    [0,1,0,1,0,1,0,1],
    [1,0,1,0,1,0,1,0],
    [0,1,0,1,0,1,0,1],
    [1,0,1,0,1,0,1,0]
]

def condition(saveLoc:(int,int)):
    var = getPlayerOnLocation(saveLoc)
    if var != None and turn == 'AI':
        if var.name == 'p' or var.name == 'r' or var.name == 'n' or var.name == 'b' or var.name == 'q' or var.name == 'k':
            return True
    if var != None and turn == 'User':
        if var.name == 'P' or var.name == 'R' or var.name == 'N' or var.name == 'B' or var.name == 'Q' or var.name == 'K':
            return True
    return False

def GetMoves(player):
    moves = []
    if player.name == 'R': # castelling on the first move with the king
        #check is LocationToMoveOn lies in its movement
        # print('Rook to be Moved')
        # forward (d) backward(u) leftwards(l) rightwards(r)
        saveLoc = player.position
        #d
        save_saveLoc = saveLoc
        # print('Downwards')
        while saveLoc[0] < len(Board):
            saveLoc = (saveLoc[0]+1,saveLoc[1])
            if getPlayerOnLocation(saveLoc) == None:
                # print(saveLoc)
                if (saveLoc[0] >=0 and saveLoc[0] < 8) and (saveLoc[1] >=0 and saveLoc[1] < 8):
                    moves.append(saveLoc)
            else:
                if condition(saveLoc):
                    moves.append(saveLoc)
                # print('--->' + str(saveLoc))
                break
            
        #u
        saveLoc = save_saveLoc
        # print('Upwards')
        while 0 <= saveLoc[0]:
            saveLoc = (saveLoc[0]-1,saveLoc[1])
            if getPlayerOnLocation(saveLoc) == None:
                # print(saveLoc)
                if (saveLoc[0] >=0 and saveLoc[0] < 8) and (saveLoc[1] >=0 and saveLoc[1] < 8):
                    moves.append(saveLoc)
            else:
                if condition(saveLoc):
                    moves.append(saveLoc)
                # print('--->' + str(saveLoc))
                break
        
        #r
        saveLoc = save_saveLoc
        # print('Rightwards')
        while saveLoc[1] < len(Board):
            saveLoc = (saveLoc[0],saveLoc[1]+1)
            if getPlayerOnLocation(saveLoc) == None:
                # print(saveLoc)
                if (saveLoc[0] >=0 and saveLoc[0] < 8) and (saveLoc[1] >=0 and saveLoc[1] < 8):
                    moves.append(saveLoc)
            else:
                if condition(saveLoc):
                    moves.append(saveLoc)
                # print('--->' + str(saveLoc))
                break
        
        #l
        saveLoc = save_saveLoc
        # print('leftwards')
        while 0 <= saveLoc[1]:
            saveLoc = (saveLoc[0],saveLoc[1]-1)
            if getPlayerOnLocation(saveLoc) == None:
                # print(saveLoc)
                if (saveLoc[0] >=0 and saveLoc[0] < 8) and (saveLoc[1] >=0 and saveLoc[1] < 8):
                    moves.append(saveLoc)
            else:
                if condition(saveLoc):
                    moves.append(saveLoc)
                # print('--->' + str(saveLoc))
                break

    if player.name == 'N':
        # print('Knight to be Moved')
        # L-shaped movement forward (d) backwards(u) left and right
        saveLoc = player.position
        
        #forward (D)
        saveLoc = (saveLoc[0]+2,saveLoc[1])
        saveLoc1 = (saveLoc[0],saveLoc[1]+1)
        if getPlayerOnLocation(saveLoc1) == None:
            # print('Forward R'+str(saveLoc1))
            if (saveLoc1[0] >=0 and saveLoc1[0] < 8) and (saveLoc1[1] >=0 and saveLoc1[1] < 8):
                moves.append(saveLoc1)
        else:
            if condition(saveLoc1):
                moves.append(saveLoc1)
        saveLoc2 = (saveLoc[0],saveLoc[1]-1)
        if getPlayerOnLocation(saveLoc2) == None:
            # print('Forward L'+str(saveLoc2))
            if (saveLoc2[0] >=0 and saveLoc2[0] < 8) and (saveLoc2[1] >=0 and saveLoc2[1] < 8):
                moves.append(saveLoc2)
        else:
            if condition(saveLoc2):
                moves.append(saveLoc2)
        saveLoc = player.position
        #backward (u)
        saveLoc = (saveLoc[0]-2,saveLoc[1])
        saveLoc1 = (saveLoc[0],saveLoc[1]+1)
        if getPlayerOnLocation(saveLoc1) == None:
            # print('Backward R'+str(saveLoc1))
            if (saveLoc1[0] >=0 and saveLoc1[0] < 8) and (saveLoc1[1] >=0 and saveLoc1[1] < 8):
                moves.append(saveLoc1)
        else:
            if condition(saveLoc1):
                moves.append(saveLoc1)
        saveLoc2 = (saveLoc[0],saveLoc[1]-1)
        if getPlayerOnLocation(saveLoc2) == None:
            # print('Backward L'+str(saveLoc2))
            if (saveLoc2[0] >=0 and saveLoc2[0] < 8) and (saveLoc2[1] >=0 and saveLoc2[1] < 8):
                moves.append(saveLoc2)
        else:
            if condition(saveLoc2):
                moves.append(saveLoc2)
        saveLoc = player.position
        #Rightward (r)
        saveLoc = (saveLoc[0],saveLoc[1]+2)
        saveLoc1 = (saveLoc[0]+1,saveLoc[1])
        if getPlayerOnLocation(saveLoc1) == None:
            # print('Right L'+str(saveLoc1))
            if (saveLoc1[0] >=0 and saveLoc1[0] < 8) and (saveLoc1[1] >=0 and saveLoc1[1] < 8):
                moves.append(saveLoc1)
        else:
            if condition(saveLoc1):
                moves.append(saveLoc1)
        saveLoc2 = (saveLoc[0]-1,saveLoc[1])
        if getPlayerOnLocation(saveLoc2) == None:
            # print('Right U'+str(saveLoc2))
            if (saveLoc2[0] >=0 and saveLoc2[0] < 8) and (saveLoc2[1] >=0 and saveLoc2[1] < 8):
                moves.append(saveLoc2)
        else:
            if condition(saveLoc2):
                moves.append(saveLoc2)
        saveLoc = player.position
        #Leftward (r)
        saveLoc = (saveLoc[0],saveLoc[1]-2)
        saveLoc1 = (saveLoc[0]+1,saveLoc[1])
        if getPlayerOnLocation(saveLoc1) == None:
            # print('Left L'+str(saveLoc1))
            if (saveLoc1[0] >=0 and saveLoc1[0] < 8) and (saveLoc1[1] >=0 and saveLoc1[1] < 8):
                moves.append(saveLoc1)
        else:
            if condition(saveLoc1):
                moves.append(saveLoc1)
        saveLoc2 = (saveLoc[0]-1,saveLoc[1])
        if getPlayerOnLocation(saveLoc2) == None:
            # print('Left U'+str(saveLoc2))
            if (saveLoc2[0] >=0 and saveLoc2[0] < 8) and (saveLoc2[1] >=0 and saveLoc2[1] < 8):
                moves.append(saveLoc2)
        else:
            if condition(saveLoc2):
                moves.append(saveLoc2)
    
    if player.name == 'B':
        # print('Bishop to be Moved')
        saveLoc = player.position
        #Downwards Right
        while saveLoc[0] < len(Board) and saveLoc[1] < len(Board):
            saveLoc = (saveLoc[0]+1,saveLoc[1]+1)
            if getPlayerOnLocation(saveLoc) == None:
                # print('DR ' +str(saveLoc))
                if (saveLoc[0] >=0 and saveLoc[0] < 8) and (saveLoc[1] >=0 and saveLoc[1] < 8):
                    moves.append(saveLoc)
            else:
                if condition(saveLoc):
                    moves.append(saveLoc)
                break
        #Upwards Left
        saveLoc = player.position
        while saveLoc[0] >= 0 and saveLoc[1] >= 0:
            saveLoc = (saveLoc[0]-1,saveLoc[1]-1)
            if getPlayerOnLocation(saveLoc) == None:
                # print('DR ' +str(saveLoc))
                if (saveLoc[0] >=0 and saveLoc[0] < 8) and (saveLoc[1] >=0 and saveLoc[1] < 8):
                    moves.append(saveLoc)
            else:
                if condition(saveLoc):
                    moves.append(saveLoc)
                break
        #Upwards Right
        saveLoc = player.position
        while saveLoc[0] >= 0 and saveLoc[1] < len(Board):
            saveLoc = (saveLoc[0]-1,saveLoc[1]+1)
            if getPlayerOnLocation(saveLoc) == None:
                # print('UR ' +str(saveLoc))
                if (saveLoc[0] >=0 and saveLoc[0] < 8) and (saveLoc[1] >=0 and saveLoc[1] < 8):
                    moves.append(saveLoc)
            else:
                if condition(saveLoc):
                    moves.append(saveLoc)
                break
        #Downwards Left
        saveLoc = player.position
        while (saveLoc[0] < len(Board) and saveLoc[1] >= 0):
            saveLoc = (saveLoc[0]+1,saveLoc[1]-1)
            if getPlayerOnLocation(saveLoc) == None:
                # print('UR ' +str(saveLoc))
                if (saveLoc[0] >=0 and saveLoc[0] < 8) and (saveLoc[1] >=0 and saveLoc[1] < 8):
                    moves.append(saveLoc)
            else:
                if condition(saveLoc):
                    moves.append(saveLoc)
                break

    if player.name == 'Q':
        # print('Queen to be Moved')
        saveLoc = player.position
        #Downwards Right
        while (saveLoc[0] < len(Board) and saveLoc[1] < len(Board)):
            saveLoc = (saveLoc[0]+1,saveLoc[1]+1)
            if getPlayerOnLocation(saveLoc) == None:
                # print('DR ' +str(saveLoc))
                if (saveLoc[0] >=0 and saveLoc[0] < 8) and (saveLoc[1] >=0 and saveLoc[1] < 8):
                    moves.append(saveLoc)
            else:
                if condition(saveLoc):
                    moves.append(saveLoc)
                break
        #Upwards Left
        saveLoc = player.position
        while saveLoc[0] >= 0 and saveLoc[1] >= 0:
            saveLoc = (saveLoc[0]-1,saveLoc[1]-1)
            if getPlayerOnLocation(saveLoc) == None:
                # print('DR ' +str(saveLoc))
                if (saveLoc[0] >=0 and saveLoc[0] < 8) and (saveLoc[1] >=0 and saveLoc[1] < 8):
                    moves.append(saveLoc)
            else:
                if condition(saveLoc):
                    moves.append(saveLoc)
                break
        #Upwards Right
        saveLoc = player.position
        while saveLoc[0] >= 0 and saveLoc[1] < len(Board):
            saveLoc = (saveLoc[0]-1,saveLoc[1]+1)
            if getPlayerOnLocation(saveLoc) == None:
                # print('UR ' +str(saveLoc))
                if (saveLoc[0] >=0 and saveLoc[0] < 8) and (saveLoc[1] >=0 and saveLoc[1] < 8):
                    moves.append(saveLoc)
            else:
                if condition(saveLoc):
                    moves.append(saveLoc)
                break
        #Downwards Left
        saveLoc = player.position
        while (saveLoc[0] < len(Board) and saveLoc[1] >= 0):
            saveLoc = (saveLoc[0]+1,saveLoc[1]-1)
            if getPlayerOnLocation(saveLoc) == None:
                # print('UR ' +str(saveLoc))
                if (saveLoc[0] >=0 and saveLoc[0] < 8) and (saveLoc[1] >=0 and saveLoc[1] < 8):
                    moves.append(saveLoc)
            else:
                if condition(saveLoc):
                    moves.append(saveLoc)
                break

        # forward (d) backward(u) leftwards(l) rightwards(r)
        saveLoc = player.position
        #d
        save_saveLoc = saveLoc
        # print('Downwards')
        while saveLoc[0] < len(Board):
            saveLoc = (saveLoc[0]+1,saveLoc[1])
            if getPlayerOnLocation(saveLoc) == None:
                # print(saveLoc)
                if (saveLoc[0] >=0 and saveLoc[0] < 8) and (saveLoc[1] >=0 and saveLoc[1] < 8):
                    moves.append(saveLoc)
            else:
                if condition(saveLoc):
                    moves.append(saveLoc)
                # print('--->' + str(saveLoc))
                break
            
        #u
        saveLoc = save_saveLoc
        # print('Upwards')
        while 0 <= saveLoc[0]:
            saveLoc = (saveLoc[0]-1,saveLoc[1])
            if getPlayerOnLocation(saveLoc) == None:
                # print(saveLoc)
                if (saveLoc[0] >=0 and saveLoc[0] < 8) and (saveLoc[1] >=0 and saveLoc[1] < 8):
                    moves.append(saveLoc)
            else:
                if condition(saveLoc):
                    moves.append(saveLoc)
                # print('--->' + str(saveLoc))
                break
        
        #r
        saveLoc = save_saveLoc
        # print('Rightwards')
        while saveLoc[1] < len(Board):
            saveLoc = (saveLoc[0],saveLoc[1]+1)
            if getPlayerOnLocation(saveLoc) == None:
                # print(saveLoc)
                if (saveLoc[0] >=0 and saveLoc[0] < 8) and (saveLoc[1] >=0 and saveLoc[1] < 8):
                    moves.append(saveLoc)
            else:
                if condition(saveLoc):
                    moves.append(saveLoc)
                # print('--->' + str(saveLoc))
                break
        
        #l
        saveLoc = save_saveLoc
        # print('leftwards')
        while 0 <= saveLoc[1]:
            saveLoc = (saveLoc[0],saveLoc[1]-1)
            if getPlayerOnLocation(saveLoc) == None:
                # print(saveLoc)
                if (saveLoc[0] >=0 and saveLoc[0] < 8) and (saveLoc[1] >=0 and saveLoc[1] < 8):
                    moves.append(saveLoc)
            else:
                if condition(saveLoc):
                    moves.append(saveLoc)
                # print('--->' + str(saveLoc))
                break

    if player.name == 'K':
        # print('King to be Moved')
        saveLoc = player.position
        #Downwards Right
        if(saveLoc[0] < len(Board) and saveLoc[1] < len(Board)):
            saveLoc = (saveLoc[0]+1,saveLoc[1]+1)
            if getPlayerOnLocation(saveLoc) == None:
                # print('DR ' +str(saveLoc))
                if (saveLoc[0] >=0 and saveLoc[0] < 8) and (saveLoc[1] >=0 and saveLoc[1] < 8):
                    moves.append(saveLoc) 
            else:
                if condition(saveLoc):
                    moves.append(saveLoc)           
        #Upwards Left
        saveLoc = player.position
        if saveLoc[0] >= 0 and saveLoc[1] >= 0:
            saveLoc = (saveLoc[0]-1,saveLoc[1]-1)
            if getPlayerOnLocation(saveLoc) == None:
                # print('DR ' +str(saveLoc))
                if (saveLoc[0] >=0 and saveLoc[0] < 8) and (saveLoc[1] >=0 and saveLoc[1] < 8):
                    moves.append(saveLoc)
            else:
                if condition(saveLoc):
                    moves.append(saveLoc)
        #Upwards Right
        saveLoc = player.position
        if saveLoc[0] >= 0 and saveLoc[1] < len(Board):
            saveLoc = (saveLoc[0]-1,saveLoc[1]+1)
            if getPlayerOnLocation(saveLoc) == None:
                # print('UR ' +str(saveLoc))
                if (saveLoc[0] >=0 and saveLoc[0] < 8) and (saveLoc[1] >=0 and saveLoc[1] < 8):
                    moves.append(saveLoc)
            else:
                if condition(saveLoc):
                    moves.append(saveLoc)
        #Downwards Left
        saveLoc = player.position
        if (saveLoc[0] < len(Board) and saveLoc[1] >= 0):
            saveLoc = (saveLoc[0]+1,saveLoc[1]-1)
            if getPlayerOnLocation(saveLoc) == None:
                # print('UR ' +str(saveLoc))
                if (saveLoc[0] >=0 and saveLoc[0] < 8) and (saveLoc[1] >=0 and saveLoc[1] < 8):
                    moves.append(saveLoc)
            else:
                if condition(saveLoc):
                    moves.append(saveLoc)
        # forward (d) backward(u) leftwards(l) rightwards(r)
        saveLoc = player.position
        #d
        save_saveLoc = saveLoc
        # print('Downwards')
        if saveLoc[0] < len(Board):
            saveLoc = (saveLoc[0]+1,saveLoc[1])
            if getPlayerOnLocation(saveLoc) == None:
                # print(saveLoc)
                if (saveLoc[0] >=0 and saveLoc[0] < 8) and (saveLoc[1] >=0 and saveLoc[1] < 8):
                    moves.append(saveLoc)
            else:
                if condition(saveLoc):
                    moves.append(saveLoc)
                # print('--->' + str(saveLoc))
            
        #u
        saveLoc = save_saveLoc
        # print('Upwards')
        if 0 <= saveLoc[0]:
            saveLoc = (saveLoc[0]-1,saveLoc[1])
            if getPlayerOnLocation(saveLoc) == None:
                # print(saveLoc)
                if (saveLoc[0] >=0 and saveLoc[0] < 8) and (saveLoc[1] >=0 and saveLoc[1] < 8):
                    moves.append(saveLoc)
            else:
                if condition(saveLoc):
                    moves.append(saveLoc)
                # print('--->' + str(saveLoc))
        
        #r
        saveLoc = save_saveLoc
        # print('Rightwards')
        if saveLoc[1] < len(Board):
            saveLoc = (saveLoc[0],saveLoc[1]+1)
            if getPlayerOnLocation(saveLoc) == None:
                # print(saveLoc)
                if (saveLoc[0] >=0 and saveLoc[0] < 8) and (saveLoc[1] >=0 and saveLoc[1] < 8):
                    moves.append(saveLoc)
            else:
                if condition(saveLoc):
                    moves.append(saveLoc)
                # print('--->' + str(saveLoc))
        
        #l
        saveLoc = save_saveLoc
        # print('leftwards')
        if 0 <= saveLoc[1]:
            saveLoc = (saveLoc[0],saveLoc[1]-1)
            if getPlayerOnLocation(saveLoc) == None:
                # print(saveLoc)
                if (saveLoc[0] >=0 and saveLoc[0] < 8) and (saveLoc[1] >=0 and saveLoc[1] < 8):
                    moves.append(saveLoc)
            else:
                if condition(saveLoc):
                    moves.append(saveLoc)
                # print('--->' + str(saveLoc))

    if player.name == 'P':
        # print('Pawn to be Moved')
        # forward (d) one step and two steps forwards if first time
        saveLoc = player.position
        #d
        save_saveLoc = saveLoc
        # print('Downwards')
        saveLoc = (saveLoc[0]+1,saveLoc[1])
        if getPlayerOnLocation(saveLoc) == None:
            # print(saveLoc)
            if (saveLoc[0] >=0 and saveLoc[0] < 8) and (saveLoc[1] >=0 and saveLoc[1] < 8):
                moves.append(saveLoc)
        else:
            if condition(saveLoc):
                moves.append(saveLoc)
            # print('--->' + str(saveLoc))

        saveLoc = (saveLoc[0]+1,saveLoc[1])
        if getPlayerOnLocation(saveLoc) == None and player.firstMove:
            # print(saveLoc)
            if (saveLoc[0] >=0 and saveLoc[0] < 8) and (saveLoc[1] >=0 and saveLoc[1] < 8):
                moves.append(saveLoc)
        else:
            if condition(saveLoc):
                    moves.append(saveLoc)
            # print('--->' + str(saveLoc))
        
    if player.name == 'r': # castelling on the first move with the king
        #check is LocationToMoveOn lies in its movement
        # print('rook to be Moved')
        # forward (d) backward(u) leftwards(l) rightwards(r)
        saveLoc = player.position
        #d
        save_saveLoc = saveLoc
        # print('Downwards')
        while saveLoc[0] < len(Board):
            saveLoc = (saveLoc[0]+1,saveLoc[1])
            if getPlayerOnLocation(saveLoc) == None:
                # print(saveLoc)
                if (saveLoc[0] >=0 and saveLoc[0] < 8) and (saveLoc[1] >=0 and saveLoc[1] < 8):
                    moves.append(saveLoc)
            else:
                if condition(saveLoc):
                    moves.append(saveLoc)
                # print('--->' + str(saveLoc))
                break
            
        #u
        saveLoc = save_saveLoc
        # print('Upwards')
        while 0 <= saveLoc[0]:
            saveLoc = (saveLoc[0]-1,saveLoc[1])
            if getPlayerOnLocation(saveLoc) == None:
                # print(saveLoc)
                if (saveLoc[0] >=0 and saveLoc[0] < 8) and (saveLoc[1] >=0 and saveLoc[1] < 8):
                    moves.append(saveLoc)
            else:
                if condition(saveLoc):
                    moves.append(saveLoc)
                # print('--->' + str(saveLoc))
                break
        
        #r
        saveLoc = save_saveLoc
        # print('Rightwards')
        while saveLoc[1] < len(Board):
            saveLoc = (saveLoc[0],saveLoc[1]+1)
            if getPlayerOnLocation(saveLoc) == None:
                # print(saveLoc)
                if (saveLoc[0] >=0 and saveLoc[0] < 8) and (saveLoc[1] >=0 and saveLoc[1] < 8):
                    moves.append(saveLoc)
            else:
                if condition(saveLoc):
                    moves.append(saveLoc)
                # print('--->' + str(saveLoc))
                break
        
        #l
        saveLoc = save_saveLoc
        # print('leftwards')
        while 0 <= saveLoc[1]:
            saveLoc = (saveLoc[0],saveLoc[1]-1)
            if getPlayerOnLocation(saveLoc) == None:
                # print(saveLoc)
                if (saveLoc[0] >=0 and saveLoc[0] < 8) and (saveLoc[1] >=0 and saveLoc[1] < 8):
                    moves.append(saveLoc)
            else:
                if condition(saveLoc):
                    moves.append(saveLoc)
                # print('--->' + str(saveLoc))
                break
        
    if player.name == 'n':
        # print('knight to be Moved')
        # L-shaped movement forward (d) backwards(u) left and right
        saveLoc = player.position
        
        #forward (D)
        saveLoc = (saveLoc[0]+2,saveLoc[1])
        saveLoc1 = (saveLoc[0],saveLoc[1]+1)
        if getPlayerOnLocation(saveLoc1) == None:
            # print('Forward R'+str(saveLoc1))
            if (saveLoc1[0] >=0 and saveLoc1[0] < 8) and (saveLoc1[1] >=0 and saveLoc1[1] < 8):
                moves.append(saveLoc1)
        else:
            if condition(saveLoc1):
                moves.append(saveLoc1)
        saveLoc2 = (saveLoc[0],saveLoc[1]-1)
        if getPlayerOnLocation(saveLoc2) == None:
            # print('Forward L'+str(saveLoc2))
            if (saveLoc2[0] >=0 and saveLoc2[0] < 8) and (saveLoc2[1] >=0 and saveLoc2[1] < 8):
                moves.append(saveLoc2)
        else:
            if condition(saveLoc2):
                    moves.append(saveLoc2)
        saveLoc = player.position
        #backward (u)
        saveLoc = (saveLoc[0]-2,saveLoc[1])
        saveLoc1 = (saveLoc[0],saveLoc[1]+1)
        if getPlayerOnLocation(saveLoc1) == None:
            # print('Backward R'+str(saveLoc1))
            if (saveLoc1[0] >=0 and saveLoc1[0] < 8) and (saveLoc1[1] >=0 and saveLoc1[1] < 8):
                moves.append(saveLoc1)
        else:
            if condition(saveLoc1):
                moves.append(saveLoc1)
        saveLoc2 = (saveLoc[0],saveLoc[1]-1)
        if getPlayerOnLocation(saveLoc2) == None:
            # print('Backward L'+str(saveLoc2))
            if (saveLoc2[0] >=0 and saveLoc2[0] < 8) and (saveLoc2[1] >=0 and saveLoc2[1] < 8):
                moves.append(saveLoc2)
        else:
            if condition(saveLoc2):
                moves.append(saveLoc2)
        saveLoc = player.position
        #Rightward (r)
        saveLoc = (saveLoc[0],saveLoc[1]+2)
        saveLoc1 = (saveLoc[0]+1,saveLoc[1])
        if getPlayerOnLocation(saveLoc1) == None:
            # print('Right L'+str(saveLoc1))
            if (saveLoc1[0] >=0 and saveLoc1[0] < 8) and (saveLoc1[1] >=0 and saveLoc1[1] < 8):
                moves.append(saveLoc1)
        else:
            if condition(saveLoc1):
                moves.append(saveLoc1)
        saveLoc2 = (saveLoc[0]-1,saveLoc[1])
        if getPlayerOnLocation(saveLoc2) == None:
            # print('Right U'+str(saveLoc2))
            if (saveLoc2[0] >=0 and saveLoc2[0] < 8) and (saveLoc2[1] >=0 and saveLoc2[1] < 8):
                moves.append(saveLoc2)
        else:
            if condition(saveLoc2):
                moves.append(saveLoc2)
        saveLoc = player.position
        #Leftward (r)
        saveLoc = (saveLoc[0],saveLoc[1]-2)
        saveLoc1 = (saveLoc[0]+1,saveLoc[1])
        if getPlayerOnLocation(saveLoc1) == None:
            # print('Left L'+str(saveLoc1))
            if (saveLoc1[0] >=0 and saveLoc1[0] < 8) and (saveLoc1[1] >=0 and saveLoc1[1] < 8):
                moves.append(saveLoc1)
        else:
            if condition(saveLoc1):
                moves.append(saveLoc1)
        saveLoc2 = (saveLoc[0]-1,saveLoc[1])
        if getPlayerOnLocation(saveLoc2) == None:
            # print('Left U'+str(saveLoc2))
            if (saveLoc2[0] >=0 and saveLoc2[0] < 8) and (saveLoc2[1] >=0 and saveLoc2[1] < 8):
                moves.append(saveLoc2)
        else:
            if condition(saveLoc2):
                moves.append(saveLoc2)
    
    if player.name == 'b':
        # print('bishop to be Moved')
        saveLoc = player.position
        #Downwards Right
        while saveLoc[0] < len(Board) and saveLoc[1] < len(Board):
            saveLoc = (saveLoc[0]+1,saveLoc[1]+1)
            if getPlayerOnLocation(saveLoc) == None:
                # print('DR ' +str(saveLoc))
                if (saveLoc[0] >=0 and saveLoc[0] < 8) and (saveLoc[1] >=0 and saveLoc[1] < 8):
                    moves.append(saveLoc)
            else:
                if condition(saveLoc):
                    moves.append(saveLoc)
                break
        #Upwards Left
        saveLoc = player.position
        while saveLoc[0] >= 0 and saveLoc[1] >= 0:
            saveLoc = (saveLoc[0]-1,saveLoc[1]-1)
            if getPlayerOnLocation(saveLoc) == None:
                # print('DR ' +str(saveLoc))
                if (saveLoc[0] >=0 and saveLoc[0] < 8) and (saveLoc[1] >=0 and saveLoc[1] < 8):
                    moves.append(saveLoc)
            else:
                if condition(saveLoc):
                    moves.append(saveLoc)
                break
        #Upwards Right
        saveLoc = player.position
        while saveLoc[0] >= 0 and saveLoc[1] < len(Board):
            saveLoc = (saveLoc[0]-1,saveLoc[1]+1)
            if getPlayerOnLocation(saveLoc) == None:
                # print('UR ' +str(saveLoc))
                if (saveLoc[0] >=0 and saveLoc[0] < 8) and (saveLoc[1] >=0 and saveLoc[1] < 8):
                    moves.append(saveLoc)
            else:
                if condition(saveLoc):
                    moves.append(saveLoc)
                break
        #Downwards Left
        saveLoc = player.position
        while (saveLoc[0] < len(Board) and saveLoc[1] >= 0):
            saveLoc = (saveLoc[0]+1,saveLoc[1]-1)
            if getPlayerOnLocation(saveLoc) == None:
                # print('UR ' +str(saveLoc))
                if (saveLoc[0] >=0 and saveLoc[0] < 8) and (saveLoc[1] >=0 and saveLoc[1] < 8):
                    moves.append(saveLoc)
            else:
                if condition(saveLoc):
                    moves.append(saveLoc)
                break
        
    if player.name == 'q':
        # print('queen to be Moved')
        saveLoc = player.position
        #Downwards Right
        while(saveLoc[0] < len(Board) and saveLoc[1] < len(Board)):
            saveLoc = (saveLoc[0]+1,saveLoc[1]+1)
            if getPlayerOnLocation(saveLoc) == None:
                # print('DR ' +str(saveLoc))
                if (saveLoc[0] >=0 and saveLoc[0] < 8) and (saveLoc[1] >=0 and saveLoc[1] < 8):
                    moves.append(saveLoc)
            else:
                if condition(saveLoc):
                    moves.append(saveLoc)
                break
        #Upwards Left
        saveLoc = player.position
        while saveLoc[0] >= 0 and saveLoc[1] >= 0:
            saveLoc = (saveLoc[0]-1,saveLoc[1]-1)
            if getPlayerOnLocation(saveLoc) == None:
                # print('DR ' +str(saveLoc))
                if (saveLoc[0] >=0 and saveLoc[0] < 8) and (saveLoc[1] >=0 and saveLoc[1] < 8):
                    moves.append(saveLoc)
            else:
                if condition(saveLoc):
                    moves.append(saveLoc)
                break
        #Upwards Right
        saveLoc = player.position
        while saveLoc[0] >= 0 and saveLoc[1] < len(Board):
            saveLoc = (saveLoc[0]-1,saveLoc[1]+1)
            if getPlayerOnLocation(saveLoc) == None:
                # print('UR ' +str(saveLoc))
                if (saveLoc[0] >=0 and saveLoc[0] < 8) and (saveLoc[1] >=0 and saveLoc[1] < 8):
                    moves.append(saveLoc)
            else:
                if condition(saveLoc):
                    moves.append(saveLoc)
                break
        #Downwards Left
        saveLoc = player.position
        while (saveLoc[0] < len(Board) and saveLoc[1] >= 0):
            saveLoc = (saveLoc[0]+1,saveLoc[1]-1)
            if getPlayerOnLocation(saveLoc) == None:
                # print('UR ' +str(saveLoc))
                if (saveLoc[0] >=0 and saveLoc[0] < 8) and (saveLoc[1] >=0 and saveLoc[1] < 8):
                    moves.append(saveLoc)
            else:
                if condition(saveLoc):
                    moves.append(saveLoc)
                break

        # forward (d) backward(u) leftwards(l) rightwards(r)
        saveLoc = player.position
        #d
        save_saveLoc = saveLoc
        # print('Downwards')
        while saveLoc[0] < len(Board):
            saveLoc = (saveLoc[0]+1,saveLoc[1])
            if getPlayerOnLocation(saveLoc) == None:
                # print(saveLoc)
                if (saveLoc[0] >=0 and saveLoc[0] < 8) and (saveLoc[1] >=0 and saveLoc[1] < 8):
                    moves.append(saveLoc)
            else:
                if condition(saveLoc):
                    moves.append(saveLoc)
                # print('--->' + str(saveLoc))
                break
            
        #u
        saveLoc = save_saveLoc
        # print('Upwards')
        while 0 <= saveLoc[0]:
            saveLoc = (saveLoc[0]-1,saveLoc[1])
            if getPlayerOnLocation(saveLoc) == None:
                # print(saveLoc)
                if (saveLoc[0] >=0 and saveLoc[0] < 8) and (saveLoc[1] >=0 and saveLoc[1] < 8):
                    moves.append(saveLoc)
            else:
                if condition(saveLoc):
                    moves.append(saveLoc)
                # print('--->' + str(saveLoc))
                break
        
        #r
        saveLoc = save_saveLoc
        # print('Rightwards')
        while saveLoc[1] < len(Board):
            saveLoc = (saveLoc[0],saveLoc[1]+1)
            if getPlayerOnLocation(saveLoc) == None:
                # print(saveLoc)
                if (saveLoc[0] >=0 and saveLoc[0] < 8) and (saveLoc[1] >=0 and saveLoc[1] < 8):
                    moves.append(saveLoc)
            else:
                if condition(saveLoc):
                    moves.append(saveLoc)
                # print('--->' + str(saveLoc))
                break
        
        #l
        saveLoc = save_saveLoc
        # print('leftwards')
        while 0 <= saveLoc[1]:
            saveLoc = (saveLoc[0],saveLoc[1]-1)
            if getPlayerOnLocation(saveLoc) == None:
                # print(saveLoc)
                if (saveLoc[0] >=0 and saveLoc[0] < 8) and (saveLoc[1] >=0 and saveLoc[1] < 8):
                    moves.append(saveLoc)
            else:
                if condition(saveLoc):
                    moves.append(saveLoc)
                # print('--->' + str(saveLoc))
                break

    if player.name == 'k':
        # print('king to be Moved')
        saveLoc = player.position
        #Downwards Right
        if (saveLoc[0] < len(Board) and saveLoc[1] < len(Board)):
            saveLoc = (saveLoc[0]+1,saveLoc[1]+1)
            if getPlayerOnLocation(saveLoc) == None:
                # print('DR ' +str(saveLoc))
                if (saveLoc[0] >=0 and saveLoc[0] < 8) and (saveLoc[1] >=0 and saveLoc[1] < 8):
                    moves.append(saveLoc)
            else:
                if condition(saveLoc):
                    moves.append(saveLoc)
        #Upwards Left
        saveLoc = player.position
        if saveLoc[0] >= 0 and saveLoc[1] >= 0:
            saveLoc = (saveLoc[0]-1,saveLoc[1]-1)
            if getPlayerOnLocation(saveLoc) == None:
                # print('DR ' +str(saveLoc))
                if (saveLoc[0] >=0 and saveLoc[0] < 8) and (saveLoc[1] >=0 and saveLoc[1] < 8):
                    moves.append(saveLoc)
            else:
                if condition(saveLoc):
                    moves.append(saveLoc)
        #Upwards Right
        saveLoc = player.position
        if saveLoc[0] >= 0 and saveLoc[1] < len(Board):
            saveLoc = (saveLoc[0]-1,saveLoc[1]+1)
            if getPlayerOnLocation(saveLoc) == None:
                # print('UR ' +str(saveLoc))
                if (saveLoc[0] >=0 and saveLoc[0] < 8) and (saveLoc[1] >=0 and saveLoc[1] < 8):
                    moves.append(saveLoc)
            else:
                if condition(saveLoc):
                    moves.append(saveLoc)        
        #Downwards Left
        saveLoc = player.position
        if (saveLoc[0] < len(Board) and saveLoc[1] >= 0):
            saveLoc = (saveLoc[0]+1,saveLoc[1]-1)
            if getPlayerOnLocation(saveLoc) == None:
                # print('UR ' +str(saveLoc))
                if (saveLoc[0] >=0 and saveLoc[0] < 8) and (saveLoc[1] >=0 and saveLoc[1] < 8):
                    moves.append(saveLoc)
            else:
                if condition(saveLoc):
                    moves.append(saveLoc)
        # forward (d) backward(u) leftwards(l) rightwards(r)
        saveLoc = player.position
        #d
        save_saveLoc = saveLoc
        # print('Downwards')
        if saveLoc[0] < len(Board):
            saveLoc = (saveLoc[0]+1,saveLoc[1])
            if getPlayerOnLocation(saveLoc) == None:
                # print(saveLoc)
                if (saveLoc[0] >=0 and saveLoc[0] < 8) and (saveLoc[1] >=0 and saveLoc[1] < 8):
                    moves.append(saveLoc)
            else:
                if condition(saveLoc):
                    moves.append(saveLoc)
                # print('--->' + str(saveLoc))
            
        #u
        saveLoc = save_saveLoc
        # print('Upwards')
        if 0 <= saveLoc[0]:
            saveLoc = (saveLoc[0]-1,saveLoc[1])
            if getPlayerOnLocation(saveLoc) == None:
                # print(saveLoc)
                if (saveLoc[0] >=0 and saveLoc[0] < 8) and (saveLoc[1] >=0 and saveLoc[1] < 8):
                    moves.append(saveLoc)
            else:
                if condition(saveLoc):
                    moves.append(saveLoc)
                # print('--->' + str(saveLoc))
        
        #r
        saveLoc = save_saveLoc
        # print('Rightwards')
        if saveLoc[1] < len(Board):
            saveLoc = (saveLoc[0],saveLoc[1]+1)
            if getPlayerOnLocation(saveLoc) == None:
                # print(saveLoc)
                if (saveLoc[0] >=0 and saveLoc[0] < 8) and (saveLoc[1] >=0 and saveLoc[1] < 8):
                    moves.append(saveLoc)
            else:
                if condition(saveLoc):
                    moves.append(saveLoc)
                # print('--->' + str(saveLoc))
        
        #l
        saveLoc = save_saveLoc
        # print('leftwards')
        if 0 <= saveLoc[1]:
            saveLoc = (saveLoc[0],saveLoc[1]-1)
            if getPlayerOnLocation(saveLoc) == None:
                # print(saveLoc)
                if (saveLoc[0] >=0 and saveLoc[0] < 8) and (saveLoc[1] >=0 and saveLoc[1] < 8):
                    moves.append(saveLoc)
            else:
                if condition(saveLoc):
                    moves.append(saveLoc)
                # print('--->' + str(saveLoc))

    if player.name == 'p':
        # print('pawn to be Moved')
        # forward (d) one step and two steps forwards if first time
        saveLoc = player.position
        #d
        save_saveLoc = saveLoc
        # print('Downwards')
        saveLoc = (saveLoc[0]-1,saveLoc[1])
        if getPlayerOnLocation(saveLoc) == None:
            # print(saveLoc)
            if (saveLoc[0] >=0 and saveLoc[0] < 8) and (saveLoc[1] >=0 and saveLoc[1] < 8):
                moves.append(saveLoc)
        else:
            if condition(saveLoc):
                moves.append(saveLoc)
            # print('--->' + str(saveLoc))

        saveLoc = (saveLoc[0]-1,saveLoc[1])
        if getPlayerOnLocation(saveLoc) == None and player.firstMove:
            # print(saveLoc)
            if (saveLoc[0] >=0 and saveLoc[0] < 8) and (saveLoc[1] >=0 and saveLoc[1] < 8):
                moves.append(saveLoc)
        else:
            if condition(saveLoc):
                moves.append(saveLoc)
            # print('--->' + str(saveLoc))
    return moves

def Move(locationToMoveFrom:(int,int),locationToMoveOn:(int,int)):
    # in case there is already a player on the tile
    # result = getPlayerOnLocation((locationToMoveOn[0],locationToMoveOn[1]))
    # if result != None:
    #     return
    # If you can move on a tile
    MovePlayer(getPlayerOnLocation(locationToMoveFrom),locationToMoveOn)

def MovePlayer(player:Player,new_location:(int,int)):
    foundLoc:bool = False
    if player.name == 'R': # castelling on the first move with the king
        #check is LocationToMoveOn lies in its movement
        # print('Rook to be Moved')
        # forward (d) backward(u) leftwards(l) rightwards(r)
        saveLoc = player.position
        #d
        save_saveLoc = saveLoc
        # print('Downwards')
        while saveLoc[0] < len(Board) and not foundLoc:
            saveLoc = (saveLoc[0]+1,saveLoc[1])
            if getPlayerOnLocation(saveLoc) == None:
                # print(saveLoc)
                if new_location == saveLoc:
                    # print('Can Do the Move')
                    foundLoc = True
            else:
                # print('--->' + str(saveLoc))
                if condition(saveLoc):
                    if new_location == saveLoc:
                    # print('Can Do the Move')
                        foundLoc = True
                break
            
        #u
        saveLoc = save_saveLoc
        # print('Upwards')
        while 0 <= saveLoc[0] and not foundLoc:
            saveLoc = (saveLoc[0]-1,saveLoc[1])
            if getPlayerOnLocation(saveLoc) == None:
                # print(saveLoc)
                if new_location == saveLoc:
                    # print('Can Do the Move')
                    foundLoc = True
            else:
                if condition(saveLoc):
                    if new_location == saveLoc:
                    # print('Can Do the Move')
                        foundLoc = True
                # print('--->' + str(saveLoc))
                break
        
        #r
        saveLoc = save_saveLoc
        # print('Rightwards')
        while saveLoc[1] < len(Board) and not foundLoc:
            saveLoc = (saveLoc[0],saveLoc[1]+1)
            if getPlayerOnLocation(saveLoc) == None:
                # print(saveLoc)
                if new_location == saveLoc:
                    # print('Can Do the Move')
                    foundLoc = True
            else:
                if condition(saveLoc):
                    if new_location == saveLoc:
                    # print('Can Do the Move')
                        foundLoc = True
                # print('--->' + str(saveLoc))
                break
        
        #l
        saveLoc = save_saveLoc
        # print('leftwards')
        while 0 <= saveLoc[1] and not foundLoc:
            saveLoc = (saveLoc[0],saveLoc[1]-1)
            if getPlayerOnLocation(saveLoc) == None:
                # print(saveLoc)
                if new_location == saveLoc:
                    # print('Can Do the Move')
                    foundLoc = True
            else:
                if condition(saveLoc):
                    if new_location == saveLoc:
                    # print('Can Do the Move')
                        foundLoc = True
                # print('--->' + str(saveLoc))
                break
        
        if foundLoc:
            foundLoc = False
            player.firstMove = False
            if getPlayerOnLocation(new_location) != None:
                getPlayerOnLocation(new_location).isDead = True
                getPlayerOnLocation(new_location).position = (-1,-1)
            player.position = new_location

    if player.name == 'N':
        # print('Knight to be Moved')
        # L-shaped movement forward (d) backwards(u) left and right
        saveLoc = player.position
        
        #forward (D)
        saveLoc = (saveLoc[0]+2,saveLoc[1])
        saveLoc1 = (saveLoc[0],saveLoc[1]+1)
        if saveLoc1 == new_location:
            if getPlayerOnLocation(saveLoc1) == None:
                foundLoc = True
            else:
                if condition(saveLoc1):
                    foundLoc = True
                # print('Forward R'+str(saveLoc1))
        saveLoc2 = (saveLoc[0],saveLoc[1]-1)
        if saveLoc2 == new_location and not foundLoc:
            if getPlayerOnLocation(saveLoc2) == None:
                foundLoc = True
                # print('Forward L'+str(saveLoc2))
            else:
                if condition(saveLoc2):
                    foundLoc = True
        saveLoc = player.position
        #backward (u)
        saveLoc = (saveLoc[0]-2,saveLoc[1])
        saveLoc1 = (saveLoc[0],saveLoc[1]+1)
        if saveLoc1 == new_location and not foundLoc:
            if getPlayerOnLocation(saveLoc1) == None:
                foundLoc = True
                # print('Backward R'+str(saveLoc1))
            else:
                if condition(saveLoc1):
                    foundLoc = True
        saveLoc2 = (saveLoc[0],saveLoc[1]-1)
        if saveLoc2 == new_location and not foundLoc:
            if getPlayerOnLocation(saveLoc2) == None:
                foundLoc = True
                # print('Backward L'+str(saveLoc2))
            else:
                if condition(saveLoc2):
                    foundLoc = True
        saveLoc = player.position
        #Rightward (r)
        saveLoc = (saveLoc[0],saveLoc[1]+2)
        saveLoc1 = (saveLoc[0]+1,saveLoc[1])
        if saveLoc1 == new_location and not foundLoc:
            if getPlayerOnLocation(saveLoc1) == None:
                foundLoc = True
            else:
                if condition(saveLoc1):
                    foundLoc = True
                # print('Right L'+str(saveLoc1))
        saveLoc2 = (saveLoc[0]-1,saveLoc[1])
        if saveLoc2 == new_location and not foundLoc:
            if getPlayerOnLocation(saveLoc2) == None:
                foundLoc = True
                # print('Right U'+str(saveLoc2))
            else:
                if condition(saveLoc2):
                    foundLoc = True
        saveLoc = player.position
        #Leftward (r)
        saveLoc = (saveLoc[0],saveLoc[1]-2)
        saveLoc1 = (saveLoc[0]+1,saveLoc[1])
        if saveLoc1 == new_location and not foundLoc:
            if getPlayerOnLocation(saveLoc1) == None:
                foundLoc = True
                # print('Left L'+str(saveLoc1))
            else:
                if condition(saveLoc1):
                    foundLoc = True
        saveLoc2 = (saveLoc[0]-1,saveLoc[1])
        if saveLoc2 == new_location and not foundLoc:
            if getPlayerOnLocation(saveLoc2) == None:
                foundLoc = True
                # print('Left U'+str(saveLoc2))
            else:
                if condition(saveLoc2):
                    foundLoc = True
        if foundLoc:
            foundLoc = False
            player.firstMove = False
            if getPlayerOnLocation(new_location) != None:
                getPlayerOnLocation(new_location).isDead = True
                getPlayerOnLocation(new_location).position = (-1,-1)
            player.position = new_location

    if player.name == 'B':
        # print('Bishop to be Moved')
        saveLoc = player.position
        #Downwards Right
        while saveLoc[0] < len(Board) and saveLoc[1] < len(Board):
            saveLoc = (saveLoc[0]+1,saveLoc[1]+1)
            if getPlayerOnLocation(saveLoc) == None:
                if saveLoc == new_location:
                    foundLoc = True
                    # print('DR ' +str(saveLoc))
            else:
                if condition(saveLoc):
                    if saveLoc == new_location:
                        foundLoc = True
                break
        #Upwards Left
        saveLoc = player.position
        while not foundLoc and saveLoc[0] >= 0 and saveLoc[1] >= 0:
            saveLoc = (saveLoc[0]-1,saveLoc[1]-1)
            if getPlayerOnLocation(saveLoc) == None:
                if saveLoc == new_location:
                    foundLoc = True
                    # print('DR ' +str(saveLoc))
            else:
                if condition(saveLoc):
                    if saveLoc == new_location:
                        foundLoc = True
                break
        #Upwards Right
        saveLoc = player.position
        while not foundLoc and saveLoc[0] >= 0 and saveLoc[1] < len(Board):
            saveLoc = (saveLoc[0]-1,saveLoc[1]+1)
            if getPlayerOnLocation(saveLoc) == None:
                if saveLoc == new_location:
                    foundLoc = True
                    # print('UR ' +str(saveLoc))
            else:
                if condition(saveLoc):
                    if saveLoc == new_location:
                        foundLoc = True
                break
        #Downwards Left
        saveLoc = player.position
        while not foundLoc and (saveLoc[0] < len(Board) and saveLoc[1] >= 0):
            saveLoc = (saveLoc[0]+1,saveLoc[1]-1)
            if getPlayerOnLocation(saveLoc) == None:
                if saveLoc == new_location:
                    foundLoc = True
                    # print('UR ' +str(saveLoc))
            else:
                if condition(saveLoc):
                    if saveLoc == new_location:
                        foundLoc = True
                break
        if foundLoc:
            foundLoc = False
            player.firstMove = False
            if getPlayerOnLocation(new_location) != None:
                getPlayerOnLocation(new_location).isDead = True
                getPlayerOnLocation(new_location).position = (-1,-1)
            player.position = new_location

    if player.name == 'Q':
        # print('Queen to be Moved')
        saveLoc = player.position
        #Downwards Right
        while not foundLoc and (saveLoc[0] < len(Board) and saveLoc[1] < len(Board)):
            saveLoc = (saveLoc[0]+1,saveLoc[1]+1)
            if getPlayerOnLocation(saveLoc) == None:
                if saveLoc == new_location:
                    foundLoc = True
                    # print('DR ' +str(saveLoc))
            else:
                if condition(saveLoc):
                    if saveLoc == new_location:
                        foundLoc = True
                break
        #Upwards Left
        saveLoc = player.position
        while not foundLoc and saveLoc[0] >= 0 and saveLoc[1] >= 0:
            saveLoc = (saveLoc[0]-1,saveLoc[1]-1)
            if getPlayerOnLocation(saveLoc) == None:
                if saveLoc == new_location:
                    foundLoc = True
                    # print('DR ' +str(saveLoc))
            else:
                if condition(saveLoc):
                    if saveLoc == new_location:
                        foundLoc = True
                break
        #Upwards Right
        saveLoc = player.position
        while not foundLoc and saveLoc[0] >= 0 and saveLoc[1] < len(Board):
            saveLoc = (saveLoc[0]-1,saveLoc[1]+1)
            if getPlayerOnLocation(saveLoc) == None:
                if saveLoc == new_location:
                    foundLoc = True
                    # print('UR ' +str(saveLoc))
            else:
                if condition(saveLoc):
                    if saveLoc == new_location:
                        foundLoc = True
                break
        #Downwards Left
        saveLoc = player.position
        while not foundLoc and (saveLoc[0] < len(Board) and saveLoc[1] >= 0):
            saveLoc = (saveLoc[0]+1,saveLoc[1]-1)
            if getPlayerOnLocation(saveLoc) == None:
                if saveLoc == new_location:
                    foundLoc = True
                    # print('UR ' +str(saveLoc))
            else:
                if condition(saveLoc):
                    if saveLoc == new_location:
                        foundLoc = True
                break

        # forward (d) backward(u) leftwards(l) rightwards(r)
        saveLoc = player.position
        #d
        save_saveLoc = saveLoc
        # print('Downwards')
        while saveLoc[0] < len(Board) and not foundLoc:
            saveLoc = (saveLoc[0]+1,saveLoc[1])
            if getPlayerOnLocation(saveLoc) == None:
                # print(saveLoc)
                if new_location == saveLoc:
                    # print('Can Do the Move')
                    foundLoc = True
            else:
                if condition(saveLoc):
                    if new_location == saveLoc:
                        # print('Can Do the Move')
                        foundLoc = True
                # print('--->' + str(saveLoc))
                break
            
        #u
        saveLoc = save_saveLoc
        # print('Upwards')
        while 0 <= saveLoc[0] and not foundLoc:
            saveLoc = (saveLoc[0]-1,saveLoc[1])
            if getPlayerOnLocation(saveLoc) == None:
                # print(saveLoc)
                if new_location == saveLoc:
                    # print('Can Do the Move')
                    foundLoc = True
            else:
                if condition(saveLoc):
                    if new_location == saveLoc:
                        # print('Can Do the Move')
                        foundLoc = True
                # print('--->' + str(saveLoc))
                break
        
        #r
        saveLoc = save_saveLoc
        # print('Rightwards')
        while saveLoc[1] < len(Board) and not foundLoc:
            saveLoc = (saveLoc[0],saveLoc[1]+1)
            if getPlayerOnLocation(saveLoc) == None:
                # print(saveLoc)
                if new_location == saveLoc:
                    # print('Can Do the Move')
                    foundLoc = True
            else:
                if condition(saveLoc):
                    if new_location == saveLoc:
                        # print('Can Do the Move')
                        foundLoc = True
                # print('--->' + str(saveLoc))
                break
        
        #l
        saveLoc = save_saveLoc
        # print('leftwards')
        while 0 <= saveLoc[1] and not foundLoc:
            saveLoc = (saveLoc[0],saveLoc[1]-1)
            if getPlayerOnLocation(saveLoc) == None:
                # print(saveLoc)
                if new_location == saveLoc:
                    # print('Can Do the Move')
                    foundLoc = True
            else:
                if condition(saveLoc):
                    if new_location == saveLoc:
                        # print('Can Do the Move')
                        foundLoc = True
                # print('--->' + str(saveLoc))
                break

        if foundLoc:
            foundLoc = False
            player.firstMove = False
            if getPlayerOnLocation(new_location) != None:
                getPlayerOnLocation(new_location).isDead = True
                getPlayerOnLocation(new_location).position = (-1,-1)
            player.position = new_location

    if player.name == 'K':
        # print('King to be Moved')
        saveLoc = player.position
        #Downwards Right
        if not foundLoc and (saveLoc[0] < len(Board) and saveLoc[1] < len(Board)):
            saveLoc = (saveLoc[0]+1,saveLoc[1]+1)
            if getPlayerOnLocation(saveLoc) == None:
                if saveLoc == new_location:
                    foundLoc = True
            else:
                if condition(saveLoc):
                    if saveLoc == new_location:
                        foundLoc = True
                    # print('DR ' +str(saveLoc))
            
        #Upwards Left
        saveLoc = player.position
        if not foundLoc and saveLoc[0] >= 0 and saveLoc[1] >= 0:
            saveLoc = (saveLoc[0]-1,saveLoc[1]-1)
            if getPlayerOnLocation(saveLoc) == None:
                if saveLoc == new_location:
                    foundLoc = True
                    # print('DR ' +str(saveLoc))
            else:
                if condition(saveLoc):
                    if saveLoc == new_location:
                        foundLoc = True
        #Upwards Right
        saveLoc = player.position
        if not foundLoc and saveLoc[0] >= 0 and saveLoc[1] < len(Board):
            saveLoc = (saveLoc[0]-1,saveLoc[1]+1)
            if getPlayerOnLocation(saveLoc) == None:
                if saveLoc == new_location:
                    foundLoc = True
                    # print('UR ' +str(saveLoc))
            else:
                if condition(saveLoc):
                    if saveLoc == new_location:
                        foundLoc = True
        #Downwards Left
        saveLoc = player.position
        if not foundLoc and (saveLoc[0] < len(Board) and saveLoc[1] >= 0):
            saveLoc = (saveLoc[0]+1,saveLoc[1]-1)
            if getPlayerOnLocation(saveLoc) == None:
                if saveLoc == new_location:
                    foundLoc = True
                    # print('UR ' +str(saveLoc))
            else:   
                if condition(saveLoc):
                    pass
        # forward (d) backward(u) leftwards(l) rightwards(r)
        saveLoc = player.position
        #d
        save_saveLoc = saveLoc
        # print('Downwards')
        if saveLoc[0] < len(Board) and not foundLoc:
            saveLoc = (saveLoc[0]+1,saveLoc[1])
            if getPlayerOnLocation(saveLoc) == None:
                # print(saveLoc)
                if new_location == saveLoc:
                    # print('Can Do the Move')
                    foundLoc = True
            else:
                if condition(saveLoc):
                    if new_location == saveLoc:
                        # print('Can Do the Move')
                        foundLoc = True
                # print('--->' + str(saveLoc))
            
        #u
        saveLoc = save_saveLoc
        # print('Upwards')
        if 0 <= saveLoc[0] and not foundLoc:
            saveLoc = (saveLoc[0]-1,saveLoc[1])
            if getPlayerOnLocation(saveLoc) == None:
                # print(saveLoc)
                if new_location == saveLoc:
                    # print('Can Do the Move')
                    foundLoc = True
            else:
                if condition(saveLoc):
                    if new_location == saveLoc:
                        # print('Can Do the Move')
                        foundLoc = True
                # print('--->' + str(saveLoc))
        
        #r
        saveLoc = save_saveLoc
        # print('Rightwards')
        if saveLoc[1] < len(Board) and not foundLoc:
            saveLoc = (saveLoc[0],saveLoc[1]+1)
            if getPlayerOnLocation(saveLoc) == None:
                # print(saveLoc)
                if new_location == saveLoc:
                    # print('Can Do the Move')
                    foundLoc = True
            else:
                if condition(saveLoc):
                    if new_location == saveLoc:
                        # print('Can Do the Move')
                        foundLoc = True
                # print('--->' + str(saveLoc))
        
        #l
        saveLoc = save_saveLoc
        # print('leftwards')
        if 0 <= saveLoc[1] and not foundLoc:
            saveLoc = (saveLoc[0],saveLoc[1]-1)
            if getPlayerOnLocation(saveLoc) == None:
                # print(saveLoc)
                if new_location == saveLoc:
                    # print('Can Do the Move')
                    foundLoc = True
            else:
                if condition(saveLoc):
                    if new_location == saveLoc:
                        # print('Can Do the Move')
                        foundLoc = True
                # print('--->' + str(saveLoc))

        if foundLoc:
            foundLoc = False
            player.firstMove = False
            if getPlayerOnLocation(new_location) != None:
                getPlayerOnLocation(new_location).isDead = True
                getPlayerOnLocation(new_location).position = (-1,-1)
            player.position = new_location

    if player.name == 'P':
        # print('Pawn to be Moved')
        # forward (d) one step and two steps forwards if first time
        saveLoc = player.position
        #d
        save_saveLoc = saveLoc
        # print('Downwards')
        saveLoc = (saveLoc[0]+1,saveLoc[1])
        if getPlayerOnLocation(saveLoc) == None:
            # print(saveLoc)
            if new_location == saveLoc:
                # print('Can Do the Move')
                foundLoc = True
        else:
            if condition(saveLoc):
                if new_location == saveLoc:
                    # print('Can Do the Move')
                    foundLoc = True
            # print('--->' + str(saveLoc))

        saveLoc = (saveLoc[0]+1,saveLoc[1])
        if getPlayerOnLocation(saveLoc) == None and player.firstMove:
            # print(saveLoc)
            if new_location == saveLoc:
                # print('Can Do the Move')
                foundLoc = True
        else:
            if condition(saveLoc):
                if new_location == saveLoc:
                    # print('Can Do the Move')
                    foundLoc = True
            # print('--->' + str(saveLoc))
        
        if foundLoc:
            foundLoc = False
            player.firstMove = False
            if getPlayerOnLocation(new_location) != None:
                getPlayerOnLocation(new_location).isDead = True
                getPlayerOnLocation(new_location).position = (-1,-1)
            player.position = new_location

    if player.name == 'r': # castelling on the first move with the king
        #check is LocationToMoveOn lies in its movement
        # print('rook to be Moved')
        # forward (d) backward(u) leftwards(l) rightwards(r)
        saveLoc = player.position
        #d
        save_saveLoc = saveLoc
        # print('Downwards')
        while saveLoc[0] < len(Board) and not foundLoc:
            saveLoc = (saveLoc[0]+1,saveLoc[1])
            if getPlayerOnLocation(saveLoc) == None:
                # print(saveLoc)
                if new_location == saveLoc:
                    # print('Can Do the Move')
                    foundLoc = True
            else:
                if condition(saveLoc):
                    if new_location == saveLoc:
                        # print('Can Do the Move')
                        foundLoc = True
                # print('--->' + str(saveLoc))
                break
            
        #u
        saveLoc = save_saveLoc
        # print('Upwards')
        while 0 <= saveLoc[0] and not foundLoc:
            saveLoc = (saveLoc[0]-1,saveLoc[1])
            if getPlayerOnLocation(saveLoc) == None:
                # print(saveLoc)
                if new_location == saveLoc:
                    # print('Can Do the Move')
                    foundLoc = True
            else:
                if condition(saveLoc):
                    if new_location == saveLoc:
                        # print('Can Do the Move')
                        foundLoc = True
                # print('--->' + str(saveLoc))
                break
        
        #r
        saveLoc = save_saveLoc
        # print('Rightwards')
        while saveLoc[1] < len(Board) and not foundLoc:
            saveLoc = (saveLoc[0],saveLoc[1]+1)
            if getPlayerOnLocation(saveLoc) == None:
                # print(saveLoc)
                if new_location == saveLoc:
                    # print('Can Do the Move')
                    foundLoc = True
            else:
                if condition(saveLoc):
                    if new_location == saveLoc:
                        # print('Can Do the Move')
                        foundLoc = True
                # print('--->' + str(saveLoc))
                break
        
        #l
        saveLoc = save_saveLoc
        # print('leftwards')
        while 0 <= saveLoc[1] and not foundLoc:
            saveLoc = (saveLoc[0],saveLoc[1]-1)
            if getPlayerOnLocation(saveLoc) == None:
                # print(saveLoc)
                if new_location == saveLoc:
                    # print('Can Do the Move')
                    foundLoc = True
            else:
                if condition(saveLoc):
                    if new_location == saveLoc:
                        # print('Can Do the Move')
                        foundLoc = True
                # print('--->' + str(saveLoc))
                break
        
        if foundLoc:
            foundLoc = False
            player.firstMove = False
            if getPlayerOnLocation(new_location) != None:
                getPlayerOnLocation(new_location).isDead = True
                getPlayerOnLocation(new_location).position = (-1,-1)
            player.position = new_location

    if player.name == 'n':
        # print('knight to be Moved')
        # L-shaped movement forward (d) backwards(u) left and right
        saveLoc = player.position
        
        #forward (D)
        saveLoc = (saveLoc[0]+2,saveLoc[1])
        saveLoc1 = (saveLoc[0],saveLoc[1]+1)
        if saveLoc1 == new_location:
            if getPlayerOnLocation(saveLoc1) == None:
                foundLoc = True
                # print('Forward R'+str(saveLoc1))
            else:
                if condition(saveLoc1):
                    foundLoc = True
        saveLoc2 = (saveLoc[0],saveLoc[1]-1)
        if saveLoc2 == new_location and not foundLoc:
            if getPlayerOnLocation(saveLoc2) == None:
                foundLoc = True
                # print('Forward L'+str(saveLoc2))
            else:
                if condition(saveLoc2):
                    foundLoc = True
        saveLoc = player.position
        #backward (u)
        saveLoc = (saveLoc[0]-2,saveLoc[1])
        saveLoc1 = (saveLoc[0],saveLoc[1]+1)
        if saveLoc1 == new_location and not foundLoc:
            if getPlayerOnLocation(saveLoc1) == None:
                foundLoc = True
                # print('Backward R'+str(saveLoc1))
            else:
                if condition(saveLoc1):
                    foundLoc = True
        saveLoc2 = (saveLoc[0],saveLoc[1]-1)
        if saveLoc2 == new_location and not foundLoc:
            if getPlayerOnLocation(saveLoc2) == None:
                foundLoc = True
                # print('Backward L'+str(saveLoc2))
            else:
                if condition(saveLoc2):
                    foundLoc = True
        saveLoc = player.position
        #Rightward (r)
        saveLoc = (saveLoc[0],saveLoc[1]+2)
        saveLoc1 = (saveLoc[0]+1,saveLoc[1])
        if saveLoc1 == new_location and not foundLoc:
            if getPlayerOnLocation(saveLoc1) == None:
                foundLoc = True
                # print('Right L'+str(saveLoc1))
            else:
                if condition(saveLoc1):
                    foundLoc = True
        saveLoc2 = (saveLoc[0]-1,saveLoc[1])
        if saveLoc2 == new_location and not foundLoc:
            if getPlayerOnLocation(saveLoc2) == None:
                foundLoc = True
                # print('Right U'+str(saveLoc2))
            else:
                if condition(saveLoc2):
                    foundLoc = True
        saveLoc = player.position
        #Leftward (r)
        saveLoc = (saveLoc[0],saveLoc[1]-2)
        saveLoc1 = (saveLoc[0]+1,saveLoc[1])
        if saveLoc1 == new_location and not foundLoc:
            if getPlayerOnLocation(saveLoc1) == None:
                foundLoc = True
                # print('Left L'+str(saveLoc1))
            else:
                if condition(saveLoc1):
                    foundLoc = True
        saveLoc2 = (saveLoc[0]-1,saveLoc[1])
        if saveLoc2 == new_location and not foundLoc:
            if getPlayerOnLocation(saveLoc2) == None:
                foundLoc = True
                # print('Left U'+str(saveLoc2))
            else:
                if condition(saveLoc2):
                    foundLoc = True
        if foundLoc:
            foundLoc = False
            player.firstMove = False
            if getPlayerOnLocation(new_location) != None:
                getPlayerOnLocation(new_location).isDead = True
                getPlayerOnLocation(new_location).position = (-1,-1)
            player.position = new_location

    if player.name == 'b':
        # print('bishop to be Moved')
        saveLoc = player.position
        #Downwards Right
        while saveLoc[0] < len(Board) and saveLoc[1] < len(Board):
            saveLoc = (saveLoc[0]+1,saveLoc[1]+1)
            if getPlayerOnLocation(saveLoc) == None:
                if saveLoc == new_location:
                    foundLoc = True
                    # print('DR ' +str(saveLoc))
            else:
                if condition(saveLoc):
                    if saveLoc == new_location:
                        foundLoc = True
                break
        #Upwards Left
        saveLoc = player.position
        while not foundLoc and saveLoc[0] >= 0 and saveLoc[1] >= 0:
            saveLoc = (saveLoc[0]-1,saveLoc[1]-1)
            if getPlayerOnLocation(saveLoc) == None:
                if saveLoc == new_location:
                    foundLoc = True
                    # print('DR ' +str(saveLoc))
            else:
                if condition(saveLoc):
                    if saveLoc == new_location:
                        foundLoc = True
                break
        #Upwards Right
        saveLoc = player.position
        while not foundLoc and saveLoc[0] >= 0 and saveLoc[1] < len(Board):
            saveLoc = (saveLoc[0]-1,saveLoc[1]+1)
            if getPlayerOnLocation(saveLoc) == None:
                if saveLoc == new_location:
                    foundLoc = True
                    # print('UR ' +str(saveLoc))
            else:
                if condition(saveLoc):
                    if saveLoc == new_location:
                        foundLoc = True
                break
        #Downwards Left
        saveLoc = player.position
        while not foundLoc and (saveLoc[0] < len(Board) and saveLoc[1] >= 0):
            saveLoc = (saveLoc[0]+1,saveLoc[1]-1)
            if getPlayerOnLocation(saveLoc) == None:
                if saveLoc == new_location:
                    foundLoc = True
                    # print('UR ' +str(saveLoc))
            else:
                if condition(saveLoc):
                    if saveLoc == new_location:
                        foundLoc = True
                break
        if foundLoc:
            foundLoc = False
            player.firstMove = False
            if getPlayerOnLocation(new_location) != None:
                getPlayerOnLocation(new_location).isDead = True
                getPlayerOnLocation(new_location).position = (-1,-1)
            player.position = new_location

    if player.name == 'q':
        # print('queen to be Moved')
        saveLoc = player.position
        #Downwards Right
        while not foundLoc and (saveLoc[0] < len(Board) and saveLoc[1] < len(Board)):
            saveLoc = (saveLoc[0]+1,saveLoc[1]+1)
            if getPlayerOnLocation(saveLoc) == None:
                if saveLoc == new_location:
                    foundLoc = True
                    # print('DR ' +str(saveLoc))
            else:
                if condition(saveLoc):
                    if saveLoc == new_location:
                        foundLoc = True
                break
        #Upwards Left
        saveLoc = player.position
        while not foundLoc and saveLoc[0] >= 0 and saveLoc[1] >= 0:
            saveLoc = (saveLoc[0]-1,saveLoc[1]-1)
            if getPlayerOnLocation(saveLoc) == None:
                if saveLoc == new_location:
                    foundLoc = True
                    # print('DR ' +str(saveLoc))
            else:
                if condition(saveLoc):
                    if saveLoc == new_location:
                        foundLoc = True
                break
        #Upwards Right
        saveLoc = player.position
        while not foundLoc and saveLoc[0] >= 0 and saveLoc[1] < len(Board):
            saveLoc = (saveLoc[0]-1,saveLoc[1]+1)
            if getPlayerOnLocation(saveLoc) == None:
                if saveLoc == new_location:
                    foundLoc = True
                    # print('UR ' +str(saveLoc))
            else:
                if condition(saveLoc):
                    if saveLoc == new_location:
                        foundLoc = True
                break
        #Downwards Left
        saveLoc = player.position
        while not foundLoc and (saveLoc[0] < len(Board) and saveLoc[1] >= 0):
            saveLoc = (saveLoc[0]+1,saveLoc[1]-1)
            if getPlayerOnLocation(saveLoc) == None:
                if saveLoc == new_location:
                    foundLoc = True
                    # print('UR ' +str(saveLoc))
            else:
                if condition(saveLoc):
                    if saveLoc == new_location:
                        foundLoc = True
                break

        # forward (d) backward(u) leftwards(l) rightwards(r)
        saveLoc = player.position
        #d
        save_saveLoc = saveLoc
        # print('Downwards')
        while saveLoc[0] < len(Board) and not foundLoc:
            saveLoc = (saveLoc[0]+1,saveLoc[1])
            if getPlayerOnLocation(saveLoc) == None:
                print(saveLoc)
                if new_location == saveLoc:
                    # print('Can Do the Move')
                    foundLoc = True
            else:
                if condition(saveLoc):
                    if saveLoc == new_location:
                        foundLoc = True
                # print('--->' + str(saveLoc))
                break
            
        #u
        saveLoc = save_saveLoc
        # print('Upwards')
        while 0 <= saveLoc[0] and not foundLoc:
            saveLoc = (saveLoc[0]-1,saveLoc[1])
            if getPlayerOnLocation(saveLoc) == None:
                print(saveLoc)
                if new_location == saveLoc:
                    # print('Can Do the Move')
                    foundLoc = True
            else:
                if condition(saveLoc):
                    if saveLoc == new_location:
                        foundLoc = True
                # print('--->' + str(saveLoc))
                break
        
        #r
        saveLoc = save_saveLoc
        # print('Rightwards')
        while saveLoc[1] < len(Board) and not foundLoc:
            saveLoc = (saveLoc[0],saveLoc[1]+1)
            if getPlayerOnLocation(saveLoc) == None:
                print(saveLoc)
                if new_location == saveLoc:
                    # print('Can Do the Move')
                    foundLoc = True
            else:
                if condition(saveLoc):
                    if saveLoc == new_location:
                        foundLoc = True
                # print('--->' + str(saveLoc))
                break
        
        #l
        saveLoc = save_saveLoc
        # print('leftwards')
        while 0 <= saveLoc[1] and not foundLoc:
            saveLoc = (saveLoc[0],saveLoc[1]-1)
            if getPlayerOnLocation(saveLoc) == None:
                print(saveLoc)
                if new_location == saveLoc:
                    # print('Can Do the Move')
                    foundLoc = True
            else:
                if condition(saveLoc):
                    if saveLoc == new_location:
                        foundLoc = True
                # print('--->' + str(saveLoc))
                break

        if foundLoc:
            foundLoc = False
            player.firstMove = False
            if getPlayerOnLocation(new_location) != None:
                getPlayerOnLocation(new_location).isDead = True
                getPlayerOnLocation(new_location).position = (-1,-1)
            player.position = new_location

    if player.name == 'k':
        # print('king to be Moved')
        saveLoc = player.position
        #Downwards Right
        if not foundLoc and (saveLoc[0] < len(Board) and saveLoc[1] < len(Board)):
            saveLoc = (saveLoc[0]+1,saveLoc[1]+1)
            if getPlayerOnLocation(saveLoc) == None:
                if saveLoc == new_location:
                    foundLoc = True
                    # print('DR ' +str(saveLoc))
            else:
                if condition(saveLoc):
                    if saveLoc == new_location:
                        foundLoc = True
        #Upwards Left
        saveLoc = player.position
        if not foundLoc and saveLoc[0] >= 0 and saveLoc[1] >= 0:
            saveLoc = (saveLoc[0]-1,saveLoc[1]-1)
            if getPlayerOnLocation(saveLoc) == None:
                if saveLoc == new_location:
                    foundLoc = True
                    # print('DR ' +str(saveLoc))
            else:
                if condition(saveLoc):
                    if saveLoc == new_location:
                        foundLoc = True
        #Upwards Right
        saveLoc = player.position
        if not foundLoc and saveLoc[0] >= 0 and saveLoc[1] < len(Board):
            saveLoc = (saveLoc[0]-1,saveLoc[1]+1)
            if getPlayerOnLocation(saveLoc) == None:
                if saveLoc == new_location:
                    foundLoc = True
                    # print('UR ' +str(saveLoc))
            else:
                if condition(saveLoc):
                    if saveLoc == new_location:
                        foundLoc = True
        #Downwards Left
        saveLoc = player.position
        if not foundLoc and (saveLoc[0] < len(Board) and saveLoc[1] >= 0):
            saveLoc = (saveLoc[0]+1,saveLoc[1]-1)
            if getPlayerOnLocation(saveLoc) == None:
                if saveLoc == new_location:
                    foundLoc = True
                    # print('UR ' +str(saveLoc))
            else:
                if condition(saveLoc):
                    if saveLoc == new_location:
                        foundLoc = True
        # forward (d) backward(u) leftwards(l) rightwards(r)
        saveLoc = player.position
        #d
        save_saveLoc = saveLoc
        # print('Downwards')
        if saveLoc[0] < len(Board) and not foundLoc:
            saveLoc = (saveLoc[0]+1,saveLoc[1])
            if getPlayerOnLocation(saveLoc) == None:
                # print(saveLoc)
                if new_location == saveLoc:
                    # print('Can Do the Move')
                    foundLoc = True
            else:
                if condition(saveLoc):
                    if new_location == saveLoc:
                        # print('Can Do the Move')
                        foundLoc = True
                # print('--->' + str(saveLoc))
            
        #u
        saveLoc = save_saveLoc
        # print('Upwards')
        if 0 <= saveLoc[0] and not foundLoc:
            saveLoc = (saveLoc[0]-1,saveLoc[1])
            if getPlayerOnLocation(saveLoc) == None:
                # print(saveLoc)
                if new_location == saveLoc:
                    # print('Can Do the Move')
                    foundLoc = True
            else:
                if condition(saveLoc):
                    if new_location == saveLoc:
                        # print('Can Do the Move')
                        foundLoc = True
                # print('--->' + str(saveLoc))
        
        #r
        saveLoc = save_saveLoc
        # print('Rightwards')
        if saveLoc[1] < len(Board) and not foundLoc:
            saveLoc = (saveLoc[0],saveLoc[1]+1)
            if getPlayerOnLocation(saveLoc) == None:
                # print(saveLoc)
                if new_location == saveLoc:
                    # print('Can Do the Move')
                    foundLoc = True
            else:
                if condition(saveLoc):
                    if new_location == saveLoc:
                        # print('Can Do the Move')
                        foundLoc = True
                # print('--->' + str(saveLoc))
        
        #l
        saveLoc = save_saveLoc
        print('leftwards')
        if 0 <= saveLoc[1] and not foundLoc:
            saveLoc = (saveLoc[0],saveLoc[1]-1)
            if getPlayerOnLocation(saveLoc) == None:
                # print(saveLoc)
                if new_location == saveLoc:
                    # print('Can Do the Move')
                    foundLoc = True
            else:
                if condition(saveLoc):
                    if new_location == saveLoc:
                        # print('Can Do the Move')
                        foundLoc = True
                # print('--->' + str(saveLoc))

        if foundLoc:
            foundLoc = False
            player.firstMove = False
            if getPlayerOnLocation(new_location) != None:
                getPlayerOnLocation(new_location).isDead = True
                getPlayerOnLocation(new_location).position = (-1,-1)
            player.position = new_location

    if player.name == 'p':
        # print('pawn to be Moved')
        # forward (d) one step and two steps forwards if first time
        saveLoc = player.position
        #d
        save_saveLoc = saveLoc
        # print('Downwards')
        saveLoc = (saveLoc[0]-1,saveLoc[1])
        if getPlayerOnLocation(saveLoc) == None:
            # print(saveLoc)
            if new_location == saveLoc:
                # print('Can Do the Move')
                foundLoc = True
        else:
            if condition(saveLoc):
                if new_location == saveLoc:
                    # print('Can Do the Move')
                    foundLoc = True
            # print('--->' + str(saveLoc))

        saveLoc = (saveLoc[0]-1,saveLoc[1])
        if getPlayerOnLocation(saveLoc) == None and player.firstMove:
            # print(saveLoc)
            if new_location == saveLoc:
                # print('Can Do the Move')
                foundLoc = True
        else:
            if condition(saveLoc):
                if new_location == saveLoc:
                    # print('Can Do the Move')
                    foundLoc = True
            # print('--->' + str(saveLoc))
        
        if foundLoc:
            foundLoc = False
            player.firstMove = False
            if getPlayerOnLocation(new_location) != None:
                getPlayerOnLocation(new_location).isDead = True
                getPlayerOnLocation(new_location).position = (-1,-1)
            player.position = new_location

def PrintBoard():
    for i in range(len(Board)):
        for j in range(len(Board)):
            fp = getPlayerOnLocation((i,j))
            if fp != None and not fp.isDead:
                print(fp.name, end='  ')
            else:
                print(Board[i][j],end='  ')
        print("")
    print('')

#Only for the user king
def checkMate(player: Player):
    # print(player.position)
    if player.name != 'k':
        return
    for i in BlackTeam.Team:
        movesToCheck = GetMoves(i)
        for j in movesToCheck:
            if player.position == j:
                print("\nCHECK MATE BY ", end='')
                print(i.name,end='')
                print(' from pos: '+ str(i.position))

def kingLoc() -> Player:
    for i in WhiteTeam.Team:
        if i.name == 'k':
            return i

def getPoints(player:str):
    if player == 'k':
        return 10
    elif player == 'q':
        return 9
    elif player == 'b':
        return 8
    elif player == 'n':
        return 7
    elif player == 'r':
        return 6
    elif player == 'p':
        return 5

def getKillables(p:Player,tlist):
    killable =[]
    point = -1
    for i in WhiteTeam.Team:
        for j in tlist:
            if i.position == j:
                killable.append(i.position)
                if getPoints(i.name) > point:
                    point = getPoints(i.name)
    return (point,killable)

def minimax(chalein):
    max = -1
    temp = None
    player = None
    for i in range(len(BlackTeam.Team)):
            a = getKillables(BlackTeam.Team[i],chalein[BlackTeam.Team[i]])
            if len(a[1]) > 0:
                # print(a[0])
                # print(a[1])
                if a[0] > max:
                    max = a[0]
                    temp = a
                    player = i
    if temp != None:
        MovePlayer(BlackTeam.Team[player],temp[1][0])
    else:
        for i in range(len(BlackTeam.Team)):
            a = GetMoves(BlackTeam.Team[i])
            MovePlayer(BlackTeam.Team[i],a[0])

def casteling(playerK:Player, playerR:Player):
    if playerK.firstMove and playerR.firstMove:
            playerR,playerK = playerK, playerK

turn = 'AI'
if __name__=="__main__":
    turn = 'AI'
    while True:
        #User Turn
        turn = 'User'
        PrintBoard()
        # checkMate(kingLoc())
        print('Your Turn')
        x0 = int(input('X-Coordinate of player to move FROM '))
        y0 = int(input('Y-Coordinate '))
        pl = getPlayerOnLocation((x0,y0))
        print(pl.position)
        print(pl.name)
        if pl.name == 'r' or \
        pl.name == 'n' or \
        pl.name == 'b' or \
        pl.name == 'q' or \
        pl.name == 'k' or \
        pl.name == 'p':
            print('Available Moves************')
            print(GetMoves(getPlayerOnLocation((x0,y0))))
            x1 = int(input('X-Coordinate of player to move ON '))
            y1 = int(input('Y-Coordinate '))
            Move((x0,y0),(x1,y1))
            PrintBoard()
        else:
            print('Not your Player u are White (small letter)')
            continue
        turn = 'AI'
        print('Ai\'s Turn')
        # AI Move Black
        chalein = dict()
        for b in BlackTeam.Team:
            chalein[b] = GetMoves(b)

        minimax(chalein)
                
        # chalein has all the attacks that can be done by a player



        print('------------------------------------------')
        checkMate(kingLoc())

