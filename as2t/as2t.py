import tkinter
import tkinter.messagebox
import PIL.ImageTk
import PIL.Image

main_window = tkinter.Tk()
main_window.title("AS2T - ATEXIS Text-to-Speech App")
main_window.geometry("640x480")
main_window.iconbitmap("as2t/as2t.ico")


def dummy_command():
    pass


def show():
    show_hide_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=20)


def hide():
    show_hide_frame.grid_forget()


def radio():
    radio_label = tkinter.Label(main_window, text=regular_variable.get())
    radio_label.grid(row=4, column=2)


def popup():
    tkinter.messagebox.askquestion(title="Warning message", message="Bad!")

# atexis_logo = PIL.ImageTk.PhotoImage(PIL.Image.open("as2t/data/images/atexis.png"))
# atexis_logo_label = tkinter.Label(image=atexis_logo)
# atexis_logo_label.grid(row=0, column=0)

# text_entry = tkinter.Entry(main_window, width=300, font=("Segoe UI", 9))
# text_entry.grid(row=1, column=1)

# Define Menu
main_menu = tkinter.Menu(main_window)
main_window.config(menu=main_menu)

# Create Menu Items
file_menu = tkinter.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=dummy_command)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=main_window.quit)

# Create another submenu Edit
edit_menu = tkinter.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=dummy_command)
edit_menu.add_command(label="Copy", command=dummy_command)
edit_menu.add_command(label="Paste", command=dummy_command)

show_button = tkinter.Button(main_window, text="Show", command=show)
hide_button = tkinter.Button(main_window, text="Hide", command=hide)

show_button.grid(row=0, column=0)
hide_button.grid(row=0, column=1)

show_hide_frame = tkinter.Frame(main_window, width=200, heigh=200, bd=5, bg="blue", relief="sunken")
show_hide_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

show_hide_frame_label = tkinter.Label(show_hide_frame, text="Hello World", font=("Helvetica", 20))
show_hide_frame_label.pack(padx=20, pady=20)

status = tkinter.Label(main_window, text="Waiting", bd=2, relief="sunken", width=60)
status.grid(row=2, column=0)

regular_variable = tkinter.IntVar()

radio_button_01 = tkinter.Radiobutton(main_window, text="One", variable=regular_variable, value=1)
radio_button_02 = tkinter.Radiobutton(main_window, text="Two", variable=regular_variable, value=2)

radio_button_01.grid(row=2, column=2)
radio_button_02.grid(row=2, column=3)

radio_control = tkinter.Button(main_window, text="Click Me", command=radio)
radio_control.grid(row=3, column=2)

# Create checkboxes
var = tkinter.BooleanVar()
checkbutton = tkinter.Checkbutton(main_window, text="Pepperoni", variable=var, onvalue=True, offvalue=False)
checkbutton.grid(row=3, column=1)

pop_button = tkinter.Button(main_window, text="Click to Popup", command=popup)
pop_button.grid(row=4, column=1)

main_window.mainloop()
