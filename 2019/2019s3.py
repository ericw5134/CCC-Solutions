table = [list(input().split(" ")), list(input().split(" ")), list(input().split(" "))]


def getA(b, c):
    return 2*b - c

def getB(a, c):
    return int((a+c)/2)

def getC(a, b):
    return 2*b - a

def rowFill():
    for i in range(3):
        count = []
        for j in range(3):
            if table[i][j] != "X":
                table[i][j] = int(table[i][j])
                count.append(True) #True means number EXISTS
            else:
                count.append(False) #False means number DOES NOT EXISTS
        if count.count(True) == 2:
            if not count[0]:
                table[i][0] = getA(table[i][1], table[i][2])
            elif not count[1]:
                table[i][1] = getB(table[i][0], table[i][2])
            else:
                table[i][2] = getC(table[i][0], table[i][1])



def colFill():
    for i in range(3):
        count = []
        for j in range(3):
            if table[j][i] != "X":
                table[j][i] = int(table[j][i])
                count.append(True) #True means number EXISTS
            else:
                count.append(False) #False means number DOES NOT EXISTS
        if count.count(True) == 2:
            if not count[0]:
                table[0][i] = getA(table[1][i], table[2][i])
            elif not count[1]:
                table[1][i] = getB(table[0][i], table[2][i])
            else:
                table[2][i] = getC(table[0][i], table[1][i])

#Write for different cases

rowFill()
colFill()

fullRCount = []
fullCCount = []

for i in range(3): #This for loop counts element existing integer
    existsR = 0
    existsC = 0
    for j in range(3):
        if table[i][j] != "X":
            existsR += 1
        if table[j][i] != "X":
            existsC += 1
    fullRCount.append(existsR)
    fullCCount.append(existsC)

if fullCCount.count(0) == 3 and fullRCount.count(0) == 3: #ZERO
    for i in range(3):
        for j in range(3):
            table[i][j] = 0

elif fullCCount.count(0) == 2 and fullRCount.count(0) == 2: #ONE
    num = 0
    for i in range(3):
        for j in range(3):
            if table[j][i] != "X":
                num = table[j][i]
                break
    for i in range(3):
        for j in range(3):
            table[j][i] = num

elif fullCCount.count(1) == 2 and fullRCount.count(1) == 2 and fullCCount.count(3) == 0: #TWO
    for i in range(3):
        num = 0
        for j in range(3):
            if table[i][j] != "X":
                num = table[i][j]
        if num != "X":
            for j in range(3):
                table[i][j] = num
        colFill()

elif fullCCount.count(3) == 0 and fullRCount.count(3) == 1: #THREE ROW
    for i in range(3): #Scans through certain column, finds a number, and replaces entire column
        num = 0
        for j in range(3):
            if table[j][i] != "X":
                num = table[j][i]
        for j in range(3):
            table[j][i] = num

elif fullCCount.count(3) == 1 and fullRCount.count(3) == 0: #THREE COLUMN
    for i in range(3): #Scans through certain row, finds a number, and replaces entire row
        num = 0
        for j in range(3):
            if table[i][j] != "X":
                num = table[i][j]
        for j in range(3):
            table[i][j] = num

elif fullCCount.count(1) == 3 and fullRCount.count(1) == 3: #THREE INDIVIDUAL
    num = 0
    exception = False
    for j in range(3): #If row is fillable
        if table[1][j] != "X":
            num = table[1][j]
    else: #If row is NOT fillable -> fills in column instead
        exception = True
        for j in range(3):
            if table[j][1] != "X":
                num = table[j][1]
        for j in range(3):
            table[j][1] = num
    if not exception:
        for j in range(3):
            table[1][j] = num
    colFill()
    rowFill()
    colFill()
    rowFill()

elif fullCCount.count(3) == 1 and fullRCount.count(3) == 1: #FIVE CROSS
    i = 0
    j = 0
    while table[i][j] != "X":
        if i == 2:
            i = 0
            j += 1
        else:
            i += 1
    table[i][j] = 0
    colFill()
    rowFill()
    colFill()
    rowFill()



for i in range(3):
    output = ""
    for j in range(3):
        output += str(table[i][j])
        output += " "
    print(output)