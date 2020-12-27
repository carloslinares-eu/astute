import tkinter
import tkinter.scrolledtext
import PIL.ImageTk
import PIL.Image

main_window = tkinter.Tk()
main_window.title("AS2T - ATEXIS Text-to-Speech App")
main_window.geometry("640x480")
main_window.iconbitmap("as2t/as2t.ico")
text_style_01 = ("Segoe UI", 10)

text_entry_label = tkinter.Label(main_window, text="Input text", font=text_style_01, anchor="sw")
text_entry_label.grid(row=0, column=0, pady=20, padx=20, sticky="W")

# atexis_logo = PIL.ImageTk.PhotoImage(PIL.Image.open("as2t/data/images/atexis.png"))
# atexis_logo_label = tkinter.Label(image=atexis_logo)
# atexis_logo_label.grid(row=0, column=0)

text_entry = tkinter.scrolledtext.ScrolledText(main_window, font=text_style_01)
text_entry.grid(row=1, column=0, columnspan=2, padx=20, sticky="W")

main_window.mainloop()
