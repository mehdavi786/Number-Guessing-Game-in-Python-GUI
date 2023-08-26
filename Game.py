from tkinter import *
from random import randint

#function to disable the state of guess button and display the results.
def showresult():
    guess_btn.config(state=DISABLED)
    win_text.config(text=f"You guessed in {score.get()} tries. You won!")

def showhelp():
    help_text.config(text="Hello user! In this game, you will be asked to guess a number using trial and error. Hints will be provided at every guess.", font='Arial 9', wraplength=350)

#two same functions to compare numbers and provide hints.
#Function below is triggered when enter key is used.
def comparefuncenter(event):
    score.set(score.get() + 1)
    if var.get() == value.get():
        showresult()
    elif var.get() - value.get() <= 3 and var.get() - value.get() >= -3:
        help_text.config(text="Your guess is almost right.", font='Arial 9', wraplength=350)
    else:
        help_text.config(text="Your guess is very far from the generated number.", font='Arial 9', wraplength=350)

#Function below is triggered when guess button is clicked.
def comparefunc():
    score.set(score.get() + 1)
    if var.get() == value.get():
        showresult()

#Function to start game
def startgame():
    #generate a random number
    value.set(randint(0,10))
    
    help_text.config(text="")
    win_text.config(text="")

    #set intitial score to 0
    score.set(0)
    
    #display guess button and input field.
    field.pack(pady=15)
    field.bind('<Return>', comparefuncenter)

    guess_btn.pack(pady=15)
    guess_btn.config(state=NORMAL)

#intitialize gui window
root = Tk()

#set title
root.title("Guessing Game")

#set default opening and max size of gui window
root.geometry("400x300")
root.minsize(width=100, height=100)

# Center align the h1 label using pack
h1 = Label(root, text="Guessing Game!", font="arial 15 italic", pady=15)
h1.pack(side="top", fill="both", expand=True)  # Fill and expand to center

# Place the start_btn and help_btn side by side and centered
button_frame = Frame(root)
button_frame.pack(side="top", fill="both", expand=True, padx=120)

start_btn = Button(button_frame, fg='green', text='Start Game', command=startgame)
help_btn = Button(button_frame, fg='black', text='Instructions', command=showhelp)
start_btn.pack(side="left", padx=5)
help_btn.pack(side="left", padx=5)

#Text to display instructions and hints.
help_text = Label(root, fg='black', text='')
help_text.pack(side='top', padx=25)

#text to display final result.
win_text = Label(root, fg='black', text='')
win_text.pack(side='bottom', padx=25)

#variables for score, random number and input number.
value = IntVar()
var = IntVar()
score = IntVar()

#input field and guess button
field = Entry(root, textvariable=var)
guess_btn = Button(fg='red', text='Guess!', command=comparefunc)

# Start the program
root.mainloop()
