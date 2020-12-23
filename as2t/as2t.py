import tkinter
import PIL.ImageTk
import PIL.Image

main = tkinter.Tk()
main.title("AS2T - ATEXIS Text-to-Speech App")
main.geometry("640x480")
main.iconbitmap("as2t/as2t.ico")

atexis_logo = PIL.ImageTk.PhotoImage(PIL.Image.open("as2t/data/images/atexis.png"))
atexis_logo_label = tkinter.Label(image=atexis_logo)
atexis_logo_label.grid(row=0, column=0)

text_entry = tkinter.Entry(main, width=300, font=("Segoe UI", 9))
text_entry.grid(row=1, column=1)

main.mainloop()

