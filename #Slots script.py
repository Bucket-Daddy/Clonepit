#Slots script
import random
import math
import mathpy as mp
import numpy as np

#importerer nødvendig data
prerollItems = []
interventions = []
postrollItems = []
symbols = ['lemon', 'cherry', 'clover', 'bell', 'diamond', 'treasure', 'seven']
symbolWeights = [1.3, 1.3, 1, 1, 0.8, 0.8, 0.5] #lemon, cherry, clover, bell, diamond, treasure, seven.
buttonPressed = False
luck = 15
res = []
chance666 = 1.5
is666 = False
save666 = False
result = []
eyeShape = [1, 2, 3, 5, 6, 8, 9, 11, 12, 13]
aboveShape = [2, 6, 8, 10, 11, 12, 13, 14]
belowShape = [0, 1, 2, 3, 4, 6, 8, 12]
eye = False
zigShape = [2, 6, 8, 10, 14]
zagShape = [0, 4, 6, 8, 12]



#pre-roll items aktiveres
for item in prerollItems:
    item.trigger

#Luck symbol vælges og indsættes
luckSymbol = random.choices(symbols, weights = symbolWeights)
for i in range(luck):
    res += luckSymbol

#Resten af symbolerne vælges
if(len(res) < 15):
    for i in range(15 - len(res)):
        res += random.choices(symbols, weights = symbolWeights)

#Symbolerne fordeles over skærmen
random.shuffle(res)

#666, 66 og 6 chancerne rulles
if(100 * random.random() <= chance666):
    res[6] = 'six'
    res[7] = 'six'
    res[8] = 'six'
    is666 = True
else:
    if(100 * random.random() <= 6):
        res[6] = 'six'
        res[7] = 'six'
    else:
     if(100 * random.random() <= 6):
         res[6] = 'six'

#Hvis der rulles en 666 tjekkes det om der er interventions der kan redde. Hvis der ikke er, sættes coins til 0, hvis der er sker intet
if(is666):
    if(not save666):
        coins = 0
else:
   
    vertList = [0,0,0]
    horXLList = [0,0,0,0,0]
    horLList = [0,0,0,0]
    horList = [0,0,0]
    diagList = []

#Eye listen defineres
    eyeList = []
    for i in eyeShape:
        eyeList.append(res[i])    

#Det tjekkes om der er et eye
    if(eyeList.count(eyeList[0]) == 10):
        result.append('eye')
        eye = True
    else: #Hvis der ikke er et eye tjekkes de 2 verts der indgår i eye
        for i in range(2):
            for j in range(3):
                vertList[j] = res[1 + 5 * j +2 * i]
            if(vertList.count(vertList[0]) == 3):
                    result.append('vert' + str(i * 2))

#De tre andre verts tjekkes lige meget hvad
    for i in range(3):
        for j in range(3):
            vertList[j] = res[5 * j + 2 * i]
        if(vertList.count(vertList[0]) == 3):
            result.append('vert' + str(1 + i * 2))
    
#Above listen defineres
    aboveList = []
    for i in aboveShape:
        aboveList.append(res[i])

#Det tjekkes om der er en above
    if(aboveList.count(aboveList[0]) == 8):
        result.append('above')
    else: #Hvis der ikke er et above tjekkes den horXL der indgår i above
        for i in range(5):
            horXLList[i] = res(i)   
        if(horXLList.count(horXLList[0]) == 5): # X X X X X
            result.append('horXL1') 
        else: #Hvis der ikke er en horXL tjekkes den første af de 2 horL der kan indgå i horXL
            for i in range(4):
                horLList[i] = res(i)
            if(horLList.count(horLList[0]) == 4): # X X X X *
                result.append('horL1.1')
            else: #Hvis den første horL ikke er der tjekkes der for den anden
                for i in range(4):
                    horLList[i] = res(i + 1)
                if(horLList.count(horLList[0]) == 4): # * X X X X
                    result.append('horL1.2')  
                else: #hvis der ikke er nogen horL tjekkes der for 2 af de 3 mulige hor
                    for i in range(2):
                        for j in range(3):
                            horList[j] = res(2 * i + j)
                    if(horList.count(horList[0]) == 3): # X X X * *
                        result.append('hor1.' + str(1 + 2 * i))
#Den sidste hor tjekkes, men her skal det også tjekkes om det overskrives af eye
                    for i in range(3):
                        horList[j] = res(i)    
                    if(horList.count(horList[0]) == 3 and not eye): # * X X X *
                        result.append('hor1.2') 
#Hvis der ikke er et above tjekkes der for en zig
        zigList = []    
        for i in zigShape:
            zigList.append(i)
        if(zigList.count(zigList[0]) == 5):
            result.append('zig')
        else: #Hvis der ikke er en zig tjekkes der for den første af de 2 mulige diags
            diagShape = [2, 6, 10]
            diagList.clear()
            for i in diagShape:
                diagList.append(res[i])
            if(diagList.count(diagList[0]) == 3):
                result.append('fwdDiag1')
            else: #Hvis den første diag ikke er der tjekkes der for den anden
                diagshape = [2, 8, 14]
                diagList.clear()
                for i in diagShape:
                    diagList.append(res[i])
                if(diagList.count(diagList[0]) == 3):
                    result.append('bckDiag3')

#Below listen defineres
    belowList = []
    for i in belowShape:
        belowList.append(res[i])

#Det tjekkes om der er en below
    if(belowList.count(belowList[0]) == 8):
        result.append('below')
    else: #Hvis der ikke er et below tjekkes den horXL der indgår i below
        for i in range(5):
            horXLList[i] = res(i + 10)   
        if(horXLList.count(horXLList[0]) == 5): # X X X X X
            result.append('horXL3') 
        else: #Hvis der ikke er en horXL tjekkes den første af de 2 horL der kan indgå i horXL
            for i in range(4):
                horLList[i] = res(i + 10)
            if(horLList.count(horLList[0]) == 4): # X X X X *
                result.append('horL3.1')
            else: #Hvis den første horL ikke er der tjekkes der for den anden
                for i in range(4):
                    horLList[i] = res(i + 11)
                if(horLList.count(horLList[0]) == 4): # * X X X X
                    result.append('horL3.2')  
                else: #hvis der ikke er nogen horL tjekkes der for 2 af de 3 mulige hor
                    for i in range(2):
                        for j in range(3):
                            horList[j] = res(2 * i + j + 10)
                    if(horList.count(horList[0]) == 3): # X X X * *
                        result.append('hor3.' + str(1 + 2 * i))
#Den sidste hor tjekkes, men her skal det også tjekkes om det overskrives af eye
                    for i in range(3):
                        horList[j] = res(i)    
                    if(horList.count(horList[0]) == 3 and not eye): # * X X X *
                        result.append('hor3.2')
#Hvis der ikke er et below tjekkes der for en zag
        zagList = []    
        for i in zagShape:
            zagList.append(i)
        if(zagList.count(zagList[0]) == 5):
            result.append('zag')
        else: #Hvis der ikke er en zag tjekkes der for den første af de 2 mulige diags
            diagShape = [0, 6, 12]
            diagList.clear()
            for i in diagShape:
                diagList.append(res[i])
            if(diagList.count(diagList[0]) == 3):
                result.append('bckDiag1')
            else: #Hvis den første diag ikke er der tjekkes der for den anden
                diagShape = [4, 8, 12]
                diagList.clear()
                for i in diagShape:
                    diagList.append(res[i])
                if(diagList.count(diagList[0]) == 3):
                    result.append('fwdDiag3')

#Den midterste horXL tjekkes lige meget hvad
    for i in range(5):
        horXLList[i] = res[i + 5]
    if(horXLList.count(horXLList[0]) == 5): # X X X X X
        result.append('horXL2') 
    else: #Hvis der ikke er en horXL tjekkes den første af de 2 horL der kan indgå i horXL
        for i in range(4):
            horLList[i] = res(i + 5)
        if(horLList.count(horLList[0]) == 4): # X X X X *
            result.append('horL2.1')
        else: #Hvis den første horL ikke er der tjekkes der for den anden
            for i in range(4):
                horLList[i] = res(i + 6)
            if(horLList.count(horLList[0]) == 4): # * X X X X
                result.append('horL2.2')  
            else: #hvis der ikke er nogen horL tjekkes der for de 3 mulige hor
                for i in range(3):
                    for j in range(3):
                        horList[j] = res(i + j + 5)
                if(horList.count(horList[0]) == 3):
                    result.append('hor2.' + str(1 + i))

#De midterste 2 diags tjekkes lige meget hvad
    diagShape = [3, 7, 11]
    diagList.clear()
    for i in diagShape:
        diagList.append(res[i])
    if(diagList.count(diagList[0]) == 3):
        result.append('fwdDiag2')

    diagShape = [1, 7, 13]
    diagList.clear()
    for i in diagShape:
        diagList.append(res[i])
    if(diagList.count(diagList[0]) == 3):
        result.append('bckDiag2')

#Jackpot tjekkes lige meget hvad
    if(res.count(res[0]) == 15):
        result.append('jackpot')



print(res[:5])
print(res[5:10])
print(res[10:])
print(result)
