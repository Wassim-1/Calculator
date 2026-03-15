from tkinter import *
def run():
    window=Tk()
    def button_press(num):
        nonlocal equation_text
        if num=="=": 
            equation_text=equation_text.replace("%","/100")
            equation_text=equation_text.replace("mod","%")
            try:
                total=str(eval(equation_text))
                equation_label.set(total)
                equation_text=total
            except:
                equation_label.set("ERROR")
                equation_text=""

        
        elif num=="AC":
            equation_text=""
            equation_label.set(equation_text)
        else:
            equation_text=equation_text+str(num)
            equation_label.set(equation_text)


    equation_text=""
    equation_label= StringVar()

    window.geometry("510x725")
    window.title("Calculator")
    icon=PhotoImage(file="images.png")
    window.iconphoto(True,icon)
    window.config(background="black")
    label=Label(window,textvariable=equation_label,
            font=('Arial',40,'bold'),
            width=14,height=2,
            fg="#f30707",
            bg='#180e45',
            relief='sunken',
            bd=10
            )
    label.pack()
    frame=Frame(window)
    frame.pack()
    buttons=["AC","%","mod","/",
         "7","8","9","*",
         "4","5","6","-",
         "1","2","3","+",
         "00","0",".","="]
    col=0;
    row=0;
    for btn in buttons:
        Button(frame, text=btn,height=4,width=9,font=('Arial',12),
               command=lambda x=btn: button_press(x)).grid(row=row,column=col)
        col+=1
        if col>3:
            col=0
            row+=1
    window.mainloop()
run()





