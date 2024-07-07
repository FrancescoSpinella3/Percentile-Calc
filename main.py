import tkinter as tk
from tkinter import *
from tkinter import ttk
import customtkinter

# PROGRAM TO PERCENTAGE CALCULATION
def percentage_calculation():
    try:
        starter_value = float(entry1.get())  # USER ENETER THE STARTER VALUE
        final_value = float(entry2.get())  # USER ENETER THE FINAL VALUE

        result = (final_value / starter_value) * 100 - 100  # CALCULATE THE RESULT
        label_result.config(text=f"Result: {result:.2f}%")

    except ValueError as error:
        label_result.config(text="Error: Enter a valid value")

# CREATING MAIN WINDOW
root = customtkinter.CTk()
root.resizable(width=False, height=False)
root.config(bg= "white")
root.eval('tk::PlaceWindow . center')
root.title("")
root.iconbitmap("percent_icon.ico")
root.geometry("200x250")


# CREATING CENTRAL FRAME
central_frame = tk.Frame(root, bg= "white") # CAMBIARE BACKGROUND COLOR NEL FRAME E RENDERLO UGUALE AL RESTO: GRIGIO SCURO
central_frame.pack(expand=True)

# CREATING WIDGETS INSIDE CENTRAL FRAME
label1 = tk.Label(central_frame, 
                #   text="First value", 
                  font= "bold"
                  )
label1.pack(pady=2)

entry1 = customtkinter.CTkEntry(central_frame, 
                                corner_radius= 50,
                                text_color= "black",
                                placeholder_text= "First number",
                                fg_color= ("blue", "white")
                                )
entry1.pack(pady=5)

label2 = tk.Label(central_frame, 
                #   text="Second value", 
                  font= "bold"
                  )
label2.pack(pady=5)

entry2 = customtkinter.CTkEntry(central_frame, 
                                corner_radius= 50,
                                text_color= "black",
                                placeholder_text= "Second number",
                                fg_color= ("blue", "white")
                                )
entry2.pack(pady=5)

# BUTTON TO DO THE CALCULATION
button = customtkinter.CTkButton(master=central_frame, 
                                 text="Calculate", 
                                 command=percentage_calculation, 
                                 font= ("Arial", 15)
                                 )
button.pack(pady=5)

# LABEL TO SHOW THE RESULT
label_result = tk.Label(central_frame, 
                        text="Result: ", 
                        font= "bold", 
                        bg= "white"
                        )
label_result.pack(pady=8)

root.mainloop()







