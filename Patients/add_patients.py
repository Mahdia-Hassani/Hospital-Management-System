import os
import shutil
from tkinter import *
from tkinter import ttk, filedialog, messagebox
import bcrypt
from HMS.DB.database_connection import get_connection


def add_patient(
        first_name_ent,
        last_name_ent,
        user_name_ent,
        email_ent,
        password_ent,
        confirm_password_ent,
        dob_ent,
        gender_var,
        address_ent,
        country_var,
        city_ent,
        state_var,
        postal_ent,
        phone_ent,
        avatar_path_var,
        status_var,
):
    fist_name = first_name_ent.get()
    last_name = last_name_ent.get()
    user_name = user_name_ent.get()
    email = email_ent.get()
    password = password_ent.get()
    confirm_password = confirm_password_ent.get()
    date_of_birth = dob_ent.get()
    gender = gender_var.get()
    address = address_ent.get()
    country = country_var.get()
    city =city_ent.get()
    state = state_var.get()
    postal = postal_ent.get()
    phone = phone_ent.get()
    status = status_var.get()
    avatar_path = avatar_path_var.get()

    if password != confirm_password:
        messagebox.showerror("Error","Password do not match")
        return

    try:
        con = get_connection()
        cur = con.cursor()

        hashed_password = bcrypt.hashpw(
            password.encode("utf-8"),
            bcrypt.gensalt()
        )
        query = """
        INSERT INTO hms_add_patient(
        first_name, last_name, user_name,email, password, dob, gender, address, country, city, state, postal, phone, image, status
       
        )
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """

        data= (
            fist_name,last_name,user_name,email,
            date_of_birth,gender,address,country,city,state,
            postal,phone,avatar_path,status
        )
        cur.execute(query,data)
        con.commit()

        messagebox.showinfo("Success","Patient register successfully")
        cur.close()
        con.close()
    except Exception as e:
        messagebox.showerror("Database Error",str(e))

 #============Scroll bar====================

def scrollbar_frame(parent):
    canvas = Canvas(
        parent,
        bg="#fff",
        highlightthickness=0
    )

    scrollbar = Scrollbar(
        parent,
        orient="vertical",
        command=canvas.yview
    )

    scroll_frame = Frame(canvas,bg="#fff")
    scroll_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    canvas.create_window(
        (0,0),
        window=scroll_frame,
        anchor="nw"
    )
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.pack(side="left",fill="both",expand=True)
    scrollbar.pack(side="right",fill="y")

    return scroll_frame

def add_patient_form(content_frame):
    form_area = scrollbar_frame(content_frame)
    container = Frame(form_area,bg="#fff")
    container.pack(fill="both",expand=True,padx=20)

    container.grid_columnconfigure(0,weight=1,uniform="x")
    container.grid_columnconfigure(1,weight=1,uniform="x")
    container.grid_columnconfigure(2,weight=1,uniform="x")
    container.grid_columnconfigure(3,weight=1,uniform="x")

    #====================title===========================
    Label(
        container,
        text="Add Patient",
        bg="#fff",
        fg="#333",
        font=("Segeo UI",18,"bold")
    ).grid(row=0,column=0,columnspan=4,sticky="w",pady=(0,20))

    # ====================Variable===========================

    gender_var = StringVar(value="Male")
    status_var = StringVar(value="Active")
    country_var = StringVar()
    state_var = StringVar()
    avatar_path_var = StringVar(value="No File Selected")
    selected_avatar_path =None
    for i in range(4):
        container.columnconfigure(i,weight=1,uniform="x")

    # ====================Helper=============================

    def create_Label(text,row,col,required=False):
        Label(container,
              text=text +("*" if required else ""),
              bg="#fff",
              fg="#444",
              font=("Segeo UI",10)
        ).grid(row=row,column=col,pady=(8,4),padx=10,sticky="w",)

    def create_Entry(row,col,colspan=1,show=None):
            ent= Entry(
                container,
                font=("Segeo UI",10),
                relief="solid",
                bd=1,
            )
            if show:
                ent.config(show = show)
            ent.grid(
                row = row,
                column=col,
                columnspan= colspan,
                sticky="we",
                padx=10,
                pady= 6
            )
            return ent
    def file_name(name,max_len=30):
            return name if len(name)<= max_len else name[:max_len -3]+"..."

        # ====================Basic info=============================

    create_Label('First Name',row=1,col=0,required=True)
    create_Label('Last Name', row=1, col=2, required=True)

    first_name_ent = create_Entry(2,0,2)
    last_name_ent = create_Entry(2,2,2)

    create_Label('User Name', row=3, col=0, required=True)
    create_Label('Email', row=3, col=2, required=True)

    user_name_ent = create_Entry(4, 0, 2)
    email_ent = create_Entry(4, 2, 2)

    create_Label('Password', row=5, col=0)
    create_Label('Confirm Password', row=5, col=2)

    password_ent = create_Entry(6, 0, 2,show="*")
    confirm_password_ent= create_Entry(6, 2, 2,show="*")

 # ====================Date Calender=============================

    create_Label('Date of Birth', row=7, col=0)
    create_Label('Gender', row=7, col=2)

    dob_ent = create_Entry(8,0,2)

    Radiobutton(
            container,
            text="Male",
            variable= gender_var,value="Male",
            bg="#fff",
        ).grid(row = 8,column=2,sticky="w",padx=10)

    Radiobutton(
            container,
            text="Female",
            variable= gender_var,value="Female",
            bg="#fff",
        ).grid(row = 8,column=3,sticky="w",padx=10)

    # ====================Address=============================

    create_Label("Address",9,0)
    address_ent = create_Entry(10,0,4)

# ===================Location=============================

    create_Label("Country", 11, 0)
    create_Label("City", 11, 1)
    create_Label("State /Province", 11, 2)
    create_Label("Postal Code", 11, 3)

    style =ttk.Style()
    style.configure("Custom.TCombobox",padding= 6)
    country_combobox = ttk.Combobox(
            container,
            textvariable=country_var,
            values=["Afghanistan","Iran","USA","Canada"],
            style= "Custom.TCombobox"
        )
    country_combobox.grid(row=12,column=0,sticky="we",padx=10,pady=4)
    city_ent = create_Entry(12,1)

    state_combobox = ttk.Combobox(
            container,
            textvariable=state_var,
            values=["California", "Tehran", "USA", "Kabul"],
            style="Custom.TCombobox"
        )
    state_combobox.grid(row=12,column=2,sticky="we",padx=10,pady=4)
    postal_ent = create_Entry(12,3)

    create_Label("Phone",13,0)
    phone_ent= create_Entry(14,0,2,)

    create_Label("Image",13,2)
    avatar_label = Label(
            container,
            textvariable=avatar_path_var,
            bg="#f0f0f0",
            anchor="w",
            padx=10,
            font=("Segeo UI",9),
            width=30,
            relief="solid",
            bd=1
        )
    avatar_label.grid(row=14,column=2,sticky="we",padx=10)

#==================Choose file Button====================================
    saved_avatar_path = None
    def choose_image():
        global saved_avatar_path

        select_avatar_path = filedialog.askopenfilename(
            title="Select Image",
            filetypes=[("Image Files","*.png *.jpg *.jpeg *.TIF")]
        )
        if not select_avatar_path:
            return

        images_dir= "DoctorsImage"
        os.makedirs(images_dir,exist_ok=True)

        image_name = os.path.basename(select_avatar_path)
        saved_avatar_path = os.path.join(images_dir,image_name)

        if os.path.exists(saved_avatar_path):
            messagebox.showerror(
                "Duplicate","This image already exists"
            )
            return
        try:
            shutil.copy(select_avatar_path, saved_avatar_path)

        except Exception as e:
            messagebox.showerror("Image Error",str(e))

        avatar_path_var.set(file_name(image_name))


    Button(
            container,
            text="Choose File",
            font=("Segeo UI",10),
            relief="solid",
            bd=1,
            command=choose_image
        ).grid(row=14,column=3,sticky="w",padx=10)

    # ====================Status==============================
    create_Label("Status",15,0)

    Radiobutton(
            container,
            text="Active",
            variable=status_var,value="Active",
            bg="#fff",
        ).grid(row=18,column=0,sticky="w",padx=10)

    Radiobutton(
            container,
            text="Deactivate",
            variable=status_var,value="Deactivate",
            bg="#fff",
        ).grid(row=18,column=1,sticky="w",padx=10)

    Button(
            container,
            text="Create Account",
            bg="#0d6efd",
            font=("Segeo UI",10),
            relief="flat",
            fg="#fff",
            padx=30,
            pady=10,
            cursor="hand2",
            command= lambda: add_patient(
        first_name_ent,
        last_name_ent,
        user_name_ent,
        email_ent,
        password_ent,
        confirm_password_ent,
        dob_ent,
        gender_var,
        address_ent,
        country_var,
        city_ent,
        state_var,
        postal_ent,
        phone_ent,
        avatar_path_var,
        status_var,
)
        ).grid(row=19,column=0,columnspan=4,pady=30)
















