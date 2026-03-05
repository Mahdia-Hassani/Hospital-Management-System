from tkinter import *
from tkinter import messagebox,Image
from PIL import Image,ImageTk
import bcrypt
from tkinter import ttk
from mysql.connector import cursor
from DB.database_connection import get_connection

def loginUser():
    username = user_nameEnt.get().strip()
    password = PasswordEnt.get()

    if not username or not password:
        messagebox.showerror("Error","All fields are required")
        return

    try:
        con= get_connection()
        cursor = con.cursor()

        database = """
            SELECT password FROM hms_user
            WHERE email=%s OR fullName=%s """
        cursor.execute(database,(username,username))
        result = cursor.fetchone()

        cursor.close()
        con.close()

        if result:
            stored_hash = result[0]

            if bcrypt.checkpw(password.encode('utf-8'),stored_hash):
                messagebox.showinfo("Success",f"Welcome")
                root.destroy()

            else:
                messagebox.showerror("Error",f"Invalid username or password")
        else:
            messagebox.showerror("Error",f"User not found")
    except Exception as e:
        messagebox.showerror("Error",str(e))

def register_form():
    root.destroy()
    import register_form
#__________________
#Main window
#__________________
root=Tk()
root.title("Sign In")
root.configure(bg="#f2f2f2")
root.resizable(width=False,height=False)
root.state("zoomed")
width=1100
height=700

m_width = root.winfo_screenwidth()
m_height = root.winfo_screenheight()
center_x = int((m_width - width)/2)
center_y = int((m_height - height)/2)
root.geometry(f"{width}x{height}+{center_x}+{center_y}")

#center frame
card = Frame(root,
    bg="#fff",
    width=450,
    height=500
)
card.place(rely=0.5,relx=0.5,anchor="center")
#Shadow frame
shadow = Frame(root,
               bg="#555",
               width=453,
               height=503,
               )
shadow.place(rely=0.5,relx=0.5,anchor="center")
card.lift()

#image
img= Image.open("icon/logo-dark.png")
img = img.resize((80,80))

logo_img= ImageTk.PhotoImage(img)
logo_label = Label(card,image= logo_img, bg="#fff",width=95,height=95 )
logo_label.image = logo_img
logo_label.place(x=185,y=20)

#______________________
# Entry And Label
#______________________

Label(card,
      text="User Name or Email:",
      bg="#fff",
      fg="#000000",
      font=("Arial",12)
      ).place(x=22,y=150)
user_nameEnt = Entry(card,
                     bg="#fff",
                     fg="#000000",
                     font=("Arial",12),
                     relief="solid",
                     bd=1
                     )
user_nameEnt.place(x=22,y=175,width=400,height=40)
#Password Entry

Label(card,
      text="Password:",
      bg="#fff",
      fg="#000000",
      font=("Arial",12)
      ).place(x=22,y=235)

PasswordEnt = Entry(card,
                    bg="#fff",
                    fg="#000000",
                    font=("Arial",12),
                    relief="solid",
                    show="*",
                    bd=1
                    )
PasswordEnt.place(x=22,y=260,width=400,height=40)

#______________________
# Submit Button
#______________________
back = Button(card,
                    text="Forget your password?",
                    bg="#fff",
                    fg="#1eaffc",
                    font=("Arial",9,"bold"),
                    bd=0,
                    cursor="hand2",
                    )
back.place(x=22,y=310)
signin = Button(card,
                text="LOGIN",
                bg="#1eaffc",
                fg="#fff",
                height=2,
                bd=0,
                font=("Se geo UI",14,"bold"),
                command=loginUser,
                )
signin.place(x=180,y=360,width=95,height=45)

Label(card,
      text="Don't have account? ",
      bg="#fff",
      fg="#000000",
      font=("Arial",12)
).place(x=100,y=430)

back = Button(card,
                    text="Sign Up!",
                    bg="#fff",
                    fg="black",
                    font=("Arial",9,"bold"),
                    bd=0,
                    cursor="hand2",
                    command = register_form
                    )
back.place(x=250,y=432)

root.mainloop()
