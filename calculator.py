from tkinter import *


def buttonPressed(num):
    global equationText
    equationText = equationText + str(num)
    equationLabel.set(equationText)

def equals():
        global equationText
        try:
            total = str(eval(equationText)) #eval automatically calculate everything
            equationLabel.set(total)
            equationText = total
        except ZeroDivisionError:
             equationLabel.set("arithmetic error")
             equationText = ""
        except SyntaxError:
             equationLabel.set("Syntax error")
             equationText = ""
def clear():
    global equationText
    equationText = ""
    equationLabel.set(equationText)



window = Tk()
window.title("Calculator Program")
#icon = PhotoImage(file="Noura.png")
window.geometry("500x500")
window.config(background="#9E9E9E")


equationText = ""
equationLabel = StringVar()

label = Label(window, textvariable=equationLabel , font=("consolas",20), bg = "white", width=24, height = 2)
label.pack()

frame = Frame(window)
frame.pack()
button1 = Button(frame, text = 1 , height=4, width = 9, font = 35, command= lambda:buttonPressed(1))
button1.grid(row = 0, column=0)

button2 = Button(frame, text = 2 , height=4, width = 9, font = 35, command= lambda:buttonPressed(2))
button2.grid(row = 0, column=1)

button3 = Button(frame, text = 3 , height=4, width = 9, font = 35, command= lambda:buttonPressed(3))
button3.grid(row = 0, column=2)

button4 = Button(frame, text = 4 , height=4, width = 9, font = 35, command= lambda:buttonPressed(4))
button4.grid(row = 1, column=0)

button5 = Button(frame, text = 5 , height=4, width = 9, font = 35, command= lambda:buttonPressed(5))
button5.grid(row = 1, column=1)

button6 = Button(frame, text = 6 , height=4, width = 9, font = 35, command= lambda:buttonPressed(6))
button6.grid(row = 1, column=2)

button7 = Button(frame, text = 7 , height=4, width = 9, font = 35, command= lambda:buttonPressed(7))
button7.grid(row = 2, column=0)

button8 = Button(frame, text = 8 , height=4, width = 9, font = 35, command= lambda:buttonPressed(8))
button8.grid(row = 2, column=1)

button9 = Button(frame, text = 9 , height=4, width = 9, font = 35, command= lambda:buttonPressed(9))
button9.grid(row = 2, column=2)

button0 = Button(frame, text = "0" , height=4, width = 9, font = 35, command= lambda:buttonPressed(0))
button0.grid(row = 3, column=0)

buttonPlus = Button(frame, text = "+" , height=4, width = 9, font = 35, command= lambda:buttonPressed("+"))
buttonPlus.grid(row = 0, column=3)

buttonMinus = Button(frame, text = "-" , height=4, width = 9, font = 35, command= lambda:buttonPressed("-"))
buttonMinus.grid(row = 1, column=3)

buttonMulti = Button(frame, text = "*" , height=4, width = 9, font = 35, command= lambda:buttonPressed("*"))
buttonMulti.grid(row = 2, column=3)

buttonDiv = Button(frame, text = "/" , height=4, width = 9, font = 35, command= lambda:buttonPressed("/"))
buttonDiv.grid(row = 3, column=3)

buttonEqual = Button(frame, text = "=" , height=4, width = 9, font = 35, command= equals)
buttonEqual.grid(row = 3, column=2)

buttonDecimal = Button(frame, text = "." , height=4, width = 9, font = 35, command= lambda:buttonPressed("."))
buttonDecimal.grid(row = 3, column=1)


buttonClear = Button(window, text = "Clear" , height=4, width = 12, font = ("consolas",20), command= clear)
buttonClear.pack()
window = mainloop()