# python calculator
from tkinter import *

window = Tk()
window.geometry("200x200")
window.title("I Calculate")
window.configure(bg='#456A8F')
s0 = s1 = s2 = ""
val = ""
operatorVal = ""
lastVal = ""


# function definitions
def num0Clicked():
    global val
    global lastVal
    if val == "":
        val = val + "0"
        labelid.set(val)
    else:
        lastVal = operatorVal + "0"
        labelid.set(lastVal)


def num1Clicked():
    global val
    global lastVal
    global s0,s2
    if val == "":
        val = val + "1"

        labelid.set("1")
        s0 = float(val)
    else:

        lastVal = operatorVal + "1"
        labelid.set(lastVal)
        s2 = float(val)

def num2Clicked():
    global val
    global lastVal
    if val == "":
        val = val + "2"
        labelid.set(val)
    else:
        lastVal = operatorVal + "2"
        labelid.set(lastVal)


def num3Clicked():
    global val
    global lastVal
    if val == "":
        val = val + "3"
        labelid.set(val)
    else:
        lastVal = operatorVal + "3"
        labelid.set(lastVal)


def num4Clicked():
    global val
    global lastVal
    if val == "":
        val = val + "4"
        labelid.set(val)
    else:
        lastVal = operatorVal + "4"
        labelid.set(lastVal)


def num5Clicked():
    global val
    global lastVal
    if val == "":
        val = val + "5"
        labelid.set(val)
    else:
        lastVal = operatorVal + "5"
        labelid.set(lastVal)


def num6Clicked():
    global val
    global lastVal
    if val == "":
        val = val + ""
        labelid.set(val)
    else:
        lastVal = operatorVal + "6"
        labelid.set(lastVal)


def num7Clicked():
    global val
    global lastVal
    if val == "":
        val = val + "7"
        labelid.set(val)
    else:
        lastVal = operatorVal + "7"
        labelid.set(lastVal)


def num8Clicked():
    global val
    global lastVal
    if val == "":
        val = val + "8"
        labelid.set(val)
    else:
        lastVal = operatorVal + "8"
        labelid.set(lastVal)


def num9Clicked():
    global val
    global lastVal
    if val == "":
        val = val + "9"
        labelid.set(val)
    else:
        lastVal = operatorVal + "9"
        labelid.set(lastVal)


def dotClicked():
    global val
    val = val + "."
    labelid.set(val)


def addClicked():
    global operatorVal
    global s1
    s1 = "+"
    operatorVal = val + s1
    labelid.set(operatorVal)
def minusClicked():
    global operatorVal
    global s1
    s1 = "-"
    operatorVal = val + s1
    labelid.set(operatorVal)
def multClicked():
    global operatorVal
    global s1
    s1 = "x"
    operatorVal = val + s1
    labelid.set(operatorVal)
def divClicked():
    global operatorVal
    global s1
    s1 = "/"
    operatorVal = val + s1
    labelid.set(operatorVal)


def equalClicked():
    if s1 == "+":

        temp = s0 + s2

        labelid.set(temp)

    elif s1 == "-":
        temp = s0 - s2

        labelid.set(temp)
    elif s1 == "x":
        temp = s0 * s2
        labelid.set(temp)
    elif s1 == "/":
        temp = s0 / s2
        labelid.set(temp)
    else:
        print("hai")



# creating a text field
labelid = StringVar()
label = Label(window, text="", width=26, textvariable=labelid, anchor=E)

# creating buttons
b0 = Button(window, text="0", width=3, height=1, command=num0Clicked)
b1 = Button(window, text="1", width=3, height=1, command=num1Clicked)
b2 = Button(window, text="2", width=3, height=1, command=num2Clicked)
b3 = Button(window, text="3", width=3, height=1, command=num3Clicked)
b4 = Button(window, text="4", width=3, height=1, command=num4Clicked)
b5 = Button(window, text="5", width=3, height=1, command=num5Clicked)
b6 = Button(window, text="6", width=3, height=1, command=num6Clicked)
b7 = Button(window, text="7", width=3, height=1, command=num7Clicked)
b8 = Button(window, text="8", width=3, height=1, command=num8Clicked)
b9 = Button(window, text="9", width=3, height=1, command=num9Clicked)

bd = Button(window, text="/", width=3, height=1,command=divClicked)
bm = Button(window, text="x", width=3, height=1,command=multClicked)
ba = Button(window, text="+", width=3, height=1, command=addClicked)
bs = Button(window, text="-", width=3, height=1,command=minusClicked)

beq = Button(window, text="=", width=3, height=1, command=equalClicked)
bc = Button(window, text="C", width=3, height=1)
bdot = Button(window, text=".", width=3, height=1, command=dotClicked)

# applying grid system to all elements
label.grid(row=0, columnspan=10, padx=6, pady=8)
b7.grid(row=1, column=1, padx=10, pady=8)
b8.grid(row=1, column=2, padx=10)
b9.grid(row=1, column=3, padx=10)
bd.grid(row=1, column=4, padx=10)

b4.grid(row=2, column=1, pady=8)
b5.grid(row=2, column=2)
b6.grid(row=2, column=3)
bm.grid(row=2, column=4)

b1.grid(row=3, column=1, pady=8)
b2.grid(row=3, column=2)
b3.grid(row=3, column=3)
bs.grid(row=3, column=4)

b0.grid(row=4, column=1, pady=8)
bdot.grid(row=4, column=2)
beq.grid(row=4, column=3)
ba.grid(row=4, column=4)

# arranging elements


# execution of calculator ends here
window.mainloop()
