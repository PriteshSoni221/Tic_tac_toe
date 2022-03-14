import tkinter as tk
from tkinter import messagebox

# Global Variables
num_of_turns = 0
turn_of_X = True


def play(buttons):
    """Player will click on valid button and the mark will appear on the button."""
    global turn_of_X, num_of_turns
    if buttons["text"] == " " and turn_of_X == True:
        buttons["text"] = "X"
        turn_of_X = False
        check_if_game_over()
        num_of_turns += 1

    elif buttons["text"] == " " and turn_of_X == False:
        buttons["text"] = "O"
        turn_of_X = True
        check_if_game_over()
        num_of_turns += 1

    else:
        messagebox.showwarning(title="Warning!", message="Clicked already", )


def check_if_game_over():
    if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
            button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
            button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X' or
            button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
            button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
            button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
            button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
            button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
        quit_application("X")

    elif num_of_turns == 8:
        quit_application("")

    elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
          button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
          button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
          button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O' or
          button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
          button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
          button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):
        quit_application("O")
    """we are checking if the game is over or not by checking the win and tie conditions"""


def clear_button():
    """Clearing the sign from the buttons."""
    button1["text"] = " "
    button2["text"] = " "
    button3["text"] = " "
    button4["text"] = " "
    button5["text"] = " "
    button6["text"] = " "
    button7["text"] = " "
    button8["text"] = " "
    button9["text"] = " "


# def disableButton():
#     button1.configure(state='disabled')
#     button2.configure(state=DISABLED)
#     button3.configure(state=DISABLED)
#     button4.configure(state=DISABLED)
#     button5.configure(state=DISABLED)
#     button6.configure(state=DISABLED)
#     button7.configure(state=DISABLED)
#     button8.configure(state=DISABLED)
#     button9.configure(state=DISABLED)


def restart_game():
    global num_of_turns
    global turn_of_X
    """To restart the game we just need to clear sign from buttons and set number of turns to zero."""
    num_of_turns = 0
    turn_of_X = True
    clear_button()
    # disableButton()


def quit_application(winner):
    """Ask user to restart or quit the game."""
    if winner == "X" or winner == "O":
        message_box = tk.messagebox.askquestion("Tic Tac Toe", "{} has won the game.\n"
                                                               "Do want to quit the application".format(
                                                                   winner),
                                                icon='warning')
    else:
        message_box = tk.messagebox.askquestion("Tic Tac Toe", "It is a Draw!\nDo you want to quit the application",
                                                icon='warning')
    if message_box == 'yes':
        root.destroy()
    else:
        tk.messagebox.showinfo('Tic Tac Toe', "Restarting the game...")
        restart_game()


# From here I will define the GUI code
root = tk.Tk()
root.title("Tic Tac Toe")
min_width, min_height = 750, 700
root.minsize(min_width, min_height)
# given line of code will make our whole window transparent. I have commented it because it was not very pleasing to see
# root.wm_attributes("-alpha", 0.75)

background_image = tk.PhotoImage(file="./game.png")

background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

notice_label = tk.Label(
    root, text="Welcome to a tic tac toe game \n \t by Pritesh Soni.", font=("times new roman", 20))
notice_label.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)

# These are buttons with 0.19*0.19 relsize so that there is a thin line between them, makes it look pretty.

button1 = tk.Button(root, text=" ", command=lambda: play(
    button1), font=("times new roman", 22))
button1.place(relx=0.2, rely=0.3, relwidth=0.19, relheight=0.19)
button2 = tk.Button(root, text=" ", command=lambda: play(
    button2), font=("times new roman", 22))
button2.place(relx=0.4, rely=0.3, relwidth=0.19, relheight=0.19)
button3 = tk.Button(root, text=" ", command=lambda: play(
    button3), font=("times new roman", 22))
button3.place(relx=0.6, rely=0.3, relwidth=0.19, relheight=0.19)
button4 = tk.Button(root, text=" ", command=lambda: play(
    button4), font=("times new roman", 22))
button4.place(relx=0.2, rely=0.5, relwidth=0.19, relheight=0.19)
button5 = tk.Button(root, text=" ", command=lambda: play(
    button5), font=("times new roman", 22))
button5.place(relx=0.4, rely=0.5, relwidth=0.19, relheight=0.19)
button6 = tk.Button(root, text=" ", command=lambda: play(
    button6), font=("times new roman", 22))
button6.place(relx=0.6, rely=0.5, relwidth=0.19, relheight=0.19)
button7 = tk.Button(root, text=" ", command=lambda: play(
    button7), font=("times new roman", 22))
button7.place(relx=0.2, rely=0.7, relwidth=0.19, relheight=0.19)
button8 = tk.Button(root, text=" ", command=lambda: play(
    button8), font=("times new roman", 22))
button8.place(relx=0.4, rely=0.7, relwidth=0.19, relheight=0.19)
button9 = tk.Button(root, text=" ", command=lambda: play(
    button9), font=("times new roman", 22))

button1 = tk.Button(root, text=" ", command=lambda: play(
    button1), font=("times new roman", 22))
button1.place(relx=0.2, rely=0.3, relwidth=0.19, relheight=0.19)
button2 = tk.Button(root, text=" ", command=lambda: play(
    button2), font=("times new roman", 22))
button2.place(relx=0.4, rely=0.3, relwidth=0.19, relheight=0.19)
button3 = tk.Button(root, text=" ", command=lambda: play(
    button3), font=("times new roman", 22))
button3.place(relx=0.6, rely=0.3, relwidth=0.19, relheight=0.19)
button4 = tk.Button(root, text=" ", command=lambda: play(
    button4), font=("times new roman", 22))
button4.place(relx=0.2, rely=0.5, relwidth=0.19, relheight=0.19)
button5 = tk.Button(root, text=" ", command=lambda: play(
    button5), font=("times new roman", 22))
button5.place(relx=0.4, rely=0.5, relwidth=0.19, relheight=0.19)
button6 = tk.Button(root, text=" ", command=lambda: play(
    button6), font=("times new roman", 22))
button6.place(relx=0.6, rely=0.5, relwidth=0.19, relheight=0.19)
button7 = tk.Button(root, text=" ", command=lambda: play(
    button7), font=("times new roman", 22))
button7.place(relx=0.2, rely=0.7, relwidth=0.19, relheight=0.19)
button8 = tk.Button(root, text=" ", command=lambda: play(
    button8), font=("times new roman", 22))
button8.place(relx=0.4, rely=0.7, relwidth=0.19, relheight=0.19)
button9 = tk.Button(root, text=" ", command=lambda: play(
    button9), font=("times new roman", 22))

button9.place(relx=0.6, rely=0.7, relwidth=0.19, relheight=0.19)

clear_screen = tk.Button(root, text="Clear Screen", font=(
    "times new roman", 22), command=restart_game)
clear_screen.place(relx=0.38, rely=0.21, relwidth=0.24, relheight=0.08)

root.mainloop()
