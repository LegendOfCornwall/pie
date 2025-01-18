import tkinter as tk

index = 0  # Define the index as a global variable

def updateData():
    global index
    myList = ["Hi", "Hey", "Ho", "AAHAHHAHAH"]

    # Clear any existing labels by destroying them
    for widget in window.winfo_children():
        widget.destroy()
    
    # Display the current label
    label = tk.Label(text=myList[index], width="100")
    label.pack()

    # Update the index for the next label
    index = (index + 1) % len(myList)

    # Schedule updateData to be called again after 1 second
    window.after(1000, updateData)

window = tk.Tk()

updateData()  # Start the update loop

window.mainloop()
