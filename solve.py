import evaluate
from board import Board

def solve(board, depth, moves, ismax, alpha, beta):
    if(board.checkover()):
        return [evaluate.getScore(board), moves]
    if(depth == 0):
        return [evaluate.getScore(board), moves]

    rtn = [0, []]

    # make each move
    for i in range(7):
        if(board.move(i)):
            bval = solve(board, depth - 1, moves + [i], not ismax, alpha, beta)

            if(rtn == [0,[]]):
                rtn = bval

            #print(board)
            #print([bval, moves + [i]])
            if(ismax):
                if(rtn[0] <= bval[0]):
                    rtn = bval
                alpha = max(alpha, rtn[0])
            else:
                if(rtn[0] >= bval[0]):
                    rtn = bval
                beta = min(beta, rtn[0])

            board.unmove(i)

            if(beta < alpha):
                break

    return rtn


# ----- test board -----
brd = Board()
while True:
    sol = solve(brd, 5,  [], True, -9999999999, 9999999999)
    print(sol)
    brd.move(sol[1][0])
    print(brd)
    if(brd.checkover()):
        print(brd.moves)
        print("Game Over!")

    moveinp = int(input())
    brd.move(moveinp)
    print(brd)
    if(brd.checkover()):
        print(brd.moves)
        print("Game Over!")
# ----- end test board -----
