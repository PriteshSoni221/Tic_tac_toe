import tkinter as tk

# Global Variables

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

current_player = "X"

game_still_going = True

winner = None


def play_game():
    """The main function to play the game"""
    # calling global functions. We need them if player wants to play again.
    global board
    global game_still_going

    # shows initial position of board , all places are blank
    display_board()

    # while loop to keep the game continuous until someone wins or game ties.
    while game_still_going:
        handle_turn(current_player)

        check_if_game_over()

        flip_player()

    # Printing the result
    if winner is not None:
        print(winner + " has won the game!")
    else:
        print("Draw!")

    # Given line of codes are helping user to play again if he wishes
    play_again = input("Type 'yes' to play again, Type anything else to close the game! : ")
    play_again = play_again.lower().strip()
    if play_again == "yes":
        board = ["-", "-", "-",
                 "-", "-", "-",
                 "-", "-", "-"]
        game_still_going = True

        play_game()

    else:
        print("Thank you for playing!")

    return


def display_board():
    """ Display the current board"""
    print("\n")
    print(board[0] + "|" + board[1] + "|" + board[2] + "\t" + "1 | 2 | 3")
    print(board[3] + "|" + board[4] + "|" + board[5] + "\t" + "4 | 5 | 6")
    print(board[6] + "|" + board[7] + "|" + board[8] + "\t" + "7 | 8 | 9")
    print("\n")
    pass


def handle_turn(player):
    """Allows user to input the sign i.e. X or O  and show the sign in a new board"""
    print(player, "'s turn")
    valid = False
    while not valid:
        position = input("Enter the position number from 1-9:")
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Enter the position number from 1-9:")

        position = int(position) - 1
        if board[position] == "-":
            valid = True
        else:
            print("Position is invalid!")

    board[position] = player

    # display the board after taking an input from user
    display_board()


def flip_player():
    """ Gives chance to another player to play """
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"
    return


def check_if_game_over():
    """we are checking if the game is over or not by checking the win and tie conditions"""
    player_won()
    game_tie()


def player_won():
    """we are calling the functions check_row(), check_column() and check_diagonal(). Saving the returned
    values in variables. Those returned values are either X or O. Then we will assign either value in winner"""
    global winner

    row_winner = check_row()
    column_winner = check_column()
    diagonal_winner = check_diagonal()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner


def check_row():
    """checking all 3 rows for wining conditions"""
    # calling global variabel to make changes in it
    global game_still_going

    # checking the values of Row 1,2 & 3. excluding "-" to get rid of unexpected situation in the beginning
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    # If rows have equal sign, we need to stop the game immediately
    if row_1 or row_2 or row_3:
        game_still_going = False

    # we are returning the winner player's sign.
    if row_1:
        return board[0]
    elif row_2:
        return board[4]
    elif row_3:
        return board[7]
    else:
        return None


def check_column():
    """checking columns. Logic is pretty similar to row"""
    global game_still_going

    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    if column_1 or column_2 or column_3:
        game_still_going = False

    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    else:
        return None


def check_diagonal():
    """checking diagonals. Logic is pretty similar to row"""
    global game_still_going

    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"

    if diagonal_1 or diagonal_2:
        game_still_going = False

    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    else:
        return None


def game_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False


# From here I will define the GUI code
root = tk.Tk()
root.title("Tic Tac Toe")
min_width, min_height = 750, 700
root.minsize(min_width, min_height)
# given line of code will make our whole window transparent.
# root.wm_attributes("-alpha", 0.99)
background_image = tk.PhotoImage(file="game.png")
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0)

notice_label = tk.Label(root, text="Important info will appear here.", font=("times new roman", 20))
notice_label.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)

# These are buttons with 0.19*0.19 size so that there is a thin line between them, make it look pretty.
button1 = tk.Button(root, bg="#4287f5")
button1.place(relx=0.2, rely=0.3, relwidth=0.19, relheight=0.19)
button2 = tk.Button(root, bg="#4287f5")
button2.place(relx=0.4, rely=0.3, relwidth=0.19, relheight=0.19)
button3 = tk.Button(root, bg="#4287f5")
button3.place(relx=0.6, rely=0.3, relwidth=0.19, relheight=0.19)
button4 = tk.Button(root, bg="#4287f5")
button4.place(relx=0.2, rely=0.5, relwidth=0.19, relheight=0.19)
button5 = tk.Button(root, bg="#4287f5")
button5.place(relx=0.4, rely=0.5, relwidth=0.19, relheight=0.19)
button6 = tk.Button(root, bg="#4287f5")
button6.place(relx=0.6, rely=0.5, relwidth=0.19, relheight=0.19)
button7 = tk.Button(root, bg="#4287f5")
button7.place(relx=0.2, rely=0.7, relwidth=0.19, relheight=0.19)
button8 = tk.Button(root, bg="#4287f5")
button8.place(relx=0.4, rely=0.7, relwidth=0.19, relheight=0.19)
button9 = tk.Button(root, bg="#4287f5")
button9.place(relx=0.6, rely=0.7, relwidth=0.19, relheight=0.19)

root.mainloop()

# play_game()
