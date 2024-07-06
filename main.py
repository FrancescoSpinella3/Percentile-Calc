import tkinter as tk
from tkinter import *
from tkinter import ttk



# PROGRAM TO PERCENTAGE CALCULATION
def percentage_calculation():
    try:
        starter_value = float(entry1.get()) # USER ENETER THE STARTER VALUE
        final_value = float(entry2.get()) # USER ENETER THE FINAL VALUE

        result = (final_value / starter_value) * 100 - 100 # CALCULATE THE RESULT
        label_result.config(text= f"Result: {result:.2f}")
        #return input("Press Enter to exit.")
    except ValueError as error:
        label_result.config(text= "Error: Enter a valid value")
        #return input("Press Enter to exit. ")

# CREATING MAIN WINDOW 
root = tk.Tk()
root.title("Percentile calculation")
root.geometry("300x200")

#CREATING WIDGET
label1 = tk.Label(root, text= "First value")
label1.pack(pady= 5)

entry1 = tk.Entry(root)
entry1.pack(pady= 5)

label2 = tk.Label(root, text= "Second value")
label2.pack(pady= 5)

entry2 = tk.Entry(root)
entry2.pack(pady= 5)

# BUTTON TO DO THE CALCULATION
button = tk.Button(root, text= "Calculate", command= percentage_calculation)
button.pack(pady= 10)

# LABEL TO SHOW TH RESULT
label_result = tk.Label(root, text= "Result: ")
label_result.pack(pady= 5)
root.mainloop()


#print(percentage_calculation())







