import evaluate

class Board:
    state = [[-1, -1, -1, -1, -1, -1] for i in range(7)] # columns first
    turn = 0
    def __init__(self, state):
        self.state = state

    def __init__(self):
        pass

    def move(self, col):
        for i in range(len(self.state[col]))[::-1]: # always 7
            if(self.state[col][i] == -1):
                self.state[col][i] = self.turn
                self.turn = int(not self.turn)
                return True
        return False

    def unmove(self, col):
        for i in range(len(self.state[col])):
            if(self.state[col][i] != -1):
                self.state[col][i] = -1
                self.turn = int(not self.turn)
                return True
        return False

    def __repr__(self):
        rtnStr = ""
        for i in range(len(self.state[0])):
            for j in range(len(self.state)):
                rtnStr += str(self.state[j][i]) + "\t"
            rtnStr += "\n"
        return rtnStr

def solve(board, depth, moves, ismax):
    if(depth == 0):
        return [evaluate.evalBoard(board), moves]

    rtn = [0, []]

    # make each move
    for i in range(7):
        if(board.move(i)):
            bval = solve(board, depth - 1, moves + [i], not ismax)

            if(rtn == [0,[]]):
                rtn = bval

            #print(board)
            #print([bval, moves + [i]])
            if(ismax):
                if(rtn[0] <= bval[0]):
                    rtn = bval
            else:
                if(rtn[0] >= bval[0]):
                    rtn =bval
            board.unmove(i)

    return rtn


# ----- test board -----
brd = Board()
while True:
    sol = solve(brd, 5,  [], True)
    brd.move(sol[1][0])
    print(brd)

    moveinp = int(input())
    brd.move(moveinp)
    print(brd)
# ----- end test board -----

print(brd)
print(solve(brd, 5, [], True))
print("done")
