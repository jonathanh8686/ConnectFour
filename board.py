import evaluate

class Board:
    state = [[-1, -1, -1, -1, -1, -1] for i in range(7)] # columns first
    moves = []
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

                moves.append(col)
                return True
        return False

    def unmove(self, col):
        for i in range(len(self.state[col])):
            if(self.state[col][i] != -1):
                self.state[col][i] = -1
                self.turn = int(not self.turn)

                moves.remove(col)
                return True
        return False

    def checkover(self):
        counts = evaluate.countConnected(self)
        if(counts[0][4] != 0 or counts[1][4] != 0):
            return True
        else:
            return False

    def __repr__(self):
        rtnStr = ""
        for i in range(len(self.state[0])):
            for j in range(len(self.state)):
                if(self.state[j][i] == 0):
                    rtnStr += "X"
                elif(self.state[j][i] == 1):
                    rtnStr += "O"
                else:
                    rtnStr += "."
                rtnStr += "    "
            rtnStr += "\n"
        return rtnStr
