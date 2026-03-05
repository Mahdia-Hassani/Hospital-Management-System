import os
from tkinter import *
from tkinter import messagebox, ttk
from PIL import ImageTk
from HMS.DB.database_connection import get_connection


#dataBase
def select_patient():
    try:
        con = get_connection()
        cursor = con.cursor()

        sql = """ 
        SELECT first_name, dob,address,phone,email
        FROM hms_add_patient
        ORDER BY id DESC
        """
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        con.close()
        return data
    except Exception as e:
        messagebox.showerror("DataBase Error",str(e))
        return []

def patient_list(content_frame):
    data = select_patient()

    entry_var= IntVar(value=10)
    current_page = IntVar(value=1)

    style = ttk.Style()
    style.theme_use("default")

    style.configure(
        "Treeview",
        background = "#fff",
        foreground="#333",
        rowheight = 46,
        fieldbackground = "#fff",
        font=("Segeo UI",10),
    )
    style.configure(
        "Treeview.Heading",
        background = "#f1f1f3f6",
        foreground="#000",
        font=("Segeo UI",11,"bold"),
    )
    style.map(
        "Treeview",
        background=[(
            "selected","#fef3f2fd"
        )]
    )
    top_frame = Frame(content_frame,bg="#fff")
    top_frame.pack(fill="x",padx=20,pady=12)

    Label(
        top_frame,
        text="Show",
        bg="#fff",
        font=("Segeo UI",11)
    ).pack(side="left")
    entries_box = ttk.Combobox(
        top_frame,
        textvariable=entry_var,
        width=7,
        font=("Segeo UI",11),
        values =[10,20,30,40,50],
        state="readonly"
    )
    entries_box.pack(side="left",padx=8)

    Label(
        top_frame,
        text="Entry",
        bg="#fff",
        font=("Segeo UI", 11)
    ).pack(side="left")

    table_frame = Frame(content_frame,bg="#fff")
    table_frame.pack(fill="both",padx=20,expand=True)

    columns = ("Name","Age","Address","Phone","Email","Action")

    tree = ttk.Treeview(
        table_frame,
        columns=columns,
        show="tree headings",
        height=10

    )
    tree.column("#0",width=60,anchor="center")
    tree.heading("#0")

    tree.column("Name",width=160)
    tree.column("Age", width=70,anchor="center")
    tree.column("Address", width=240,anchor="center")
    tree.column("Phone", width=140,anchor="center")
    tree.column("Email", width=220,anchor="center")
    tree.column("Action", width=200, anchor="center")

    for col in columns:
        tree.heading(col,text=col)

    tree.pack(side="left",fill="both",expand=True)

    scrollbar = ttk.Scrollbar(
        table_frame,
        orient="vertical",
        command=tree.yview
    )
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right",fill="y")

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    img_path = os.path.join(BASE_DIR,"..","image","user.jpg")
    img = Image.open(img_path).resize((32,32))

    photo = ImageTk.PhotoImage(img)
    photos = []

    def load_data():
        tree.delete(*tree.get_children())
        per_page = entry_var.get()
        page = current_page.get()

        strat = (page-1) * per_page

        end = strat+ per_page

        for row in data[strat:end]:
            tree.insert(
                "",
                "end",
                image = photo,
                values=(row[0],row[1],row[2],row[3],row[4],"delete")
            )
            photos.append(photo)

        #page_label


    pagination_frame = Frame(content_frame,bg="#fff")
    pagination_frame.pack(fill="x",padx=20,pady=12)

    page_label = Label(
        pagination_frame,
        text= "",
        bg = "#fff",
        font = ("Segoe UI",10)
    )
    page_label.pack(side="left")

    def prev_page():
        if current_page.get()>1:
            current_page.set(current_page.get()-1)
            load_data()

    def next_page():
        per_page = entry_var.get()
        max_page = (len(data)+per_page-1) //per_page
        if current_page.get() < max_page:
            current_page.set(current_page.get()+1)
            load_data()














