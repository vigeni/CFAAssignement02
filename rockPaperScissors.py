play = True

while play:
    print("Welcome to another round of Rock, paper, scissors.")
    print("Enter the number corresponding to your choice. Enter 0 to quit")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissor")
    player1 = input("Player1, make your choice.")
    player2 = input("Player2, make your choice.")
    if player1 == "0" or player2 == "0":
        play = False
        print("Thank you for playing.")
        break
    if player1 == player2:
        print("Tie!")
        break
    if player1 == "1":
        if player2 == "2":
            print("Player2 Wins")
            break
        if player2 == "3":
            print("Player1 Wins")
            break
    if player1 == "2":
        if player2 == "1":
            print("Player1 Wins")
            break
        if player2 == "3":
            print("Player2 Wins")
            break
    if player1 == "3":
        if player2 == "1":
            print("Player2 Wins")
            break
        if player2 == "2":
            print("Player1 Wins")
            break
    print("Invalid information.")
