#setting up variables
print('Plug in Values Below. For Blank Spaces Enter 0')
r1str = '200030040' #input("Enter first row of numbers: ")
r2str = '030600007' #input("Enter second row of numbers: ")
r3str = '009007108' #input("Enter third row of numbers: ")
r4str = '004072000'# #input("Enter fourth row of numbers: ")
r5str = '025081900' #input("Enter fifth row of numbers: ")
r6str = '103006005' #input("Enter sixth row of numbers: ")
r7str = '000020400' #input("Enter seventh row of numbers: ")
r8str = '406800070'#input("Enter eigth row of numbers: ")
r9str = '500900300' #input("Enter ninth row of numbers: ")
arrStr = [r1str],[r2str],[r3str],[r4str],[r5str],[r6str],[r7str],[r8str],[r9str]
arrBoard = [[0 for col in range(9)] for row in range(9)]
box1 = [[0 for col in range(3)] for row in range(3)]
box2 = [[0 for col in range(3)] for row in range(3)]   
box3 = [[0 for col in range(3)] for row in range(3)]
box4 = [[0 for col in range(3)] for row in range(3)]
box5 = [[0 for col in range(3)] for row in range(3)]
box6 = [[0 for col in range(3)] for row in range(3)]
box7 = [[0 for col in range(3)] for row in range(3)]
box8 = [[0 for col in range(3)] for row in range(3)]
box9 = [[0 for col in range(3)] for row in range(3)]
arrPoss = [[[0] for col in range(9)] for row in range(9)]
arrTest = [1,2,3,4,5,6,7,8,9]
repeat = True


#making board
for i in range (0,9):
    tempStr = arrStr[i][0]
    for j in range (0,9):
        tempNum = int(tempStr[j])
        arrBoard[i][j] = tempNum


#making boxes
for i in range (0,9):
    for j in range (0,9):
        if i < 3 and j <3:
            box1[j][i] = arrBoard[j][i]
        elif i > 2 and i <6 and j < 3:
            box2[j][i-3] = arrBoard[j][i]
        elif i > 5 and j < 3:
            box3[j][i-6] = arrBoard[j][i]
        elif i < 3 and j > 2 and j < 6:
            box4[j-3][i] = arrBoard[j][i]
        elif i > 2 and i < 6 and j < 6 and j > 2:
            box5[j-3][i-3] = arrBoard[j][i]
        elif i > 5 and j > 2 and j < 6:
            box6[j-3][i-6] = arrBoard[j][i]
        elif i < 3 and j > 5:
            box7[j-6][i] = arrBoard[j][i]
        elif i > 2 and i < 6 and j > 5:
            box8[j-6][i-3] = arrBoard[j][i]
        else:
            box9[j-6][i-6] = arrBoard[j][i]


#Finding Possitbilities
def findPoss(arrP, arrB):
    arrP = [[[0] for col in range(9)] for row in range(9)]
    for i in range(0,9):
        for j in range(0,9):
            if i < 3 and j <3:
                box1[j][i] = arrB[j][i]
                box = box1
            elif i > 2 and i <6 and j < 3:
                box2[j][i-3] = arrB[j][i]
                box = box2
            elif i > 5 and j < 3:
                box3[j][i-6] = arrB[j][i]
                box = box3
            elif i < 3 and j > 2 and j < 6:
                box4[j-3][i] = arrB[j][i]
                box = box4
            elif i > 2 and i < 6 and j < 6 and j > 2:
                box5[j-3][i-3] = arrB[j][i]
                box = box5
            elif i > 5 and j > 2 and j < 6:
                box6[j-3][i-6] = arrB[j][i]
                box = box6
            elif i < 3 and j > 5:
                box7[j-6][i] = arrB[j][i]
                box = box7
            elif i > 2 and i < 6 and j > 5:
                box8[j-6][i-3] = arrB[j][i]
                box = box8
            else:
                box9[j-6][i-6] = arrB[j][i]
                box = box9
                
            if(arrB[j][i] == 0):
                for k in range(1,10):
                    poss = True
                    col = arrB[j]
                    for x in range (0,9):
                          if col[x] == k:
                            poss = False
                    for x in range (0,9):
                        if arrB[x][i] == k:
                            poss = False
                    for x in range(0,3):
                        for y in range(0,3):
                            if k == box[x][y]:
                                poss = False
                    for x in range(0,len(arrP[j][i])):
                        temp = arrP[j][i]
                        if k == temp[x]:
                            poss = False
                    if poss == True:
                        if arrP[j][i] == [0]:
                            arrP[j][i] = [k]
                        else:
                            arrP[j][i].append(k)
    return arrP


#Check for matches
def plugVals(arrP, arrB):
    match = False
    for i in range(0,9):
        for j in range(0,9):
            arrTemp = arrP[j][i]
            if arrTemp[0] != 0 and len(arrTemp) == 1:
                match = True
                arrB[j][i] = arrTemp[0]
                arrPoss[j][i] = [0]
    if match == False:
        print('error')
        exit()
    return arrB


#Check If Solved
def checkSolved(arrB):
    for i in range(0,9):
        for j in range(0,9):
            if arrB[j][i] == 0:
                return True
    return False


#def solve(arrP, arrB, repeat):
while repeat == True:
    arrPoss = findPoss(arrPoss,arrBoard)
    arrBoard = plugVals(arrPoss, arrBoard)
    repeat = checkSolved(arrBoard)


#print(solve(arrPoss,arrBoard,repeat))
print(arrBoard)
