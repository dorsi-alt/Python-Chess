'''
KINDA STOPPED THIS BECAUSE CONTROLS ARE CONFUSING AND SO ARE GRAPHICS 
'''


board = [
    [" 0 ", " 1 ", " 2 ", " 3 ", " 4 ", " 5 ", " 6 ", " 7 ", " 8 ",],
    [" 1 ", "BRL", "BNL", "BBL", "BQN", "BKG", "BBR", "BNR", "BRR",],
    [" 2 ", "BP1", "BP2", "BP3", "BP4", "BP5", "BP6", "BP7", "BP8",],
    [" 3 ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ",],
    [" 4 ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ",],
    [" 5 ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ",],
    [" 6 ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ",],
    [" 7 ", "WP1", "WP2", "WP3", "WP4", "WP5", "WP6", "WP7", "WP8",],
    [" 8 ", "WRL", "WNL", "WBL", "WQN", "WKG", "WBR", "WNR", "WRR",],
]


for i in range(len(board)):
    print(board[i])



rows=len(board)
columns=len(board[0])

while True:
    while True:
        piece = input("What piece do you want to move:\n")
        goX = int(input("what point X do you want to go to\n"))
        goY = int(input("what Y point do you want to go to\n"))
        if goX <= 0 or goX > 8:
            continue

        if goY <= 0 or goY > 8:
            continue

        else:
            break



    def drawBoard():
        print("Current Board:")
        for i in range(len(board)):
            print(board[i])

    def movePiece(moveToX,moveToY):
        board[moveToX][moveToY]= piece

    flag = False
    for i in range(rows):
        for j in range(columns):
            if board[i][j]==piece:
                #locating piece on the board 
                #print(i,j)
                board[i][j] = "   "
                movePiece(goY,goX)
                flag = True
                break
    if flag == False:
        print ("Piece Not found!")
        


    def main():
        drawBoard()

    if __name__=='__main__':
        main()