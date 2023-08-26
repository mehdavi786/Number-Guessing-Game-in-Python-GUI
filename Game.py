from tkinter import *
from random import randint

def showresult():
    print("You won!")
    print(f"You guessed in {count.get()} tries.")
    guess_btn.config(state=DISABLED)
    win_text.config(text=f"You guessed in {count.get()} tries. You won!")

def showhelp():
    help_text.config(text="Hello user! In this game, you will be asked to guess a number using trial and error. Hints will be provided at every guess.", font='Arial 9', wraplength=350)

#function to compare numbers
def comparefuncenter(event):
    count.set(count.get() + 1)
    print(value.get())
    if var.get() == value.get():
        showresult()
    elif var.get() - value.get() <= 3 and var.get() - value.get() >= -3:
        help_text.config(text="Your guess is almost right.", font='Arial 9', wraplength=350)
    else:
        help_text.config(text="Your guess is very far from the generated number.", font='Arial 9', wraplength=350)
def comparefunc():
    count.set(count.get() + 1)
    print(value.get())
    if var.get() == value.get():
        showresult()
def startgame():
    value.set(randint(0,10))
    help_text.config(text="")
    win_text.config(text="")

    # make number input field
    count.set(0)

    field.pack(pady=15)
    field.bind('<Return>', comparefuncenter)

    # make guess button
    guess_btn.pack(pady=15)
    guess_btn.config(state=NORMAL)

root = Tk()
root.title("Guessing Game")
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

help_text = Label(root, fg='black', text='')
help_text.pack(side='top', padx=25)

win_text = Label(root, fg='black', text='')
win_text.pack(side='bottom', padx=25)

# Place the input field and guess_btn side by side in the next line using pack
input_frame = Frame(root)
input_frame.pack(side="top", fill="both", expand=True)

value = IntVar()
var = IntVar()
count = IntVar()

field = Entry(root, textvariable=var)
guess_btn = Button(fg='red', text='Guess!', command=comparefunc)

# Start the program
root.mainloop()
