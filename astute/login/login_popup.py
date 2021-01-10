import tkinter.ttk
import tkinter.filedialog

login_window = tkinter.Tk()
login_window.title("ASTUTE - Login")
login_window.geometry("400x100")
login_window.iconbitmap("astute.ico")
text_format_01 = ("Segoe UI", 10)


def browse_license_file():
    license_extension = (("JavaScript Object Notation", "*.json"), ("All files", "*.*"))
    prompt_title = "Open License File"
    path_to_license = tkinter.filedialog.askopenfile(filetypes=license_extension, title=prompt_title)
    return path_to_license


license_label = tkinter.Label(login_window, text="Select a License File", anchor="w", font=text_format_01)
license_path = tkinter.Entry(login_window, font=text_format_01, width=38)
browse_button = tkinter.ttk.Button(login_window, text="Browse", command=browse_license_file)
login_button = tkinter.


license_label.grid(padx=20, pady=10, row=0, column=0, columnspan=2, sticky="W")
license_path.grid(padx=20, pady=0, row=1, column=0, columnspan=2)
browse_button.grid(row=1, column=2, sticky="W")


login_window.mainloop()
