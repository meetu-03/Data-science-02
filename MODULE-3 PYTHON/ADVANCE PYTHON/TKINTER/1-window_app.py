import tkinter as tk
# create a main windows 
root=tk.Tk()
# create a title of your software windows
root.title("Blank windows for software or simple windows for software")
# create a windows size
root.geometry("600x400")
# create a label of windows
label=tk.Label(root,text="Hello\nI am Meetuuu", fg="red", font=("Arial",30))
# set a position  with border and content and provides a space in content padding
label.pack(pady=50)
# print a window 
root.mainloop()