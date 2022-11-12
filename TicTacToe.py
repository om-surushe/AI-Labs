board = {1: " ", 2: " ", 3: " ",
         4: " ", 5: " ", 6: " ",
         7: " ", 8: " ", 9: " "}

bot = "X"
me = "O"


def printBoard():
    print(board[1]+"|"+board[2]+"|"+board[3])
    print("-+-+-")
    print(board[4]+"|"+board[5]+"|"+board[6])
    print("-+-+-")
    print(board[7]+"|"+board[8]+"|"+board[9])


def isWin():
    if (board[1] == board[2] and board[2] == board[3] and board[3] != " "):
        return True
    elif (board[4] == board[5] and board[5] == board[6] and board[6] != " "):
        return True
    elif (board[7] == board[8] and board[8] == board[9] and board[9] != " "):
        return True
    elif (board[1] == board[4] and board[4] == board[7] and board[7] != " "):
        return True
    elif (board[2] == board[5] and board[5] == board[8] and board[8] != " "):
        return True
    elif (board[3] == board[6] and board[6] == board[9] and board[9] != " "):
        return True
    elif (board[1] == board[5] and board[5] == board[9] and board[9] != " "):
        return True
    elif (board[3] == board[5] and board[5] == board[7] and board[7] != " "):
        return True
    else:
        return False


def checkMark(mark):
    if (board[1] == board[2] and board[2] == board[3] and board[3] == mark):
        return True
    elif (board[4] == board[5] and board[5] == board[6] and board[6] == mark):
        return True
    elif (board[7] == board[8] and board[8] == board[9] and board[9] == mark):
        return True
    elif (board[1] == board[4] and board[4] == board[7] and board[7] == mark):
        return True
    elif (board[2] == board[5] and board[5] == board[8] and board[8] == mark):
        return True
    elif (board[3] == board[6] and board[6] == board[9] and board[9] == mark):
        return True
    elif (board[1] == board[5] and board[5] == board[9] and board[9] == mark):
        return True
    elif (board[3] == board[5] and board[5] == board[7] and board[7] == mark):
        return True
    else:
        return False


def isDraw():
    for i in board.keys():
        if (board[i] == " "):
            return False
    return True


def isSpaceFree(index):
    if board[index] == " ":
        return True
    else:
        return False


def insertInto(mark, position):
    if isSpaceFree(position):
        board[position] = mark
        printBoard()
        if (isDraw()):
            printBoard()
            print("Draw")
            exit()

        if (isWin()):
            if (mark == bot):
                printBoard()
                print("Bot wins")
                exit()
            else:
                printBoard()
                print("You win")
                exit()

        return

    else:
        print("Can't insert there!!")
        pos = int(input("Please enter another position: "))
        insertInto(mark, pos)
        return


def playerMove():
    pos = int(input("Please enter a position for player: "))
    insertInto(me, pos)


def botMove():
    bestScore = -1000
    bestMove = 0

    for key in board.keys():
        if (board[key] == " "):
            board[key] = bot
            score = minimax(board, 0, False) # the score if we take this move
            board[key] = " "
            if (score > bestScore):
                bestScore = score
                bestMove = key

    insertInto(bot, bestMove)
    return


def minimax(board, depth, isMaximizing):

    if checkMark(bot):
        return 1

    if (checkMark(me)):
        return -1

    elif isDraw():
        return 0

    if isMaximizing:
        bestScore = -1000

        for key in board.keys():
            if(board[key]==" "):
                board[key] = bot
                score = minimax(board, 0, False) # returns the score after the other person plays
                board[key] = " "
                if (score > bestScore): # tryies to maximize
                    bestScore = score

        return bestScore

    else:
        bestScore = 800
        for key in board.keys():
            if (board[key] == " "):
                board[key] = me
                score = minimax(board, 0, True) #returns the score after bot plays
                board[key] = " "
                if (score < bestScore): # tries to minimize
                    bestScore = score
        return bestScore

while (not isDraw()):
    botMove()
    playerMove()