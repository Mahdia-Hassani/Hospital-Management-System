from tkinter import *
import bcrypt
from PIL import Image,ImageTk
from tkinter import messagebox

from DB.database_connection import get_connection
#__________________
#SQL Function
#__________________
def clear_alldata():
    usernameEnt.delete(0,'end')
    EmailEnt.delete(0,'end')
    passwordEnt.delete(0,'end')
    confirm_password.delete(0,'end')
    phoneEnt.delete(0,'end')

def delete_fullName_email():
    EmailEnt.delete(0,'end')
    usernameEnt.delete(0,'end')


def register_users():
    UserName = usernameEnt.get()
    Email = EmailEnt.get()
    password = passwordEnt.get()
    re_password = confirm_password.get()
    PhoneNumber = phoneEnt.get()

    if not UserName or not Email or not password or not re_password or not PhoneNumber:
        messagebox.showerror("Error","All Fields are required"),
        return

    if len(password)<8:
        messagebox.showerror("Error", "Password must be at least 8 character"),
        return

    if password != re_password:
        messagebox.showerror("Error", "Password Don't match"),
        return

    if len(PhoneNumber)<10:
        messagebox.showwarning("Warning","Phone number must be 10 Character!")
        return
    clear_alldata()

    try:
        con = get_connection()
        cur = con.cursor()

        #check database if email already exists
        check_database="SELECT id from hms_user WHERE email = %s"
        cur.execute(check_database,(Email,))
        exist_Email = cur.fetchone()

        if exist_Email:
                messagebox.showwarning("Warning", "This Email already exists"),
                return

        #check database if fullName already exists
        check_database="SELECT id from hms_user WHERE fullName = %s"
        cur.execute(check_database,(UserName,))
        exist_fullName = cur.fetchone()

        if exist_fullName:
                messagebox.showwarning("Warning", "This Name already exists"),
                return
        delete_fullName_email()

        hashed_password = bcrypt.hashpw(
            password.encode("utf-8"),
            bcrypt.gensalt()
        )

        Add_User = """INSERT INTO hms_user(fullName,email,phone,password)
        VALUES(%s, %s, %s, %s)"""
        values= (UserName,Email,PhoneNumber,hashed_password)
        cur.execute(Add_User,values)
        con.commit()
        messagebox.showinfo("Success","Registration Successful")
        cur.close()
        con.close()
    except Exception as e:
        messagebox.showerror("Database Error", str(e))
#______________________
#If Select "click here"
#______________________
def go_to_login():
    root.destroy()
    import SignIn
#__________________
#root
#__________________
root = Tk()
root.title("Register Login Form")
root.configure(bg="#f2f2f2")
root.resizable(width=False,height=False)
width = 1100
height= 700

s_width = root.winfo_screenwidth()
s_height= root.winfo_screenheight()
center_x= int((s_width- width)/2)
center_y= int((s_height- height)/2)
root.geometry(f"{width}x{height}+{center_x}+{center_y}")
root.state("zoomed")
#__________________
#center frame
#__________________
card = Frame(root,
             bg="#fff",
             width=450,
             height=670
             )
card.place(relx=0.5,rely=0.5,anchor="center")
#_Shadow_
shadow = Frame(root,
               bg="#000000",
               width=453,
               height=673
               )
shadow.place(relx=0.5,rely=0.5,anchor="center")
card.lift()
#image
img= Image.open("icon/logo-dark.png")
img = img.resize((80,80))

logo_img= ImageTk.PhotoImage(img)
logo_label = Label(card,image =logo_img, bg="white", width=95, height=95)
logo_label.image = logo_img
logo_label.place(x=185, y=20)
#______________________
# Entry And Label
#______________________
Label(card,
      text="User Name:",
      bg="#fff",
      fg="#000000",
      font=("Arial",12)
      ).place(x=22,y=120)
usernameEnt = Entry(card,
                    bg="#fff",
                    fg="#000000",
                    font = ("Arial", 12),
                    bd=1,
                    relief="solid"
                    )
usernameEnt.place(x=22, y=146, width=400, height=40)
#Email Address Button
Label(card,
      text="Email Address:",
      bg="#fff",
      fg="#000000",
      font=("Arial",12)
      ).place(x=22,y=210)
EmailEnt=Entry(card,
                    bg="#fff",
                    fg="#000000",
                    font = ("Arial", 12),
                    bd=1,
                    relief="solid"
                    )
EmailEnt.place(x=22,y=236,width=400,height=40)
#Password Button
Label(card,
      text="Password:",
      bg="#fff",
      fg="#000000",
      bd=1,
      font=("Arial",12)
      ).place(x=22,y=296)
passwordEnt = Entry(card,
             bg="#fff",
             fg="#000000",
             font=("Arial",12),
             relief="solid",
             show="*"
            )
passwordEnt.place(x=22,y=320,width=400,height=40)
#Confirm Password Button
Label(card,
      text="Confirm Password:",
      bg="#fff",
      fg="#000000",
      font=("Arial",12),
      ).place(x=22,y=386)
confirm_password=Entry(card,
            bg="#fff",
            fg="#000000",
            font=("Arial",12),
            bd=1,
            relief="solid",
            show="*"
          )
confirm_password.place(x=22,y=410,width=400,height=40)
#Phone number Button
Label(card,
      text="Phone number:",
      bg="#fff",
      fg="#000000",
      font=("Arial",12),
      ).place(x=22,y=473)
phoneEnt = Entry(card,
                 bg="#fff",
                 fg="#000000",
                 font=("Arial",12),
                 relief="solid",
                 bd=1
                 )
phoneEnt.place(x=22,y=500,width=400,height=40)
#_____________________
# Submit Button
#______________________
signIn_Btn = Button(card,
                    text="Sign Up",
                    bg="#1eaffc",
                    fg="#fff",
                    font=("Arial",14,"bold"),
                    bd=0,
                    height=2,
                    command=register_users
                    )
signIn_Btn.place(x=180,y=580,width=80,height=40)
Label(card,
      text="I have Already account! ",
      bg="#fff",
      fg="#000000",
      font=("Arial",12)
).place(x=120,y=630)
back = Button(card,
                    text="click here!",
                    bg="#fff",
                    fg="black",
                    font=("Segeo",9,"bold"),
                    bd=0,
                    cursor="hand2",
                    command=go_to_login
                    )
back.place(x=293,y=630)
root.mainloop()

