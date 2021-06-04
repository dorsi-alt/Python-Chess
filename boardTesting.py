board = [
    ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ",],
    ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ",],
    ["  ", "UU", "  ", "  ", "  ", "  ", "  ", "  ",],
    ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ",],
    ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ",],
    ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ",],
    ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ",],
    ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ",],
]


for i in range(len(board)):
    print(board[i])


rows=len(board)
columns=len(board[0])
piece = input("What piece do you want to move")
goX = int(input("what point X do you want to go to"))
goY = int(input("what Y point do you want to go to"))


def drawBoard():
    for i in range(len(board)):
        print(board[i])

def movePiece(moveToX,moveToY):
    board[moveToX][moveToY]= piece

flag = False
for i in range(rows):
    for j in range(columns):
        if board[i][j]==piece:
            print(i,j)
            board[i][j] = "  "
            movePiece(goY,goX)
            print("Found it!")
            flag = True
            break
if flag == False:
    print ("Not found!")


def main():
    drawBoard()

if __name__=='__main__':
    main()