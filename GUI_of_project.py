###### building the main UI of the system #####
# needed modules
from tkinter import *  # for the ui of system
# for command of each button
# from methods_of_buttons import *
# from contant_GUI import loginy

# intialize ui window
root = Tk()

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the size and position of the window
root.geometry(f"{screen_width}x{screen_height}+0+0")
root.iconbitmap("F:\\course_py\\new_projects\\super_market_system\\img\\logy.ico")

# background color
root.config(bg="gray")

# heading
title = Label(root,text="مرحبا بمكتبة سمير و علي",fg="gold",bg="black",font=("tajawal",32,"bold"))
title.pack(fill=X)

# partition in the right side with background color darkblue 
partition1 = Frame(root,width=400,height=700,bg="darkblue")
partition1.place(x=1000,y=56)

### adding buttons in red partition 
# button 1
button1 = Button(partition1,text="Add New Reader",width=20,fg="white",bg="black",font=("tajawal",18,"bold"))
button1.place(x=25,y=10)
# button 2 
button2 = Button(partition1,text="Add New (Book)",width=20,fg="white",bg="black",font=("tajawal",18,"bold"))
button2.place(x=25,y=70)
# button 3
button3 = Button(partition1,text="Add New (Copies)",width=20,fg="white",bg="black",font=("tajawal",18,"bold"))
button3.place(x=25,y=130)
# button 4
button4 = Button(partition1,text="Add Category",width=20,fg="white",bg="black",font=("tajawal",18,"bold"))
button4.place(x=25,y=190)
# button 5
button5 = Button(partition1,text="Rejoin Reader",width=20,fg="white",bg="black",font=("tajawal",18,"bold"))
button5.place(x=25,y=250)
# button 6
button6 = Button(partition1,text="Borrow Process",width=20,fg="white",bg="black",font=("tajawal",18,"bold"))
button6.place(x=25,y=310)
# button 7
button6 = Button(partition1,text="Buying Process",width=20,fg="white",bg="black",font=("tajawal",18,"bold"))
button6.place(x=25,y=370)


# button quit
button6 = Button(partition1,text="Quit",width=20,fg="black",bg="red",font=("tajawal",18,"bold"),command=quit)
button6.place(x=25,y=580)

## button to login
# button_login = Button(root,text="تسجيل دخول",fg="black",bg="gold",font=("tajawal",16,"bold"),height=3 )
# button_login.place(x=40,y=345)

# keep showing ui 
root.mainloop()