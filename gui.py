from tkinter import *

window=Tk()
def button_press(num):
    pass

equation_text=""
equation_label= StringVar()

window.geometry("500x680")
window.title("Calculator")
icon=PhotoImage(file="images.png")
window.iconphoto(True,icon)
window.config(background="black")
label=Label(window,textvariable=equation_label,
            font=('Arial',40,'italic','bold'),
            width=14,height=2,
            fg="#73d907",
            bg='#180e45',
            relief='sunken',
            bd=10
            )
label.pack()
frame=Frame(window)
frame.pack()
button1=Button(frame, text=1,height=4,width=9,font=35,
               command=lambda: button_press(1))
button1.grid(row=0,column=0)
button2=Button(frame, text=2,height=4,width=9,font=35,
               command=lambda: button_press(2))
button2.grid(row=0,column=1)
button3=Button(frame, text=3,height=4,width=9,font=35,
               command=lambda: button_press(3))
button3.grid(row=0,column=2)
button4=Button(frame, text=4,height=4,width=9,font=35,
               command=lambda: button_press(4))
button4.grid(row=1,column=0)
button5=Button(frame, text=5,height=4,width=9,font=35,
               command=lambda: button_press(5))
button5.grid(row=1,column=1)
button6=Button(frame, text=6,height=4,width=9,font=35,
               command=lambda: button_press(6))
button6.grid(row=1,column=2)
button7=Button(frame, text=7,height=4,width=9,font=35,
               command=lambda: button_press(7))
button7.grid(row=2,column=0)
button8=Button(frame, text=8,height=4,width=9,font=35,
               command=lambda: button_press(8))
button8.grid(row=2,column=1)
button9=Button(frame, text=9,height=4,width=9,font=35,
               command=lambda: button_press(9))
button9.grid(row=2,column=2)
buttonsum=Button(frame, text='+',height=4,width=9,font=35,
               command=lambda: button_press('+'))
buttonsum.grid(row=0,column=3)
buttonminus=Button(frame, text='-',height=4,width=9,font=35,
               command=lambda: button_press('-'))
buttonminus.grid(row=1,column=3)
buttonmult=Button(frame, text='*',height=4,width=9,font=35,
               command=lambda: button_press('*'))
buttonmult.grid(row=2,column=3)
button0=Button(frame, text='0',height=4,width=9,font=35,
               command=lambda: button_press('0'))
button0.grid(row=3,column=0)
buttondot=Button(frame, text='.',height=4,width=9,font=35,
               command=lambda: button_press('.'))
buttondot.grid(row=3,column=1)
buttondiv=Button(frame, text='/',height=4,width=9,font=35,
               command=lambda: button_press('/'))
buttondiv.grid(row=3,column=2)
buttonequal=Button(frame, text='=',height=4,width=9,font=35,
               command=lambda: button_press('='))
buttonequal.grid(row=3,column=3)



window.mainloop()




