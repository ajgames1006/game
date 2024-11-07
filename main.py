import customtkinter

clicks = 0
clickupgrade = 1
cost = 15

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("green")


root = customtkinter.CTk()
root.geometry("700x550")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=10,padx=60, fill="both", expand=True)

def updatebutton():
    button2.configure(text=f"Upgrade (Cost: {cost})")

def updatelable():
    lable1.configure(text=str(clicks))

def click():
    global clicks ; clicks = 1 * clickupgrade + clicks
    updatelable()

def clickup():
    global clicks
    global cost
    global clickupgrade
    if clicks >= cost:
        clicks -= cost
        clickupgrade += 1
        cost = cost * 2
        updatelable()
        updatebutton()


lable = customtkinter.CTkLabel(master=frame, text="clicker clicker")
lable.pack(pady=10, padx=12)

lable1 = customtkinter.CTkLabel(master=frame, text=str(clicks))
lable1.pack(pady=10, padx=12)

button1 = customtkinter.CTkButton(master=frame, text="click", command=click)
button1.pack(pady=15,padx=12)

button2 = customtkinter.CTkButton(master=frame, text=f"Upgrade (Cost: {cost})", command=clickup)
button2.pack(pady=15, padx=12)

root.mainloop()
