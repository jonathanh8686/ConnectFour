
def checkBound(board, oriCord, trans):
    if(oriCord[0] + trans[0] < 0 or oriCord[1] + trans[1] < 0):
        return False

    if(oriCord[0] + trans[0] >= len(board.state) or oriCord[1] + trans[1] >= len(board.state[oriCord[0]])):
        return False

    return True

def checkTransform(board, transform, pos):
    rtn =  0
    for t in transform:
        if(not checkBound(board, pos, t)):
            break

        if(board.state[pos[0] + t[0]][pos[1] + t[1]] == board.state[pos[0]][pos[1]]):
            rtn += 1
        else:
            break
    return rtn

def countConnected(board): # returns an array [[a1, b1, c1], [a2, b2, c3]] with connected [2, 3, 4]
    rtnCount = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

    hort = [[0, 0], [1, 0], [2, 0], [3, 0]] # horizontal transform
    vert = [[0, 0], [0, 1], [0, 2], [0, 3]] # vertical transform

    tdiag = [[0, 0], [1, 1], [2, 2], [3, 3]] # top left diagonal
    bdiag = [[0, 0], [1, -1], [2, -2], [3, -3]] # bottom left diagonal

    hrtMatch, vrtMatch, tdiaMatch, bdiaMatch = 0, 0, 0, 0

    for i in range(len(board.state)):
        for j in range(len(board.state[i])):
            if(board.state[i][j] == -1):
                continue

            rtnCount[board.state[i][j]][checkTransform(board, hort, [i, j])] += 1
            rtnCount[board.state[i][j]][checkTransform(board, vert, [i, j])] += 1
            rtnCount[board.state[i][j]][checkTransform(board, tdiag, [i, j])] += 1
            rtnCount[board.state[i][j]][checkTransform(board, bdiag, [i, j])] += 1

    return rtnCount



def evalBoard(board): # return a real number [-1, 1] which depends on winner

    # TODO: make sure the AI is always aiming for a 4 (3 connect and 2 connect
    # don't matter unless there is room for a 4)
    score = 0

    matchCount = countConnected(board)

    #if(matchCount[0][4] != 0):
        #return 1000000000000
        #if(board.turn == 0):
        #    return 100000000000
        #else:
        #    return -100000000000

    #if(matchCount[1][4] != 0):
        #return 1000000000000
        #if(board.turn == 0):
        #    return -100000000000
        #else:
        #    return 100000000000
    return matchCount

def getScore(board):
    score = 0

    mult = [0, 0, 1, 4, 99999]
    matchCount = evalBoard(board)
    for i in range(len(matchCount[0])):
        score += matchCount[0][i] * mult[i]

    for i in range(len(matchCount[1])):
        score -= matchCount[1][i] * mult[i]

    return score




