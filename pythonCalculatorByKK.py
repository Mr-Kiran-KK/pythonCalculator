# python calculator

from tkinter import *
window=Tk()
window.geometry("200x200")
window.title("I Calculate")
window.configure(bg='#456A8F')

#function definitions

# creating a text field
label=Label(window,text="",width=26)

# creating buttons
b0=Button(text="0",width=3,height=1)
b1=Button(text="1",width=3,height=1)
b2=Button(text="2",width=3,height=1)
b3=Button(text="3",width=3,height=1)
b4=Button(text="4",width=3,height=1)
b5=Button(text="5",width=3,height=1)
b6=Button(text="6",width=3,height=1)
b7=Button(text="7",width=3,height=1)
b8=Button(text="8",width=3,height=1)
b9=Button(text="9",width=3,height=1)

bd=Button(text="/",width=3,height=1)
bm=Button(text="x",width=3,height=1)
ba=Button(text="+",width=3,height=1)
bs=Button(text="-",width=3,height=1)

beq=Button(text="=",width=3,height=1)
bc=Button(text="C",width=3,height=1)
bdot=Button(text=".",width=3,height=1)

# applying grid system to all elements
label.grid(row=0,columnspan=10,padx=6,pady=8)
b7.grid(row=1,column=1,padx=10,pady=8)
b8.grid(row=1,column=2,padx=10)
b9.grid(row=1,column=3,padx=10)
bd.grid(row=1,column=4,padx=10)

b4.grid(row=2,column=1,pady=8)
b5.grid(row=2,column=2)
b6.grid(row=2,column=3)
bm.grid(row=2,column=4)

b1.grid(row=3,column=1,pady=8)
b2.grid(row=3,column=2)
b3.grid(row=3,column=3)
bs.grid(row=3,column=4)

bc.grid(row=4,column=1,pady=8)
bdot.grid(row=4,column=2)
beq.grid(row=4,column=3)
ba.grid(row=4,column=4)







#arranging elements


# execution of calculator ends here
window.mainloop()
