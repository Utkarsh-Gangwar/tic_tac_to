from tkinter import *
import tkinter.messagebox
b0=' '
b1=' '
b2=' '
b3=' '
b4=' '
b5=' '
b6=' '
b7=' '
b8=' '
i=0
def match():
    global b0,b1,b2,b3,b4,b5,b6,b7,b8
    if b0==b4 and b4==b8 and b0!=' ':
        result(b0+'  wins!!')
    elif b2==b4 and b4==b6 and b2!=' ':
        result(b2+'  wins!!')
    elif b0==b1 and b1==b2 and b0!=' ':
        result(b0+'  wins!!')
    elif b3==b4 and b4==b5 and b3!=' ':
        result(b3+'  wins!!')
    elif b6==b7 and b7==b8 and b6!=' ':
        result(b6+'  wins!!')
    elif b0==b3 and b3==b6 and b0!=' ':
        result(b0+'  wins!!')
    elif b1==b4 and b4==b7 and b1!=' ':
        result(b1+'  wins!!')
    elif b2==b5 and b5==b8 and b2!=' ':
        result(b2+'  wins!!')
    elif b0!=' ' and b1!=' ' and b2!=' ' and b3!=' ' and b4!=' ' and b5!=' ' and b6!=' ' and b7!=' ' and b8!=' ':
        result('Match Draw')
def result(n):
    tkinter.messagebox.showinfo("result",n)
    r=tkinter.messagebox.askquestion('result','Do you want to play again?')
    if r=='yes':
        reset()
def reset():
    global b0,b1,b2,b3,b4,b5,b6,b7,b8
    b0=' '
    b1=' '
    b2=' '
    b3=' '
    b4=' '
    b5=' '
    b6=' '
    b7=' '
    b8=' '
    B0['text']=b0
    B1['text']=b1
    B2['text']=b2
    B3['text']=b3
    B4['text']=b4
    B5['text']=b5
    B6['text']=b6
    B7['text']=b7
    B8['text']=b8
def push0():
    global i
    global b0
    i=i+1
    if b0==' ':
        if i%2==0:
            cross(0)
        else:
            zero(0)
    else:
        i=i-1
def push1():
    global i
    global b1
    i=i+1
    if b1==' ':
        if i%2==0:
            cross(1)
        else:
            zero(1)
    else:
        i=i-1
def push2():
    global i
    global b2
    i=i+1
    if b2==' ':
        if i%2==0:
            cross(2)
        else:
            zero(2)
    else:
        i=i-1
def push3():
    global i
    global b3
    i=i+1
    if b3==' ':
        if i%2==0:
            cross(3)
        else:
            zero(3)
    else:
        i=i-1
def push4():
    global i
    global b4
    i=i+1
    if b4==' ':
        if i%2==0:
            cross(4)
        else:
            zero(4)
    else:
        i=i-1
def push5():
    global i
    global b5
    i=i+1
    if b5==' ':
        if i%2==0:
            cross(5)
        else:
            zero(5)
    else:
        i=i-1
def push6():
    global i
    global b6
    i=i+1
    if b6==' ':
        if i%2==0:
            cross(6)
        else:
            zero(6)
    else:
        i=i-1
def push7():
    global i
    global b7
    i=i+1
    if b7==' ':
        if i%2==0:
            cross(7)
        else:
            zero(7)
    else:
        i=i-1
def push8():
    global i
    global b8
    i=i+1
    if b8==' ':
        if i%2==0:
            cross(8)
        else:
            zero(8)
    else:
        i=i-1
def cross(n):
    global b0,b1,b2,b3,b4,b5,b6,b7,b8
    if n==0:
        b0='X'
        B0['text']=b0
    if n==1:
        b1='X'
        B1['text']=b1
    if n==2:
        b2='X'
        B2['text']=b2
    if n==3:
        b3='X'
        B3['text']=b3
    if n==4:
        b4='X'
        B4['text']=b4
    if n==5:
        b5='X'
        B5['text']=b5
    if n==6:
        b6='X'
        B6['text']=b6
    if n==7:
        b7='X'
        B7['text']=b7
    if n==8:
        b8='X'
        B8['text']=b8
    match()
def zero(n):
    global b0,b1,b2,b3,b4,b5,b6,b7,b8
    if n==0:
        b0='O'
        B0['text']=b0
    if n==1:
        b1='O'
        B1['text']=b1
    if n==2:
        b2='O'
        B2['text']=b2
    if n==3:
        b3='O'
        B3['text']=b3
    if n==4:
        b4='O'
        B4['text']=b4
    if n==5:
        b5='O'
        B5['text']=b5
    if n==6:
        b6='O'
        B6['text']=b6
    if n==7:
        b7='O'
        B7['text']=b7
    if n==8:
        b8='O'
        B8['text']=b8
    match()
root=Tk()
B0=Button(root,text=b0,command=push0,width=10,height=5)
B0.grid(row=0,column=0)
B1=Button(root,text=b0,command=push1,width=10,height=5)
B1.grid(row=0,column=1)
B2=Button(root,text=b0,command=push2,width=10,height=5)
B2.grid(row=0,column=2)
B3=Button(root,text=b0,command=push3,width=10,height=5)
B3.grid(row=1,column=0)
B4=Button(root,text=b0,command=push4,width=10,height=5)
B4.grid(row=1,column=1)
B5=Button(root,text=b0,command=push5,width=10,height=5)
B5.grid(row=1,column=2)
B6=Button(root,text=b0,command=push6,width=10,height=5)
B6.grid(row=2,column=0)
B7=Button(root,text=b0,command=push7,width=10,height=5)
B7.grid(row=2,column=1)
B8=Button(root,text=b0,command=push8,width=10,height=5)
B8.grid(row=2,column=2)
B9=Button(root,text='play again',command=reset,width=7,height=2)
B9.grid(row=4,column=1)
root.mainloop()
