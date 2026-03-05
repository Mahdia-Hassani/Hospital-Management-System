from tkinter import *
from PIL import Image,ImageTk
from HMS.Doctor.DoctorDetail import doctor_items
from HMS.Doctor.add_doctor import add_doctor_frame
from HMS.Patients.patient_list import patient_list
from Patients.add_patients import add_patient_form

#____ _______________________
# function
#___________________________

root =Tk()
root.title("Hospital Management Dashboard")
root.configure(bg="#f5f7ff")
root.resizable(width=False,height=False)
width=1300
height=780
s_width = root.winfo_screenwidth()
s_height = root.winfo_screenheight()
center_x = int((s_width -width)/2)
center_y = int((s_height -height)/2)
root.geometry(f"{width}x{height}+{center_x}+{center_y}")
root.state("zoomed")
#___________________________
# Header
#___________________________

header = Frame(root,
               bg="#0d6efd",
               height=60,
               )
header.pack(fill=X)

img= Image.open("icon/logo.png")
img = img.resize((32,32))

logo_img= ImageTk.PhotoImage(img)
logo_label = Label(header,
                   image =logo_img,
                   text="Hospital",
                   compound="left",
                   bg="#0d6efd",
                   fg="#fff",
                   font=("Segoe UI",16,"bold"),
                   padx=10,
                   pady=5
                   )
logo_label.image = logo_img
logo_label.pack(side="left",pady=20,padx=15)
#___________________________
# Admin Icon
#___________________________
admin_btn = Menubutton(header,
                       text="Admin",
                       fg="#fff",
                       bg="#0a71ae",
                       cursor="hand2",
                       font=("Segeo UI",10,"bold"),
                       activebackground="#0a71ae",
                       relief="flat"
)
admin_menu = Menu(admin_btn,tearoff=0,)
admin_menu.add_command(label="Profile")
admin_menu.add_command(label="Edit Profile")
admin_menu.add_separator()
admin_menu.add_command(label="LagOut")

admin_btn.configure(menu=admin_menu)
admin_btn.pack(side="right",padx=20)

#___________________________
# Main body
#___________________________

main = Frame(root,bg="#fff")
main.pack(fill="both",expand=True)

#___________________________
# side bar
#___________________________
sidebar_width = 200
sidebar = Frame(main,bg="#fff",width=sidebar_width)
sidebar.pack(side="left",fill="y")
sidebar.pack_propagate(False)
Shadow = Frame(main,bg="#d9d9d9",width=3)
Shadow.pack(side="left",fill="y")
Shadow.pack_propagate(False)

Label(sidebar,
      text="Welcome ",
      bg="#fff",
      font=("Segeo UI",11,"bold")
      ).pack(anchor="w",pady=10,padx=10)
#___________________________
# content area
#___________________________
content_frame = Frame(main,bg="#f5f7ff")
content_frame.pack(side="right",fill="both",expand=True)

account_open = False

def toggle_account():
    global account_open
    if account_open:
        account_submenuBtn.pack_forget()
        account_btn.config(text="Account ⌄")
    else:
        account_submenuBtn.pack(fill=X)
        account_btn.config(text="Account ⌃")

        account_open= not account_open
#___________________________
# helper function
#___________________________
def clear_content():
    for widget in content_frame.winfo_children():
        widget.destroy()

#___________________________
# pages function
#___________________________
def show_dashboard():
    clear_content()
    Label(
          content_frame,
          text="Dashboard",
          bg="#f5f7fa",
          font=("Segeo UI",20,"bold")
          ).pack(pady=40)

def add_doctor():
    clear_content()
    add_doctor_frame(content_frame)

def show_doctor():
    clear_content()
    # ___________________________
    # content Doctor
    # ___________________________
    top_bar = Frame(
        content_frame,
        bg="#f5f7fa",
        height=60
    )
    top_bar.pack(fill=X,padx=20,pady=(10,0))
    title_lbl = Label(
        top_bar,
        text="Doctors",
        bg="#f5f7fa",
        fg="#000",
        font=("Segeo UI",18,"bold")
    )
    title_lbl.pack(side="left")
    add_button = Button(top_bar,
                        text=" + Create Account ",
                        font=("Segeo UI",10,"bold"),
                        bg="#0d6efd",
                        fg="#fff",
                        relief="flat",
                        cursor="hand2",
                        command=add_doctor
                        )
    add_button.pack(side="right")
    doctor_items(content_frame)

def add_patients():
    clear_content()
    add_patient_form(content_frame)

def show_patient():
    clear_content()
    # ___________________________
    # content Doctor
    # ___________________________
    top_bar = Frame(
        content_frame,
        bg="#f5f7fa",
        height=60
    )
    top_bar.pack(fill=X, padx=20, pady=(10, 0))
    title_lbl = Label(
        top_bar,
        text="Patients",
        bg="#f5f7fa",
        fg="#000",
        font=("Segeo UI", 18, "bold")
    )
    title_lbl.pack(side="left")
    add_button = Button(top_bar,
                        text=" + Add Patients",
                        font=("Segeo UI", 10, "bold"),
                        bg="#0d6efd",
                        fg="#fff",
                        relief="flat",
                        cursor="hand2",
                        command=add_patients
                        )
    add_button.pack(side="right")
    patient_list(content_frame)
def show_appointment():
    clear_content()
    Label(content_frame,
          text="Appointment",
          bg="#f5f7fa",
          font=("Segeo UI",20,"bold")
          ).pack(pady=40)

def show_Invoice():
    clear_content()
    Label(content_frame,
          text="Invoice",
          bg="#f5f7fa",
          font=("Segeo UI",20,"bold")
          ).pack(pady=40)

def show_payment():
    clear_content()
    Label(content_frame,
          text="Payment",
          bg="#f5f7fa",
          font=("Segeo UI",20,"bold")
          ).pack(pady=40)
#___________________________
# sidebar button
#___________________________

#log_image
dashboard_logo = ImageTk.PhotoImage(file="icon/dashboardColor.png")
doctor = ImageTk.PhotoImage(file="icon/doctor.png")
patient = ImageTk.PhotoImage(file="icon/patients.png")
appointment = ImageTk.PhotoImage(file="icon/appointment.png")
account = ImageTk.PhotoImage(file="icon/accounts.png")

dashboard_btn=Button(sidebar,
                     image=dashboard_logo,
                     compound="left",
                     text="Dashboard",
                     bg="#fff",
                     fg="#999",
                     font=("Segoe UI",11,"bold"),
                     padx=8,
                     relief="flat",
                     anchor="w",
                     command=show_dashboard,
                     )
dashboard_btn.pack(fill="x", pady=4)

doctor_btn=Button(sidebar,
       image=doctor,
       compound="left",
       text="Doctor",
       bg="#fff",
       fg="#999",
       font=("Segoe UI",11,"bold"),
       padx=8,
       relief="flat",
       anchor="w",
       command=show_doctor,

       )
doctor_btn.pack(fill="x",pady=4)

patient_btn=Button(sidebar,
       image=patient,
       compound="left",
       text="Patient",
       bg="#fff",
       fg="#999",
       font=("Segoe UI",11,"bold"),
       padx=8,
       relief="flat",
       anchor="w",
       command=show_patient,
       )
patient_btn.pack(fill="x",pady=4)
#appointment
appointment_btn=Button(sidebar,
       image = appointment,
       compound="left",
       text="appointment",
       bg="#fff",
       fg="#999",
       font=("Segoe UI",11,"bold"),
       padx=8,
       relief="flat",
       anchor="w",
       command=show_appointment,
)
appointment_btn.pack(fill="x",pady=4)

account_btn=Button(sidebar,
       image=account,
       compound="left",
       text="Account",
       bg="#fff",
       fg="#999",
       font=("Segoe UI",11,"bold"),
       padx=8,
       relief="flat",
       anchor="w",
       command=toggle_account
       )
account_btn.pack(fill="x",pady=4)
account_submenuBtn=Frame(sidebar,bg="#f2f2f2")

submenu=Button(account_submenuBtn,
       text="Invoice",
       compound="left",
       bg="#fff",
       fg="#999",
       font=("Segoe UI",11,"bold"),
       padx=30,
       relief="flat",
       anchor="w",
       command=show_Invoice,
 )
submenu.pack(fill="x",pady=2)
submenu=Button(account_submenuBtn,
       text="payment",
       compound="left",
       bg="#fff",
       fg="#999",
       font=("Segoe UI",11,"bold"),
       padx=30,
       relief="flat",
       anchor="w",
       command=show_payment,
 )
submenu.pack(fill="x",pady=4)
show_doctor()
root.mainloop()