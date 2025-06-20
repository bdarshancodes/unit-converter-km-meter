import tkinter as tk
from tkinter import messagebox

def calculate_km():
    try:
        km=float(entry.get())
        meter=km*1000
        messagebox.showinfo("result",f"{km} km ={meter} meter")
    except ValueError:
        messagebox.showerror("invalid","please enter a valid  number")

root=tk.Tk()
root.title("umit_converter")
root.geometry("400x200")


frame=tk.Frame(root,bg="dark blue",borderwidth=4, relief="sunken")
frame.pack(padx=20,pady=10,fill="both",expand=True)

label=tk.Label(frame,text="enter  distance in km here")
label.pack(padx=5,pady=10)

entry=tk.Entry(frame)
entry.pack(padx=10,pady=5)

btn=tk.Button(frame,text="convert",command=calculate_km)
btn.pack(padx=10, pady=10)
root.mainloop()