# Python Calculator by Kiran K K
from tkinter import *
from tkinter.messagebox import *
import math

window = Tk()
window.geometry("230x350")
window.title("I Calculate")
window.configure(bg='#000066')
window.resizable(0,0)
s0 = s1 = s2 = ""
val = ""
operatorVal = ""
lastVal = ""
famous=""
equalClickedOn = False

font=('verdana',10)
#------------------ function definitions------------------
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
     try:
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
     except Exception as e:
        showerror("Error",e)

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
    labelid.set(math.sqrt(int(labelid.get())))
def darkClicked():
    window.config(bg="#000000")
    b0.config(bg='#663300')
    b1.config(bg='#000000')
    b2.config(bg='#000000')
    b3.config(bg='#000000')
    b4.config(bg='#000000')
    b5.config(bg='#000000')
    b6.config(bg='#000000')
    b7.config(bg='#000000')
    b8.config(bg='#000000')
    b9.config(bg='#000000')
    ba.config(bg='#333')
    bs.config(bg='#333')
    bd.config(bg='#333')
    bm.config(bg='#333')
    beq.config(bg='#006600')
    bc.config(bg='#660000')
    bdot.config(bg='#000000')
    bback.config(bg='#660000')
    bdark.config(bg='#000000')
    blight.config(bg='#000000')
    bsqrt.config(bg='#660000')
    bpower.config(bg='#000000')
    label.config(bg='#fff',fg='#333333')
def lightClicked():
    window.config(bg='#000066')
    b0.config(bg='#cc3300')
    b1.config(bg='#000066')
    b2.config(bg='#000066')
    b3.config(bg='#000066')
    b4.config(bg='#000066')
    b5.config(bg='#000066')
    b6.config(bg='#000066')
    b7.config(bg='#000066')
    b8.config(bg='#000066')
    b9.config(bg='#000066')
    ba.config(bg='#0066ff')
    bs.config(bg='#0066ff')
    bd.config(bg='#0066ff')
    bm.config(bg='#0066ff')
    beq.config(bg='#009900')
    bc.config(bg='#003399')
    bdot.config(bg='#000066')
    bback.config(bg='#003399')
    bdark.config(bg='#000066')
    blight.config(bg='#000066')
    bsqrt.config(bg='#003399')
    bpower.config(bg='#000066')
    label.config(bg='#fff')

#------------------creating a text field------------------
labelid = StringVar()
label = Label(window, text="", width=20, height=2,textvariable=labelid,padx=5,pady=10,anchor='e',font='verdana 12 ',fg='#000066')

# ------------------creating buttons------------------
b0 = Button(window, text="0", width=5, height=2, command=num0Clicked,activebackground='#0000ff',
            activeforeground='#000000',bg='#cc3300',borderwidth=0,foreground='#fff',font=font)
b1 = Button(window, text="1", width=5, height=2, command=num1Clicked,bg='#000066',borderwidth=0,foreground='#fff',font=font,activebackground='#0033ff')
b2 = Button(window, text="2", width=5, height=2, command=num2Clicked,bg='#000066',borderwidth=0,foreground='#fff',font=font,activebackground='#0033ff')
b3 = Button(window, text="3", width=5, height=2, command=num3Clicked,bg='#000066',borderwidth=0,foreground='#fff',font=font,activebackground='#0033ff')
b4 = Button(window, text="4", width=5, height=2, command=num4Clicked,bg='#000066',borderwidth=0,foreground='#fff',font=font,activebackground='#0033ff')
b5 = Button(window, text="5", width=5, height=2, command=num5Clicked,bg='#000066',borderwidth=0,foreground='#fff',font=font,activebackground='#0033ff')
b6 = Button(window, text="6", width=5, height=2, command=num6Clicked,bg='#000066',borderwidth=0,foreground='#fff',font=font,activebackground='#0033ff')
b7 = Button(window, text="7", width=5, height=2, command=num7Clicked,bg='#000066',borderwidth=0,foreground='#fff',font=font,activebackground='#0033ff')
b8 = Button(window, text="8", width=5, height=2, command=num8Clicked,bg='#000066',borderwidth=0,foreground='#fff',font=font,activebackground='#0033ff')
b9 = Button(window, text="9", width=5, height=2, command=num9Clicked,bg='#000066',borderwidth=0,foreground='#fff',font=font,activebackground='#0033ff')

bd = Button(window, text="/", width=5, height=2,command=divClicked,bg='#0066ff',borderwidth=0,foreground='#fff',font=font,activebackground='#0033ff')
bm = Button(window, text="x", width=5, height=2,command=multClicked,bg='#0066ff',borderwidth=0,foreground='#fff',font=font,activebackground='#0033ff')
ba = Button(window, text="+", width=5, height=2, command=addClicked,bg='#0066ff',borderwidth=0,foreground='#fff',font=font,activebackground='#0033ff')
bs = Button(window, text="-", width=5, height=2,command=minusClicked,bg='#0066ff',borderwidth=0,foreground='#fff',font=font,activebackground='#0033ff')

beq = Button(window, text="=", width=5, height=2, command=equalClicked,bg='#009900',borderwidth=0,foreground='#fff',font=font,activebackground='#0033ff')
bc = Button(window, text="C", width=5, height=2,command=clearClicked,bg='#003399',borderwidth=0,foreground='#fff',font=font ,activebackground='#0033ff')
bdot = Button(window, text=".", width=5, height=2, command=dotClicked,bg='#000066',borderwidth=0,foreground='#fff',font=font,activebackground='#0033ff')
bback = Button(window,text="back",width=5, height=2, command=backSpaceClicked,bg='#003399',borderwidth=0,foreground='#fff',font=font,activebackground='#0033ff')
bpower = Button(window,text="^",width=5, height=2, command=powerClicked,bg='#000066',borderwidth=0,foreground='#fff',font=font,activebackground='#0033ff')
bsqrt = Button(window,text="√",width=5, height=2, command=squareRoot,bg='#003399',borderwidth=0,foreground='#fff',font=font,activebackground='#0033ff')
bdark = Button(window,text="DARK",width=11, height=2, command=darkClicked,bg='#000066',borderwidth=0,foreground='#fff',font=font,activebackground='#0033ff')
blight = Button(window,text="LIGHT",width=11, height=2, command=lightClicked,bg='#000066',borderwidth=0,foreground='#fff',font=font,activebackground='#0033ff')

#------------------ applying grid system to all elements------------------

label.grid(row=2, columnspan=4,pady=30,padx=7)
bc.grid(row=4,column=0)
bback.grid(row=4,column=1,)
bsqrt.grid(row=4,column=2)
bd.grid(row=4, column=3)

b7.grid(row=5, column=0)
b8.grid(row=5, column=1)
b9.grid(row=5, column=2)
bm.grid(row=5, column=3)

b4.grid(row=6, column=0)
b5.grid(row=6, column=1)
b6.grid(row=6, column=2)
bs.grid(row=6, column=3)

b1.grid(row=7, column=0)
b2.grid(row=7, column=1)
b3.grid(row=7, column=2)
ba.grid(row=7, column=3)

b0.grid(row=8, column=1)
bdot.grid(row=8, column=0)
bpower.grid(row=8,column=2)
beq.grid(row=8, column=3)
bdark.grid(row=9,column=0,columnspan=2)
blight.grid(row=9,column=2,columnspan=2)

#------------------ execution of calculator ends here------------------
window.mainloop()
