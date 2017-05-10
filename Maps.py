# !/usr/bin/python
# -*- coding: utf-8 -*-


#Node Object
class Node(object):
    def __init__(self,node_type,position,adjacentNodes):
        """
        Node object to use in relation with the MAP
        type: Indicates if the node is a wall, a free space, or a parking slot
        position: simple [x y] array
        adjacentNodes: Array of other node objects. Important because e are dealing with roads, and as such we have nodes with direction
        ocupiedBy: Array that describes objects that are ocupying this node. Generally speaking, if two objects (cars/pedestrians) ocupy the same node, we have a crash!
        """
        self._type = node_type
        self._position = position
        self._adjacentNodes = adjacentNodes
        self._ocupiedBy = []
        
        def isAdjacent(self,node):
            """return true if we can drive/walk to input node from this one"""
            if node in self._adjacentNodes:
                return True
            else:
                return False
        
        def checkForCrashNode(self):
            """Counts the number of non Null elements in the attribute ocupiedBy, if it's bigger than 1, returns true."""
            number_of_ocupied = len(filter(lambda x: x is not None, self._ocupiedBy)) 
            if number_of_ocupied > 1:
                return True
            else:
                return False

#maps definition
WALL = 'X'
FREE = ' '
PARKING_SPOT = 'E'
ZEBRA = 'Z'
PEDESTRIAN_ZONE = '0'

SimpleMap = [[FREE for x in range(40)] for y in range(20)]

# # # WALLS # # #
SimpleMap[3][3] = WALL
SimpleMap[4][3] = WALL
SimpleMap[6][3] = WALL
SimpleMap[7][3] = WALL
SimpleMap[0][11] = WALL
SimpleMap[0][12] = WALL
for i in range(0, 2):
    for j in range(32, 34):
        SimpleMap[i][j] = WALL
for i in range(4, 7):
    SimpleMap[i][10] = WALL
for i in range(2, 4):
    for j in range(36, 38):
        SimpleMap[i][j] = WALL    
for i in range(14, 16):
    for j in range(36, 38):
        SimpleMap[i][j] = WALL
for i in range(36, 38):
    SimpleMap[17][i] = WALL
for i in range(18, 20):
    for j in range(28, 33):
        SimpleMap[i][j] = WALL
for i in range(9, 11):
    for j in range(12, 14):
        SimpleMap[i][j] = WALL
for i in range(9, 11):
    for j in range(24, 26):
        SimpleMap[i][j] = WALL
SimpleMap[12][10] = WALL
SimpleMap[17][2] = WALL
SimpleMap[17][9] = WALL
SimpleMap[8][19] = WALL
SimpleMap[7][21] = WALL
for i in range(13, 15):
    SimpleMap[16][i] = WALL
for i in range(16, 20):
    SimpleMap[16][i] = WALL    
for i in range(21, 24):
    SimpleMap[16][i] = WALL
for i in range(30, 32):
    SimpleMap[16][i] = WALL   
for i in range(18, 20):
    SimpleMap[11][i] = WALL
for i in range(18, 20):
    SimpleMap[13][i] = WALL    
for i in range(12, 14):
    SimpleMap[i][16] = WALL
for i in range(11, 13):
    SimpleMap[i][21] = WALL

# # # ZEBRAS # # #
for i in range(5, 7):
    SimpleMap[2][i] = ZEBRA
for i in range(7, 9):
    SimpleMap[8][i] = ZEBRA
for i in range(30, 32):
    SimpleMap[4][i] = ZEBRA        
for i in range(30, 32):
    SimpleMap[8][i] = ZEBRA    
for i in range(7, 9):
    SimpleMap[11][i] = ZEBRA    
for i in range(10, 12):
    SimpleMap[16][i] = ZEBRA
for i in range(26, 28):
    SimpleMap[17][i] = ZEBRA
for i in range(34, 36):
    SimpleMap[6][i] = ZEBRA
for i in range(14, 16):
    SimpleMap[i][2] = ZEBRA
for i in range(9, 11):
    SimpleMap[i][6] = ZEBRA
for i in range(14, 16):
    SimpleMap[i][15] = ZEBRA
for i in range(14, 16):
    SimpleMap[i][20] = ZEBRA
for i in range(14, 16):
    SimpleMap[i][28] = ZEBRA
for i in range(14, 16):
    SimpleMap[i][32] = ZEBRA
for i in range(5, 7):
    SimpleMap[i][28] = ZEBRA
for i in range(9, 11):
    SimpleMap[i][20] = ZEBRA
for i in range(5, 7):
    SimpleMap[i][19] = ZEBRA
for i in range(9, 11):
    SimpleMap[i][29] = ZEBRA

# # # PARKING_SPOT # # #
for i in range(11, 13):
    SimpleMap[1][i] = PARKING_SPOT
for i in range(5, 7):
    SimpleMap[19][i] = PARKING_SPOT
for i in range(4, 6):
    SimpleMap[i][33] = PARKING_SPOT
for i in range(7, 9):
    SimpleMap[i][33] = PARKING_SPOT
for i in range(11, 14):
    SimpleMap[i][33] = PARKING_SPOT
for i in range(18, 20):
    SimpleMap[i][33] = PARKING_SPOT
for i in range(4, 6):
    SimpleMap[i][36] = PARKING_SPOT
for i in range(7, 12):
    SimpleMap[i][36] = PARKING_SPOT

# # # PEDESTRIAN_ZONE # # #
for i in range(2, 14):
    SimpleMap[i][2] = PEDESTRIAN_ZONE
SimpleMap[2][3] = PEDESTRIAN_ZONE
SimpleMap[5][3] = PEDESTRIAN_ZONE
SimpleMap[8][3] = PEDESTRIAN_ZONE
for i in range(2, 9):
    SimpleMap[i][4] = PEDESTRIAN_ZONE
for i in range(7, 9):
    for j in range(5, 7):
        SimpleMap[i][j] = PEDESTRIAN_ZONE
for i in range(2, 10):
    SimpleMap[16][i] = PEDESTRIAN_ZONE
for i in range(11, 14):
    for j in range(5, 7):
        SimpleMap[i][j] = PEDESTRIAN_ZONE
for i in range(11, 14):
    SimpleMap[i][9] = PEDESTRIAN_ZONE
for i in range(12, 14):
    SimpleMap[i][11] = PEDESTRIAN_ZONE
SimpleMap[11][10] = PEDESTRIAN_ZONE
SimpleMap[13][10] = PEDESTRIAN_ZONE
for i in range(24, 26):
    SimpleMap[16][i] = PEDESTRIAN_ZONE
for i in range(12, 26):
    SimpleMap[17][i] = PEDESTRIAN_ZONE
SimpleMap[16][12] = PEDESTRIAN_ZONE
SimpleMap[16][15] = PEDESTRIAN_ZONE
SimpleMap[16][20] = PEDESTRIAN_ZONE
for i in range(28, 34):
    SimpleMap[17][i] = PEDESTRIAN_ZONE
for i in range(28, 30):
    SimpleMap[16][i] = PEDESTRIAN_ZONE
for i in range(32, 34):
    SimpleMap[16][i] = PEDESTRIAN_ZONE
for i in range(4, 12):
    SimpleMap[i][37] = PEDESTRIAN_ZONE
SimpleMap[6][36] = PEDESTRIAN_ZONE
for i in range(4, 9):
    SimpleMap[i][32] = PEDESTRIAN_ZONE
SimpleMap[6][33] = PEDESTRIAN_ZONE
for i in range(11, 14):
    SimpleMap[i][32] = PEDESTRIAN_ZONE
for i in range(12, 14):
    SimpleMap[i][26] = PEDESTRIAN_ZONE
for i in range(11, 14):
    for j in range(27, 30):
        SimpleMap[i][j] = PEDESTRIAN_ZONE
for i in range(7, 9):
    for j in range(27, 30):
        SimpleMap[i][j] = PEDESTRIAN_ZONE
for i in range(22, 27):
    SimpleMap[7][i] = PEDESTRIAN_ZONE
for i in range(22, 24):
    SimpleMap[6][i] = PEDESTRIAN_ZONE
SimpleMap[5][22] = PEDESTRIAN_ZONE
for i in range(20, 23):
    SimpleMap[8][i] = PEDESTRIAN_ZONE
for i in range(14, 21):
    SimpleMap[7][i] = PEDESTRIAN_ZONE
for i in range(15, 19):
    SimpleMap[8][i] = PEDESTRIAN_ZONE
for i in range(3, 5):
    SimpleMap[i][19] = PEDESTRIAN_ZONE
for i in range(19, 30):
    SimpleMap[2][i] = PEDESTRIAN_ZONE
for i in range(25, 30):
    SimpleMap[3][i] = PEDESTRIAN_ZONE
for i in range(26, 30):
    SimpleMap[4][i] = PEDESTRIAN_ZONE
for i in range(15, 18):
    SimpleMap[11][i] = PEDESTRIAN_ZONE
for i in range(17, 21):
    SimpleMap[12][i] = PEDESTRIAN_ZONE
for i in range(20, 24):
    SimpleMap[13][i] = PEDESTRIAN_ZONE
for i in range(22, 24):
    SimpleMap[12][i] = PEDESTRIAN_ZONE
SimpleMap[11][20] = PEDESTRIAN_ZONE
SimpleMap[11][22] = PEDESTRIAN_ZONE
SimpleMap[13][17] = PEDESTRIAN_ZONE
for i in range(12, 14):
    for j in range(14, 16):
        SimpleMap[i][j] = PEDESTRIAN_ZONE
for i in range(2, 5):
    for j in range(15, 17):
        SimpleMap[i][j] = PEDESTRIAN_ZONE
for i in range(2, 5):
    for j in range(7, 9):
        SimpleMap[i][j] = PEDESTRIAN_ZONE
for i in range(4, 9):
    SimpleMap[i][9] = PEDESTRIAN_ZONE
for i in range(7, 9):
    SimpleMap[i][10] = PEDESTRIAN_ZONE
for i in range(4, 8):
    SimpleMap[i][11] = PEDESTRIAN_ZONE
for i in range(12, 15):
    SimpleMap[4][i] = PEDESTRIAN_ZONE


# # # Declaration of Map # # #
MAP = SimpleMap


#Construction of node Map

#NodeMap = MAP

NodeMap = [[None for x in range(40)] for y in range(20)]

for y in range(0,40):
    for x in range(0,20):
        #print "x: {} y: {}".format(x,y)
        NodeMap[x][y] = Node( MAP[x][y] ,[x,y], None)	


# # # auxiliar functions on maps # # #
def printMap(): 
    for e in MAP:
        a = ""
        for c in e:
            a += ' ' + c
        print a

#printMap()

def printMapMatrix():
    a = "   "
    b = ""
    for i in range(len(MAP[0])):
        if i < 10:
            a += '|0' + str(i)
        else:
            a += '|' + str(i)
    a += "|"
    print a
    for line in range(len(MAP)):
        result_by_line = "  "
        if line < 10:
            b = "|0" + str(line) + "|"
        else:
            b = "|" + str(line) + "|"
        result_by_line = b 
        for col in range(len(MAP[0])):            
            result_by_line += " " + MAP[line][col] + " "
        result_by_line = result_by_line[:len(result_by_line)-1]
        if line < 10:
            b = "|0" + str(line) + "|"
        else:
            b = "|" + str(line) + "|"
        result_by_line += b
        print result_by_line
    print a  

def printMapWithBorders():
    upperBorder = ""
    for i in range(len(MAP[0]) + 1):
        upperBorder += "--"
    print upperBorder
    for e in MAP:
        a = "|"
        for c in e:
            a += ' ' + c
        a += "|"
        print a 
    downBorder = ""
    for i in range(len(MAP[0]) + 1):
        downBorder += "--"
    print downBorder  
    
def countElements(element):
    count = 0
    for line in MAP:
        for e in line:
            if e == element:
                count += 1
    return count
