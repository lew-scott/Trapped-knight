# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 20:35:31 2019

@author: pm11lms
"""
from getboard import initMatrix as b
import numpy as np

def getMoves():
    board = np.array(b())
    x = 35
    y = 35
    kMoves =[[x,y]]
    num = []
    num.append(board[y][x])
    
    
    def checkMove(number):
        if number in num:
            return True
        else:
            return False
        
    def moveAvailable(posMoves):
        if len(posMoves) == 0:
            return 0
        
        minMove = min(posMoves)
        
        if checkMove(minMove) == False:
            return minMove
        
        else:
            posMoves.remove(minMove)
            return moveAvailable(posMoves)
    
    minNum = float("NaN")
    
    while minNum != 0:
        moves = [[0]for i in range(0,8)]
        #up
        moves[0] = board[y-2][x-1]
        moves[1] = board[y-2][x+1]
        #down
        moves[2] = board[y+2][x-1]
        moves[3] = board[y+2][x+1]
        #left
        moves[4] = board[y-1][x-2]
        moves[5] = board[y+1][x-2]
        #right
        moves[6] = board[y-1][x+2]
        moves[7] = board[y+1][x+2]
        
        minNum = moveAvailable(moves)
        if minNum == 0:
            break
        
        index = np.where(board==minNum)
        x = int(index[1])
        y = int(index[0])
        kMoves.append([x,y])
        num.append(minNum)
    return kMoves