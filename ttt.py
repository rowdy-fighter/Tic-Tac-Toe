# Tic Tac Toe
Height=700
width=900
import tkinter.messagebox
import tkinter as tk
click=True
def checkers(buttons):
    global click
    if (buttons['text']=='' and click==True):
        buttons['text']="X"
        click=False
        scorekeeper()
    elif(buttons['text']=="" and click==False):
        buttons['text']="0"
        click=True 
        scorekeeper()
i=1
def scorekeeper():
    if(bt1['text']=="X" and bt5['text']=="X" and bt9['text']=="X"):
        bt1.configure(background="red")
        bt5.configure(background="red")
        bt9.configure(background="red")
        n=float(p2e.get())
        score=n+1
        p2e.set(score)
        tk.messagebox.showinfo("0","You win a game ")
        reset()
    elif(bt1['text']=="X" and bt2['text']=="X" and bt3['text']=='X'):
       bt1.configure(background="red")
       bt2.configure(background="red")
       bt3.configure(background="red")
       n=float(p1e.get())
       score=n+1
       p1e.set(score)
       tk.messagebox.showinfo("X","You win a game baby")
       reset()
    elif(bt4['text']=="X" and bt5['text']=="X" and bt6['text']=='X'):
        bt4.configure(background="red")
        bt5.configure(background="red")
        bt6.configure(background="red")
        n=float(p1e.get())
        score=n+1
        p1e.set(score)
        tk.messagebox.showinfo("X","You win a game baby")
        reset()
    elif(bt7['text']=="X" and bt8['text']=="X" and bt9['text']=='X'):
        bt7.configure(background="red")
        bt8.configure(background="red")
        bt9.configure(background="red")
        n=float(p1e.get())
        score=n+1
        p1e.set(score)
        tk.messagebox.showinfo("X","You win a game baby")
    elif(bt3['text']=="X" and bt5['text']=="X" and bt7['text']=='X'):
        bt7.configure(background="red")
        bt5.configure(background="red")
        bt3.configure(background="red")
        n=float(p1e.get())
        score=n+1
        p1e.set(score)
        tk.messagebox.showinfo("X","You win a game baby")
        reset()
    elif(bt1['text']=="X" and bt5['text']=="X" and bt9['text']=='X'):
        bt1.configure(background="red")
        bt5.configure(background="red")
        bt9.configure(background="red")
        n=float(p1e.get())
        score=n+1
        p1e.set(score)
        tk.messagebox.showinfo("X","You win a game baby")
        reset()
    elif(bt1['text']=="0" and bt2['text']=="0" and bt3['text']=='0'):
        bt1.configure(background="red")
        bt2.configure(background="red")
        bt3.configure(background="red")
        n=float(p2e.get())
        score=n+1
        p2e.set(score)
        tk.messagebox.showinfo("0","You win a game baby")
        reset()
    elif(bt4['text']=="0" and bt5['text']=="0" and bt6['text']=='0'):
        bt4.configure(background="red")
        bt5.configure(background="red")
        bt6.configure(background="red")
        n=float(p2e.get())
        score=n+1
        p2e.set(score)
        tk.messagebox.showinfo("0","You win a game baby")
        reset()
    elif(bt7['text']=="0" and bt8['text']=="0" and bt9['text']=='0'):
        bt7.configure(background="red")
        bt8.configure(background="red")
        bt9.configure(background="red")
        n=float(p2e.get())
        score=n+1
        p2e.set(score)
        tk.messagebox.showinfo("0","You win a game baby")
        reset()
    elif(bt3['text']=="0" and bt5['text']=="0" and bt7['text']=='0'):
        bt7.configure(background="red")
        bt5.configure(background="red")
        bt3.configure(background="red")
        n=float(p2e.get())
        score=n+1
        p2e.set(score)
        tk.messagebox.showinfo("0","You win a game baby")
        reset()
    elif(bt1['text']=="0" and bt5['text']=="0" and bt9['text']=='0'):
        bt1.configure(background="red")
        bt5.configure(background="red")
        bt9.configure(background="red")
        n=float(p2e.get())
        score=n+1
        p2e.set(score)
        tk.messagebox.showinfo("0","You win a game baby")
        reset()
     




def reset():
    bt1['text']=''
    bt2['text']=''
    bt3['text']=''
    bt4['text']=''
    bt5['text']=''
    bt6['text']=''
    bt7['text']=''
    bt8['text']=''
    bt9['text']=''
    
    bt1.configure(background="white")
    bt2.configure(background="white")
    bt3.configure(background="white")
    bt4.configure(background="white")
    bt6.configure(background="white")
    bt5.configure(background="white")
    bt7.configure(background="white")
    bt9.configure(background="white")
    bt8.configure(background="white")


def new():
    reset()
    p1e.set(0)
    p2e.set(0)



root = tk.Tk()
root.title("Tic Tac Toe")
root.configure(background="#80ff80")

p1e=tk.IntVar()
p1e.set(0)
p2e=tk.IntVar()
p2e.set(0)


canvas=tk.Canvas(root, width=width,height=Height)
canvas.pack()

background= tk.PhotoImage(file="Images/wall.png")
background_label=tk.Label(root,image=background)
background_label.place(relwidth=1,relheight=1)

Frame1=tk.Frame(root,bd=20,background="#33ccff",bg="#000000")
Frame1.place(relx=0.3,rely=0.1,relwidth=0.5,relheight=0.6,anchor="n")

bt1=tk.Button(Frame1,fg="#000000",font=50,bg="white",command=lambda: checkers(bt1))
bt1.place(relx=0,rely=0,relwidth=0.3,relheight=0.33)

bt2=tk.Button(Frame1,fg="#000000",font=50,bg="white",command=lambda: checkers(bt2))
bt2.place(relx=0.3,rely=0,relwidth=0.3,relheight=0.33)

bt3=tk.Button(Frame1,fg="#000000",font=50,bg="white",command=lambda: checkers(bt3))
bt3.place(relx=0.6,rely=0,relwidth=0.3,relheight=0.33)

bt4=tk.Button(Frame1,fg="#000000",font=50,bg="white",command=lambda: checkers(bt4))
bt4.place(relx=0,rely=0.33,relwidth=0.3,relheight=0.33)

bt5=tk.Button(Frame1,fg="#000000",font=50,bg="white",command= lambda: checkers(bt5))
bt5.place(relx=0.3,rely=0.33,relwidth=0.3,relheight=0.33)

bt6=tk.Button(Frame1,fg="#000000",font=50,bg="white",command=lambda: checkers(bt6))
bt6.place(relx=0.6,rely=0.33,relwidth=0.3,relheight=0.33)

bt7=tk.Button(Frame1,fg="#000000",font=50,bg="white",command=lambda: checkers(bt7))
bt7.place(relx=0,rely=0.66,relwidth=0.3,relheight=0.33)
    
bt8=tk.Button(Frame1,fg="#000000",font=50,bg="white",command=lambda: checkers(bt8))
bt8.place(relx=0.3,rely=0.66,relwidth=0.3,relheight=0.33)

bt9=tk.Button(Frame1,fg="#000000",font=50,bg="white",command=lambda: checkers(bt9))
bt9.place(relx=0.6,rely=0.66,relwidth=0.3,relheight=0.33)



Frame2=tk.Frame(root,bd=20,bg="red")
Frame2.place(relx=0.5,rely=0.1,relwidth=0.4,relheight=0.6)

framea=tk.Frame(Frame2,bd=20,bg="#33ccff")
framea.place(relx=0,rely=0,relwidth=1,relheight=0.45)

player1=tk.Label(framea,text="Player 1:",bd=20,font=50,fg='white',background="#000000")
player1.place(relx=0,rely=0,relwidth=0.3,relheight=0.2)
p1entry=tk.Entry(framea,fg='black',textvariable=p1e,font=60,background='white')
p1entry.place(relx=0.4,rely=0,relwidth=0.5,relheight=0.2)
player2=tk.Label(framea,text="Player 2:",font=50,fg='white',background="black")
player2.place(relx=0,rely=0.25,relwidth=0.3,relheight=0.2)
p2entry=tk.Entry(framea,textvariable=p2e,bg="black",fg='black',font=60,background='white')
p2entry.place(relx=0.4,rely=0.25,relwidth=0.5,relheight=0.2)    


frameb=tk.Frame(Frame2,bd=50,bg="#33ccff")
frameb.place(relx=0,rely=0.5,relwidth=1,relheight=0.45)

reset_bt=tk.Button(frameb,text="Reset",font=50,fg="white",background="black",command=lambda: reset())
reset_bt.place(relx=0,rely=0,relwidth=1,relheight=0.7)
new_bt=tk.Button(frameb,text="New Game",font=50,fg="white",background="black",command=lambda: new())
new_bt.place(relx=0,rely=0.8,relwidth=1,relheight=0.7)



root.mainloop()