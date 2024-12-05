#setting up variables
r1str = 0
r2str = 0
r3str = 0
r4str = 0
r5str = 0
r6str = 0
r7str = 0
r8str = 0
r9str = 0
r1str = 0

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
arrPossPrev = [[[0] for col in range(9)] for row in range(9)] #previous possibility arr: if same as previous time puzzle impossible
arrTest = [1,2,3,4,5,6,7,8,9]
repeat = True



#get input string with 9 integers
print('Plug in Values Below. For Blank Spaces Enter 0')
while len(str(r1str)) != 9 or not r1str.isdigit():
    r1str = input("Enter first row of numbers: ")
while len(str(r2str)) != 9 or not r2str.isdigit():
    r2str = input("Enter second row of numbers: ")
while len(str(r3str)) != 9 or not r3str.isdigit():
    r3str = input("Enter third row of numbers: ")
while len(str(r4str)) != 9 or not r4str.isdigit():
    r4str = input("Enter fourth row of numbers: ")
while len(str(r5str)) != 9 or not r5str.isdigit():
    r5str = input("Enter fifth row of numbers: ")
while len(str(r6str)) != 9 or not r6str.isdigit():
    r6str = input("Enter sixth row of numbers: ")
while len(str(r7str)) != 9 or not r7str.isdigit():
    r7str = input("Enter seventh row of numbers: ")
while len(str(r8str)) != 9 or not r8str.isdigit():
    r8str = input("Enter eigth row of numbers: ")
while len(str(r9str)) != 9 or not r9str.isdigit():
    r9str = input("Enter ninth row of numbers: ")
r1str = str(r1str)
r2str = str(r2str)
r3str = str(r3str)
r4str = str(r4str)
r5str = str(r5str)
r6str = str(r6str)
r7str = str(r7str)
r8str = str(r8str)
r9str = str(r9str)


#set up board array
arrStr = [r1str],[r2str],[r3str],[r4str],[r5str],[r6str],[r7str],[r8str],[r9str]


#making board
for i in range (0,9):
    tempStr = arrStr[i][0]
    for j in range (0,9):
        tempNum = int(tempStr[j])
        arrBoard[i][j] = tempNum


#making 3x3 boxes of values
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


#Finding Possibilities
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


#Check for matches in values
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


#Check If Array Fully Solved
def checkSolved(arrB):
    for i in range(0,9):
        for j in range(0,9):
            if arrB[j][i] == 0:
                return True
    return False


#def solve(arrP, arrB, repeat): if board not solved repeat the process
while repeat == True:
    arrPoss = findPoss(arrPoss,arrBoard)
    arrBoard = plugVals(arrPoss, arrBoard)
    repeat = checkSolved(arrBoard)


#print(solve(arrPoss,arrBoard,repeat)) 
for i in range(0,9):
    print(arrBoard[i])
