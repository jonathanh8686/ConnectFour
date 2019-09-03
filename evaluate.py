
def checkBound(board, oriCord, trans):
    if(oriCord[0] + trans[0] < 0 or oriCord[1] + trans[1] < 0):
        return False

    if(oriCord[0] + trans[0] >= len(board.state[oriCord[0]]) or oriCord[1] + trans[1] >= len(board.state[oriCord[0]])):
        return False

    return True


def countConnected(board): # returns an array [[a1, b1, c1], [a2, b2, c3]] with connected [ 2, 3, 4]
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

            hrtMatch = 0
            for t in hort:
                if(not checkBound(board, [i, j], t)):
                    break

                if(board.state[i + t[0]][j + t[1]] == board.state[i][j]):
                    hrtMatch += 1
                else:
                    break
            rtnCount[board.state[i][j]][hrtMatch] += 1

            vrtMatch = 0
            for t in vert:
                if(not checkBound(board, [i, j], t)):
                    break

                if(board.state[i + t[0]][j + t[1]] == board.state[i][j]):
                    vrtMatch += 1
                else:
                    break
            rtnCount[board.state[i][j]][vrtMatch] += 1

            tdiaMatch = 0
            for t in tdiag:
                if(not checkBound(board, [i, j], t)):
                    break

                if(board.state[i + t[0]][j + t[1]] == board.state[i][j]):
                    tdiaMatch += 1
                else:
                    break
            rtnCount[board.state[i][j]][tdiaMatch] += 1

            bdiaMatch = 0
            for t in bdiag:

                if(not checkBound(board, [i, j], t)):
                    break

                if(board.state[i + t[0]][j + t[1]] == board.state[i][j]):
                    bdiaMatch += 1
                else:
                    break
            rtnCount[board.state[i][j]][bdiaMatch] += 1

    return rtnCount



def evalBoard(board): # return a real number [-1, 1] which depends on winner
    # TODO: make sure the AI is always aiming for a 4 (3 connect and 2 connect
    # don't matter unless there is room for a 4)
    score = 0

    matchCount = countConnected(board)
    mult = [0, 0, 1, 4, 99999]
    #print(matchCount)
    for i in range(len(matchCount[0])):
        score += matchCount[0][i] * mult[i]

    for i in range(len(matchCount[1])):
        score -= matchCount[1][i] * mult[i]

    return score






