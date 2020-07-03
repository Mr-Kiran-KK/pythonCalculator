# python calculator
from tkinter import *
import math
window = Tk()
window.geometry("200x300")
window.title("I Calculate")
window.configure(bg='#456A8F')
s0 = s1 = s2 = ""
val = ""
operatorVal = ""
lastVal = ""
famous=""
equalClickedOn = False


# function definitions
def num0Clicked():
    global famous
    global val
    global lastVal
    global s0, s2, s1, s22, s00
    if s1 != "":
        s2=""
        s2 = s2 + "0"
        s22 = float(s2)
        famous=famous+s2
    else:
        s0=""
        s0 = s0 + "0"
        s00 = float(s0)
        famous=famous+s0
    labelid.set(famous)




def num1Clicked():
    global famous
    global val
    global lastVal
    global s0,s2,s1,s22,s00
    if s1 != "":
        s2 = ""
        s2 = s2 + "1"
        s22 = float(s2)
        famous = famous + s2
    else:
        s0 = ""
        s0 = s0 + "1"
        s00 = float(s0)
        famous = famous + s0
    labelid.set(famous)
def num2Clicked():
    global famous
    global val
    global lastVal
    global s0, s2, s1, s22, s00
    if s1 != "":
        s2 = ""
        s2 = s2 + "2"
        s22 = float(s2)
        famous = famous + s2
    else:
        s0 = ""
        s0 = s0 + "2"
        s00 = float(s0)
        famous = famous + s0
    labelid.set(famous)


def num3Clicked():
    global famous
    global val
    global lastVal
    global s0, s2, s1, s22, s00
    if s1 != "":
        s2 = ""
        s2 = s2 + "3"
        s22 = float(s2)
        famous = famous + s2
    else:
        s0 = ""
        s0 = s0 + "3"
        s00 = float(s0)
        famous = famous + s0
    labelid.set(famous)


def num4Clicked():
    global famous
    global val
    global lastVal
    global s0, s2, s1, s22, s00
    if s1 != "":
        s2 = ""
        s2 = s2 + "4"
        s22 = float(s2)
        famous = famous + s2
    else:
        s0 = ""
        s0 = s0 + "4"
        s00 = float(s0)
        famous = famous + s0
    labelid.set(famous)


def num5Clicked():
    global famous
    global val
    global lastVal
    global s0, s2, s1, s22, s00
    if s1 != "":
        s2 = ""
        s2 = s2 + "5"
        s22 = float(s2)
        famous = famous + s2
    else:
        s0 = ""
        s0 = s0 + "5"
        s00 = float(s0)
        famous = famous + s0
    labelid.set(famous)


def num6Clicked():
    global famous
    global val
    global lastVal
    global s0, s2, s1, s22, s00
    if s1 != "":
        s2 = ""
        s2 = s2 + "6"
        s22 = float(s2)
        famous = famous + s2
    else:
        s0 = ""
        s0 = s0 + "6"
        s00 = float(s0)
        famous = famous + s0
    labelid.set(famous)


def num7Clicked():
    global famous
    global val
    global lastVal
    global s0, s2, s1, s22, s00
    if s1 != "":
        s2 = ""
        s2 = s2 + "7"
        s22 = float(s2)
        famous = famous + s2
    else:
        s0 = ""
        s0 = s0 + "7"
        s00 = float(s0)
        famous = famous + s0
    labelid.set(famous)


def num8Clicked():
    global famous
    global val
    global lastVal
    global s0, s2, s1, s22, s00
    if s1 != "":
        s2 = ""
        s2 = s2 + "8"
        s22 = float(s2)
        famous = famous + s2
    else:
        s0 = ""
        s0 = s0 + "8"
        s00 = float(s0)
        famous = famous + s0
    labelid.set(famous)


def num9Clicked():
    global famous
    global val
    global lastVal
    global s0, s2, s1, s22, s00
    if s1 != "":
        s2 = ""
        s2 = s2 + "9"
        s22 = float(s2)
        famous = famous + s2
    else:
        s0 = ""
        s0 = s0 + "9"
        s00 = float(s0)
        famous = famous + s0
    labelid.set(famous)


def dotClicked():
    global val
    global lastVal
    global famous
    global s0, s2, s1, s22, s00
    if s1 != "":
        s2=""
        s2 = s2 + "."
        famous = famous + s2
    else:
        s0=""
        s0 = s0 + "."
        famous = famous + s0
    labelid.set(famous)


def addClicked():
    global famous
    global operatorVal
    global s1
    s1 = "+"
    operatorVal = s0 + s1
    famous=famous+s1
    labelid.set(famous)
def minusClicked():
    global famous
    global operatorVal
    global s1
    s1 = "-"
    operatorVal = s0 + s1
    famous = famous + s1
    labelid.set(famous)
def multClicked():
    global famous
    global operatorVal
    global s1
    s1 = "*"
    operatorVal = s0 + s1
    famous = famous + s1
    labelid.set(famous)
def divClicked():
    global famous
    global operatorVal
    global s1
    s1 = "/"
    operatorVal = s0 + s1
    famous = famous + s1
    labelid.set(famous)

def powerClicked():
    global famous
    global operatorVal
    global s1
    s1 = "^"
    operatorVal = s0 + s1
    famous=famous+s1
    labelid.set(famous)


def equalClicked():
        global s0,s2
        if s1 == "^":
            labelid.set(pow(int(s0),int(s2)))
            s0=s2=""


        else:
          global equalClickedOn
          answer=eval(famous)
          labelid.set("")
          labelid.set(answer)
          equalClickedOn = True



def clearClicked():
    global famous,s0,s1,s2
    s0=s1=s2=famous=""
    labelid.set(famous)

def backSpaceClicked():
    global famous
    if equalClickedOn == False:
         lengthOfFamous = len(famous) - 1
         newfamous = famous[0:lengthOfFamous]
         famous = newfamous
         labelid.set(famous)
    else:
        famous = ""
        labelid.set(famous)
def squareRoot():
    labelid.set( round(math.sqrt(int(labelid.get()))))













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
bc = Button(window, text="C", width=3, height=1,command=clearClicked)
bdot = Button(window, text=".", width=3, height=1, command=dotClicked)

bback = Button(window,text="back",width=3, height=1, command=backSpaceClicked)


bpower = Button(window,text="^",width=3, height=1, command=powerClicked)
bsqrt = Button(window,text="√",width=3, height=1, command=squareRoot)


# applying grid system to all elements
label.grid(row=0, columnspan=10, padx=6, pady=8)
b7.grid(row=2, column=1, padx=10, pady=8)
b8.grid(row=2, column=2, padx=10)
b9.grid(row=2, column=3, padx=10)
bd.grid(row=1, column=4, padx=10)

b4.grid(row=3, column=1, pady=8)
b5.grid(row=3, column=2)
b6.grid(row=3, column=3)
bm.grid(row=2, column=4)

b1.grid(row=4, column=1, pady=8)
b2.grid(row=4, column=2)
b3.grid(row=4, column=3)
bs.grid(row=3, column=4)

b0.grid(row=5, column=1, pady=8)
bdot.grid(row=5, column=2)
beq.grid(row=5, column=4)
ba.grid(row=4, column=4)
bc.grid(row=1,column=1,pady=8)
bback.grid(row=1,column=2)

bpower.grid(row=5,column=3)
bsqrt.grid(row=1,column=3)



# arranging elements


# execution of calculator ends here
window.mainloop()
