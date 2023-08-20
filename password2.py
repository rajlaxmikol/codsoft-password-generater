from tkinter import *
from tkinter import messagebox
import ast

window=Tk()
window.title('Sign Up')
window.geometry('900x500+300+200')
window.configure(bg="grey")
window.resizable(False,False)

def Login():
    username=user.get()
    password=code.get()
    conform_password=code.get()

    if username=='rajlaxmikol' and  password=='Rajlaxmi@123' and conform_password=='Rajlaxmi@123':
        screen=Toplevel(window)
        screen.title("App")
        screen.geometry('925x500+300+200')
        screen.config(bg="lightgreen")

        Label(screen,text="You are Welcome!",bg='grey',font=('arial(Body)',50,'bold')).pack(expand=True)

        screen.mainloop()

    elif username!='rajlaxmikol' and  password!='Rajlaxmi@123':
         messagebox.showerror("Invalid","invalid username and password")
         
    elif password!='Rajlaxmi@123':
        messagebox.showerror("Invalid",'invalid password')
        
    elif username!='rajlaxmikol':
        messagebox.showerror("Invalid",'invalid username')
        
    elif conform_password!='Rajlaxmi@123':
         messagebox.showerror("Invalid",'Not match password')
         

#img = PhotoImage(file="login.jpg")
#label(window,image=img,bg='white').place(x=20,y=50)

frame=Frame(window,width=340,height=380,bg="lightgreen")
frame.place(x=480,y=50)

heading=Label(frame,text='SIGN UP',fg='#57a1f8',bg='white',font=('microsoft YaHei UI Light',23,'bold'))
heading.place(x=90,y=5)
#################----------------
def on_enter(e):
    user.delete(0,'end')
def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')
        
user = Entry(frame,width=25,fg='black',border=1,bg="pink",font=('microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=1,bg='black').place(x=25,y=107)

################---------------
def on_enter(e):
    code.delete(0,'end')
def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0,'Password')
        
code = Entry(frame,width=25,fg='black',border=1,bg="pink",font=('microsoft YaHei UI Light',11))
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)


Frame(frame,width=295,height=1,bg='black').place(x=25,y=177)
###############--------------
def on_enter(e):
    conform_code.delete(0,'end')
def on_leave(e):
    if conform_code.get()=='':
        conform_code.insert(0,'conform Password')
        
conform_code = Entry(frame,width=25,fg='black',border=1,bg="pink",font=('microsoft YaHei UI Light',13))
conform_code.place(x=30,y=220)
conform_code.insert(0,'conform Password')
conform_code.bind('<FocusIn>',on_enter)
conform_code.bind('<FocusOut>',on_leave)
Frame(frame,width=295,height=1,bg='black').place(x=25,y=247)


#################-------------

Button(frame,width=39,pady=7,text='Login',bg='#57a1f8',fg='white',border=0,command=Login).place(x=35,y=280)
label=Label(frame,text="Don't have an account?",fg='black',bg='white',font=('microsoft YaHei UI Light',10))
label.place(x=70,y=340)

sign_Up= Button(frame,width=7,text='Sign Up',border=1,bg='pink',cursor="hand2",fg='blue')
sign_Up.place(x=220,y=340)

#reset= Button(frame,width=2,text='reset',border=1,bg='pink',cursor="hand2",fg='blue')
#reset.place(x=150,y=430)

window.mainloop()

