import math
import random
import smtplib
import tkinter as tk
from tkinter import messagebox

#function to generate otp
def generate_otp():
    digits = "0123456789"
    otp = ""
    for _ in range(6):
        otp += digits[math.floor(random.random() * 10)]
    return otp

# Function to send OTP via email
def send_otp_email(email, otp):
    msg = otp + " is your OTP"
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("Enter your Email Address", "Enter your Password")
    s.sendmail('Enter your password', email, msg)
    s.quit()

def send_otp():
    email = email_entry.get()
    if email:
        otp = generate_otp()
        send_otp_email(email, otp)
        otp_label.config(text=otp)
    else:
        messagebox.showwarning("Warning", "Please enter your email address.")
   
# Function to verify OTP
def verify_otp(otp, user_input):
    if user_input == otp:
        messagebox.showinfo("Success", "Verification Successful")
    else:
        messagebox.showerror("Error", "Verification Failed. Please check your OTP again.")

my_w = tk.Tk()
my_w.geometry("350x200")
my_w.title("OTP Verification")

my_font=("Helevetica", 15, "bold") # display size and style

email_label=tk.Label(my_w, text= "Enter Email :",font=my_font,padx=10)
email_label.grid(row=1,column=1,pady=10)

otp_entry_label=tk.Label(my_w, text= "Enter OTP :",font=my_font, padx=10)
otp_entry_label.grid(row=2,column=1,pady=10)

otp_label = tk.Label(my_w, text="")

email_entry=tk.Entry(my_w , width = 25 ,  bg = "#FEFBD8")
email_entry.grid(row=1,column=2,pady=10)

otp_entry=tk.Entry(my_w , width = 25 ,  bg = "#FEFBD8")
otp_entry.grid(row=2,column=2,pady=10)

email = email_entry.get()
send_button=tk.Button(my_w, text = "Send OTP" , width= 15,bg='#ffb3fe' ,command=send_otp)
send_button.grid(row=3,column=1,pady=10)

verify_button=tk.Button(my_w, text = "Verify OTP" , width= 15 ,bg='#ffb3fe', command=lambda: verify_otp(otp_label.cget("text"), otp_entry.get()))
verify_button.grid(row=3,column=2,pady=10)

my_w.mainloop()