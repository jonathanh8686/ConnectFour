import evaluate
import time
from board import Board

explore_order = [3, 2, 4, 1, 5, 0, 6] # center moves are better so check those first to remove alpha/beta paths

def solve(board, depth, moves, ismax, alpha, beta):
    if(board.checkover()):
        return [evaluate.getScore(board), moves]

    if(depth == 0):
        return [evaluate.getScore(board), moves]

    rtn = [0, []]

    # make each move
    for i in explore_order:
        if(board.move(i)):
            bval = solve(board, depth - 1, moves + [i], not ismax, alpha, beta)

            if(rtn == [0,[]]):
                rtn = bval

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

mvs = [6, 3, 6, 2, 6, 6, 4, 2, 5, 1, 0, 1, 4, 1, 1, 3, 0, 2, 5, 2]

# ----- test board -----
brd = Board()
#brd.load(mvs[:-4])
while True:
    start = time.time()
    sol = solve(brd, 6,  [], True, -9999999999, 9999999999)
    print("Compute Time:\t" + str(time.time() - start) + "s")
    print(sol)
    brd.move(sol[1][0])
    print(brd)
    if(brd.checkover()):
        print(brd.moves)
        mvs = brd.moves
        print("Game Over!")
        break

    moveinp = int(input())
    brd.move(moveinp)
    print(brd)
    if(brd.checkover()):
        print(brd.moves)
        mvs = brd.moves
        print("Game Over!")
        break
# ----- end test board -----





