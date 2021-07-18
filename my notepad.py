import tkinter as tk  #importlibraries

from tkinter.filedialog import askopenfilename ,asksaveasfilename
#function declaration
#saving file
def saving_file():
    file_location=asksaveasfilename(filetypes=[("Text files","*.txt"),["All files","*.*"]]) 
    if not file_location:
      return
    with open(file_location , "w") as file_output:
        text=edit_text.get(1.0,tk.END)
        file_output.write(text)
    window.title(f"MY NOTEPAD - {file_location}")

#declare open file fuction
def opening_file():
    file_location=askopenfilename(filetypes=[("Text files","*.txt"), ("All files", "*.*")])
    if not file_location:
        return
    edit_text.delete(1.0, tk.END)
    with open(file_location, "r") as file_input:
        text=file_input.read()
        edit_text.insert(tk.END, text)
        window.title(f"MY NOTEPAD - {file_location}")




#createwindow

window=tk.Tk()

window.title("MY NOTEPAD")

window.rowconfigure(0, minsize=700)

window.columnconfigure(1, minsize=700)

edit_text = tk.Text(window) #writeontkwindow
edit_text.grid(row=0, column=1, sticky="nsew")


#createbutton


frame_button = tk.Frame(window, relief=tk.RAISED, bd=3)
frame_button.grid(row=0, column=0, sticky="ns")


button_open = tk.Button(frame_button, text="OPEN FILE", command=opening_file)
button_open.grid(row=0, column=0, padx=5 , pady=5 ) #position for button

button_save = tk.Button(frame_button, text="SAVE AS", command=saving_file)
button_save.grid(row=1, column=0, padx=5) #positionforbutton 
window.mainloop()  #closetheloop


