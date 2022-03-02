from tkinter import *
import speedtest

root = Tk()
root.geometry("500x300")
root.config(bg="lavender")
root.title=("Home made speed test app")

title = Label(root, text="Internet Speed Test", font = ("Lucida Sans Unicode", 20, "bold", "italic"), bg="lavender", fg="lightsteelblue4")
title.place(relx=0.5,rely=0.1,anchor=CENTER)

dt = Label(root, text="Download Speed ↓", font=("Segoe Print", 18, "bold"),bg="lavender",fg="forestgreen")
dt.place(relx=0.25,rely=0.5,anchor=CENTER)

ut = Label(root, text="Upload Speed ↑", font=("Segoe Print", 18, "bold"),bg="lavender",fg="steelblue3")
ut.place(relx=0.75,rely=0.5,anchor=CENTER)

dts = Label(root, font=("Yu Gothic Light", 14, "bold"),bg="lavender")
dts.place(relx=0.25,rely=0.6,anchor=CENTER)

uts = Label(root, font=("Yu Gothic Light", 14, "bold"),bg="lavender")
uts.place(relx=0.75,rely=0.6,anchor=CENTER)

def speedCheck():
    st=speedtest.Speedtest()
    ds = round(st.download()/1000000,2)
    dts["text"]=str(ds) + "mbps"
    us = round(st.upload()/1000000,2)
    uts["text"]=str(us) + "mbps"

btn_doctor = Button(root, bg="lightseagreen", text="Check Speed", command=speedCheck, fg="white",relief=FLAT)
btn_doctor.place(relx=0.5,rely=0.3,anchor=CENTER)

root.mainloop()