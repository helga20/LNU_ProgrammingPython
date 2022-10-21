# для ЛР №2
from tkinter import *
from tkinter.messagebox import showwarning

def coordN(x, y):
    if ((x-1)**2+y**2<=4 and x<= 1) or (y <= -x+3 and y >= x-3): 
        return 'yes'
    else : 
        return 'no'

def harshad(number):
    copy_number = number
    digit_sum  = 0
    while number > 0 :
        digit_sum +=  number%10
        number = number//10
    if copy_number%digit_sum == 0:
       return 'yes'
    else:
        return 'no'

def verify():
    try:
        x_ = float(xEntry.get())
        y_ = float(yEntry.get())
        N_ = int(NEntry.get())
    except:
        showwarning('Некоректні дані', 'Значення повині бути числами')
        return None
    color = show.get()
    text = ''
    coord = coordN(x_, y_)
    numberN = harshad(N_)
    result['fg'] = color
    if color  == 'red':
        coord, numberN
    elif color == 'green':
        coord, numberN
    else:
        coord, numberN

    if showC.get():
        text += f'Точка в середині рисунка?\n{coord}\n\n'
    if showN.get():
        text += f'Число N є числом харшад?\n{numberN}\n\n'
    result.insert('1.0', text)
        
def clear():
    xEntry.delete(0, END)
    yEntry.delete(0, END)
    NEntry.delete(0, END)
    result.delete('1.0', END)


root = Tk()
root.title('Перевірка')

Label(root, text = 'Координати точки:').grid(row=0, column=0, rowspan=2)
Label(root, text = 'x').grid(row=0, column=1)
Label(root, text = 'y').grid(row=1, column=1)
Label(root, text = 'Число N:').grid(row=2, column=0)

xEntry = Entry(root)
xEntry.grid(row=0, column=2)

yEntry = Entry(root)
yEntry.grid(row=1, column=2)

NEntry = Entry(root)
NEntry.grid(row=2, column=2)

showC, showN = IntVar(), IntVar()
Checkbutton(root, text='Чи є точка всередині рисунка',\
     var=showC).grid(row=3, column=0)
Checkbutton(root, text='Чи є N числом харшад',\
     var=showN).grid(row=3, column=1)

Label(root, text='Результати:').grid(row=4, column=0, columnspan=2)

showing_frame = Frame(root)
showing_frame.grid(row=5, column=0, columnspan=2)

show = StringVar()

black = Radiobutton(showing_frame, var=show, value='black', fg="black")
black['text'] = 'чорний'
black.grid(row=0, column=0)
red = Radiobutton(showing_frame, var=show, value='red', fg="red")
red['text'] = 'червоний' 
red.grid(row=0, column=1)
green = Radiobutton(showing_frame, var=show, value='green', fg="green")
green['text'] = 'зелений' 
green.grid(row=0, column=2)
show.set('b')

result = Text(root, width=25, height=5)
result.grid(row=6, column=0, rowspan=2)

b_frame = Frame(root)
b_frame.grid(row=6, column=1, columnspan=2)

Button(b_frame, text='Перевірити', command=verify, bg="white", fg="black",\
     relief=RAISED, activebackground='green').grid(row=6, column=1)
Button(b_frame, text='Очистити', command=clear, bg="white", fg="black",\
     relief=SUNKEN, activebackground='red').grid(row=7, column=1)

root.mainloop()
