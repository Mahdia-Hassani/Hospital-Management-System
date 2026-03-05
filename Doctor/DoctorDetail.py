from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import bcrypt

from HMS.DB.database_connection import get_connection


def select_doctor():
    try:
        con = get_connection()
        cur = con.cursor()

        sql = """
        SElECT full_name,roles,address,image
        FROM hms_add_doctor ORDER BY id DESC
        """

        cur.execute(sql)
        doctor = cur.fetchall()
        cur.close()
        con.close()

        return doctor
    except Exception as x:
        messagebox.showerror("Database Error",str(x))
        return []



def doctor_items(content_frame):
#+++++++++++++++++++++
# Box for all cards
#+++++++++++++++++++++

    card_frame = Frame(content_frame,bg="#f5f7fa")
    card_frame.pack(fill="both",expand=True,padx=20,pady=20)

    doctors = select_doctor()

    card_width = 230
    card_height = 170
    gap_x = 40
    gap_y = 20
    cols = 4

    base_directory = os.path.dirname(os.path.abspath(__file__))

    #create card
    for index, (name,role,location,img_name) in enumerate(doctors):
        row = index // cols
        col = index % cols

        x = col *(card_width + gap_x)
        y = row * (card_height + gap_y)
        card = Frame(
        card_frame,
        bg="#fff",
        width=card_width,
        height=card_height,
        highlightthickness=1,
        highlightbackground="#e0e0e0"

        )
        card.place(x=x,y=y)
        card.pack_propagate(False)
        #Items

        Button(
            card,
            text="⋮",
            bg="#fff",
            fg="#999",
            bd=0,
            font=("Se geo UI",14 ,"bold")
        ).place(x=190,y=8)

        img_path = os.path.join(base_directory,"..","DoctorsImage",img_name)

        if not os.path.exists(img_path):
            img_path = os.path.join(base_directory, "..", "DoctorsImage", "user.jpg")


        img = Image.open(img_path).resize((60,60))
        photo = ImageTk.PhotoImage(img)

        avatar = Label(card, image=photo,bg="#fff")
        avatar.image = photo
        avatar.pack(pady=(18,6))
        #===============Name==============
        Label(
            card,
            text=name,
            bg="White",
            fg="#000",
            font=("Segeo UI",11,"bold")
        ).pack()
        #==============Role==============
        Label(
            card,
            text=role,
            bg="white",
            fg="#000",
            font=("Se geo UI",9)
        ).pack()
        #===========Location=================
        Label(
            card,
            text=f"{location}",
            bg="white",
            fg="#000",
            font=("Se geo UI",9)
        ).pack(pady=(4,0))







