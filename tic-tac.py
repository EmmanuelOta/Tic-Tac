from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Tic-Tac")
root.resizable(0, 0)

clicked = True
count = 0

btn = Button(root, width=7, height=4, text=" ", font=("Consolas", 14), command=lambda: update(btn))
btn.grid(row=0, column=0)

btn1 = Button(root, width=7, height=4, text=" ", font=("Consolas", 14), command=lambda: update(btn1))
btn1.grid(row=0, column=1)

btn2 = Button(root, width=7, height=4, text=" ", font=("Consolas", 14), command=lambda: update(btn2))
btn2.grid(row=0, column=2)

btn3 = Button(root, width=7, height=4, text=" ", font=("Consolas", 14), command=lambda: update(btn3))
btn3.grid(row=1, column=0)

btn4 = Button(root, width=7, height=4, text=" ", font=("Consolas", 14), command=lambda: update(btn4))
btn4.grid(row=1, column=1)

btn5 = Button(root, width=7, height=4, text=" ", font=("Consolas", 14), command=lambda: update(btn5))
btn5.grid(row=1, column=2)

btn6 = Button(root, width=7, height=4, text=" ", font=("Consolas", 14), command=lambda: update(btn6))
btn6.grid(row=2, column=0)

btn7 = Button(root, width=7, height=4, text=" ", font=("Consolas", 14), command=lambda: update(btn7))
btn7.grid(row=2, column=1)

btn8 = Button(root, width=7, height=4, text=" ", font=("Consolas", 14), command=lambda: update(btn8))
btn8.grid(row=2, column=2)


def reset():
    global btn
    global btn1
    global btn2
    global btn3
    global btn4
    global btn5
    global btn6
    global btn7
    global btn8

    btn.config(text=" ")
    btn1.config(text=" ")
    btn2.config(text=" ")
    btn3.config(text=" ")
    btn4.config(text=" ")
    btn5.config(text=" ")
    btn6.config(text=" ")
    btn7.config(text=" ")
    btn8.config(text=" ")


def update(buttons):
    global clicked
    global count

    if buttons["text"] == " " and clicked is True:
        buttons.config(text="x")
        clicked = False
        count += 1

        # checking if X won row by row
        if btn["text"] == "x" and btn1["text"] == "x" and btn2["text"] == "x":
            messagebox.showerror("Tic-Tac","X has won!😃😀")
            reset()
        elif btn3["text"] == "x" and btn4["text"] == "x" and btn5["text"] == "x":
            messagebox.showinfo("Tic-Tac","X has won")
            reset()
        elif btn6["text"] == "x" and btn7["text"] == "x" and btn8["text"] == "x":
            messagebox.showinfo("Tic-Tac","X has won")
            reset()

        # checking if X won column by column
        elif btn["text"] == "x" and btn3["text"] == "x" and btn6["text"] == "x":
            messagebox.showinfo("Tic-Tac","X has won")
            reset()
        elif btn1["text"] == "x" and btn4["text"] == "x" and btn7["text"] == "x":
            messagebox.showinfo("Tic-Tac","X has won")
            reset()
        elif btn2["text"] == "x" and btn5["text"] == "x" and btn8["text"] == "x":
            messagebox.showinfo("Tic-Tac","X has won")
            reset()

        #checking if X won diagonally
        elif btn["text"] == "x" and btn4["text"] == "x" and btn8["text"] == "x":
            messagebox.showinfo("Tic-Tac", "X has won")
            reset()
        elif btn2["text"] == "x" and btn4["text"] == "x" and btn6["text"] == "x":
            messagebox.showinfo("Tic-Tac","X has won")
            reset()

    elif buttons["text"] == " " and clicked is False:
        buttons.config(text="o") 
        clicked = True
        count += 1
        
        #checking if O has won row by row
        if btn["text"] == "o" and btn1["text"] == "o" and btn2["text"] == "o":
            messagebox.showinfo("Tic-Tac","O has won")
            reset()
        elif btn3["text"] == "o" and btn4["text"] == "o" and btn5["text"] == "o":
            messagebox.showinfo("Tic-Tac","O has won")
            reset()
        elif btn6["text"] == "o" and btn7["text"] == "o" and btn8["text"] == "o":
            messagebox.showinfo("Tic-Tac","O has won")
            reset()

        # checking if O won column by column
        elif btn["text"] == "o" and btn3["text"] == "o" and btn6["text"] == "o":
            messagebox.showinfo("Tic-Tac","O has won")
            reset()
        elif btn1["text"] == "o" and btn4["text"] == "o" and btn7["text"] == "o":
            messagebox.showinfo("Tic-Tac","O has won")
            reset()
        elif btn2["text"] == "o" and btn5["text"] == "o" and btn8["text"] == "o":
            messagebox.showinfo("Tic-Tac","O has won")
            reset()

        # checking if O won diagonlly
        elif btn2["text"] == "o" and btn4["text"] == "o" and btn6["text"] == "o":
            messagebox.showinfo("Tic-Tac","O has won")
            reset()
        elif btn["text"] == "o" and btn4["text"] == "o" and btn8["text"] == "o":
            messagebox.showinfo("Tic-Tac","O has won")
            reset()

    else:
        messagebox.showerror("Tic-Tac", "Hey click on the right box!")


menu = Menu(root)
option = Menu(menu, tearoff=False)
menu.add_cascade(menu=option, label="Option")
option.add_command(label="Reset", command=lambda: reset())
option.add_separator()

root.config(menu=menu)
root.mainloop()
