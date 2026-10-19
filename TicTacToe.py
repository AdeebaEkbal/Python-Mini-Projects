board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
player = "X"
turn = 0
game_over = False

while game_over == False and turn < 9:
        print(f" {board[0]} | {board[1]} | {board[2]}")
        print("---|---|---")
        print(f" {board[3]} | {board[4]} | {board[5]}")
        print("---|---|---")
        print(f" {board[6]} | {board[7]} | {board[8]}\n")

        choice = input(f"Player {player}, choose a number between 1 and 9: ")
        index = int(choice) - 1

        if board[index] == "X" or board[index] == "O":
                print("Spot already taken. Try again.")
                continue

        board[index] = player
        turn = turn + 1

        # Columns:
        if board[0] == player and board[3] == player and board[6] == player:
                game_over = True
        if board[1] == player and board[4] == player and board[7] == player:
                game_over = True
        if board[2] == player and board[5] == player and board[8] == player:
                game_over = True

        # Rows:
        if board[0] == player and board[1] == player and board[2] == player:
                game_over = True
        if board[3] == player and board[4] == player and board[5] == player:
                game_over = True
        if board[6] == player and board[7] == player and board[8] == player:
                game_over = True

        # Diagonals:
        if board[0] == player and board[4] == player and board[8] == player:
                game_over = True
        if board[2] == player and board[4] == player and board[6] == player:
                game_over = True
        
        if game_over == True:
                print(f" {board[0]} | {board[1]} | {board[2]}")
                print("---|---|---")
                print(f" {board[3]} | {board[4]} | {board[5]}")
                print("---|---|---")
                print(f" {board[6]} | {board[7]} | {board[8]}\n")
        
                print(f"Player {player} wins!")

        if player == "X":
                player = "O"
        else:
                player = "X"
                
if game_over == False:
        print("It's a Draw!")