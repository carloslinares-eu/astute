import tkinter
import tkinter.messagebox
import tkinter.scrolledtext
import tkinter.ttk
import PIL.ImageTk
import PIL.Image

main_window = tkinter.Tk()
main_window.title("ASTUTE - ATEXIS Text-to-Speech App")
main_window.geometry("480x480")
main_window.iconbitmap("astute.ico")
text_format_01 = ("Segoe UI", 10)
main_width = 60

language_codes = ["en-GB", "en-US", "es-ES"]
genders = ["Male", "Female"]
voice_types = ["Regular", "Wavenet"]
available_voices = ["B", "A"]


def check_voices():
    pass


input_text_label = tkinter.Label(main_window, text="Input text", anchor="w")
input_text_box = tkinter.scrolledtext.ScrolledText(main_window, font=text_format_01, width=main_width, height=6)

language_code_label = tkinter.Label(main_window, text="Language Code", anchor="w")
language_code_dropdown = tkinter.ttk.Combobox(main_window, value=language_codes)

gender_label = tkinter.Label(main_window, text="Gender")
gender_dropdown = tkinter.ttk.Combobox(main_window, value=genders)

voice_type_label = tkinter.Label(main_window, text="Voice Type")
voice_type_dropdown = tkinter.ttk.Combobox(main_window, value=voice_types)

voice_selection_label = tkinter.Label(main_window, text="Voice Name")
voice_check_button = tkinter.ttk.Button(main_window, text="Check available voices", command=check_voices)
voice_selection_dropdown = tkinter.ttk.Combobox(main_window, value=available_voices)


input_text_label.grid(padx=20, pady=5, row=0, column=0, sticky="w")
input_text_box.grid(padx=20, pady=5, row=1, column=0, columnspan=3, rowspan=6)

language_code_label.grid(padx=20, pady=5, row=8, column=0, sticky="w")
language_code_dropdown.grid(padx=20, pady=5, row=8, column=2, sticky="e")

gender_label.grid(padx=20, pady=5, row=9, column=0, sticky="w")
gender_dropdown.grid(padx=20, pady=5, row=9, column=2, sticky="e")

voice_selection_label.grid(padx=20, pady=5, row=10, column=0, sticky="w")
voice_check_button.grid(pady=5, row=10, column=1, sticky="e")
voice_selection_dropdown.grid(padx=20, pady=5, row=10, column=2, sticky="e")

main_window.mainloop()
