from tkinter import *
from tkinter import ttk
from tkinter import messagebox


gui = Tk()
gui.title('daily tasks')


###########Monday

#label
ML = Label(gui,text='Monday',fg='red')
ML.place(x=30,y=20)

#Morning button
def MmbFc():
    text = 'Working out'
    messagebox.showinfo('Monday Morning Task',text)

Mmb = ttk.Button(gui,text='Morning Task',command=MmbFc)
Mmb.place(x=30,y=60)

#Noon button
def MnbFc():
    text = 'Meditation'
    messagebox.showinfo('Monday Noon Task',text)

Mnb = ttk.Button(gui,text='Noon Task',command=MnbFc)
Mnb.place(x=130,y=60)

#Evening button
def MebFc():
    text = 'Relaxing'
    messagebox.showinfo('Monday Evening Task',text)

Meb = ttk.Button(gui,text='Evening Task',command=MebFc)
Meb.place(x=230,y=60)


###########Tuesday

#label
TL = Label(gui,text='Tuesday',fg='blue')
TL.place(x=30,y=100)

#Morning button
def TmbFc():
    text = 'Working out'
    messagebox.showinfo('Tuesday Morning Task',text)

Tmb = ttk.Button(gui,text='Morning Task',command=TmbFc)
Tmb.place(x=30,y=140)

#Noon button
def TnbFc():
    text = 'Meditation'
    messagebox.showinfo('Tuesday Noon Task',text)

Tnb = ttk.Button(gui,text='Noon Task',command=TnbFc)
Tnb.place(x=130,y=140)

#Evening button
def TebFc():
    text = 'Relaxing'
    messagebox.showinfo('Tuesday Evening Task',text)

Teb = ttk.Button(gui,text='Evening Task',command=TebFc)
Teb.place(x=230,y=140)

###########Wednesday

#label
WL = Label(gui,text='Wednesday',fg='green')
WL.place(x=30,y=180)

#Morning button
def WmbFc():
    text = 'Working out'
    messagebox.showinfo('Wednesday Morning Task',text)

Wmb = ttk.Button(gui,text='Morning Task',command=WmbFc)
Wmb.place(x=30,y=220)

#Noon button
def WnbFc():
    text = 'Meditation'
    messagebox.showinfo('Wednesday Noon Task',text)

Wnb = ttk.Button(gui,text='Noon Task',command=WnbFc)
Wnb.place(x=130,y=220)

#Evening button
def WebFc():
    text = 'Relaxing'
    messagebox.showinfo('Wednesday Evening Task',text)

Web = ttk.Button(gui,text='Evening Task',command=WebFc)
Web.place(x=230,y=220)


###########Thursday

#label
ThL = Label(gui,text='Thursday',fg='pink')
ThL.place(x=30,y=260)

#Morning button
def ThmbFc():
    text = 'Working out'
    messagebox.showinfo('Thursday Morning Task',text)

Thmb = ttk.Button(gui,text='Morning Task',command=ThmbFc)
Thmb.place(x=30,y=300)

#Noon button
def ThnbFc():
    text = 'Meditation'
    messagebox.showinfo('Thursday Noon Task',text)

Thnb = ttk.Button(gui,text='Noon Task',command=ThnbFc)
Thnb.place(x=130,y=300)

#Evening button
def ThebFc():
    text = 'Relaxing'
    messagebox.showinfo('Thursday Evening Task',text)

Theb = ttk.Button(gui,text='Evening Task',command=ThebFc)
Theb.place(x=230,y=300)

###########Friday

#label
ThL = Label(gui,text='Friday',fg='purple')
ThL.place(x=30,y=340)

#Morning button
def FmbFc():
    text = 'Working out'
    messagebox.showinfo('Friday Morning Task',text)

Fmb = ttk.Button(gui,text='Morning Task',command=FmbFc)
Fmb.place(x=30,y=380)

#Noon button
def FnbFc():
    text = 'Meditation'
    messagebox.showinfo('Friday Noon Task',text)

Fnb = ttk.Button(gui,text='Noon Task',command=FnbFc)
Fnb.place(x=130,y=380)

#Evening button
def FebFc():
    text = 'Relaxing'
    messagebox.showinfo('Friday Evening Task',text)

Feb = ttk.Button(gui,text='Evening Task',command=FebFc)
Feb.place(x=230,y=380)



gui.mainloop()
