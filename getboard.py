# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 20:35:31 2019

@author: pm11lms
"""


def initMatrix():
    
    #size of matrix
    sizeX = 71
    sizeY = 71
    
    # initalise matrix with zero's
    matrix = [[[0] for x in range(0,sizeX)]for x in range(0,sizeY)]
    
    #middle of matrix
    i = 35
    j = 35
    
    #numbers outside of loop
    matrix[j][i] = 1
    matrix[j][i+1] = 2
    matrix[j-1][i+1] = 3
    matrix[j-1][i] = 4
    
    #size of first sq.
    sRow = 3
    #starting point
    i = 34 
    j = 34
    
    # count starting
    c = 5

    #fill matrix
    while c <= (sizeX - 1) * (sizeY - 1):
        #down
        for x in range(0, sRow):
            matrix[j][i] = c
            j += 1
            c += 1
        #right 
        i += 1
        j -= 1
        for x in range(0, sRow):
            matrix[j][i] = c
            i += 1
            c += 1
        #up
        i -= 1
        j -= 1
        for x in range(0, sRow):
            matrix[j][i] = c
            j -= 1
            c += 1
        #left
        i -= 1
        j += 1
        for x in range(0, sRow):
            matrix[j][i] = c
            i -= 1
            c += 1
        
        #increase row size 
        sRow += 2
    
    for x in range(0, sizeY):
        matrix[x][i] = c
        c += 1
        j += 1
    
    j -= 1
    for x in range(1, sizeX):
        matrix[j][x] = c
        c += 1
        i += 1
    
    return matrix