import tkinter
import tkinter.messagebox
import tkinter.scrolledtext
import tkinter.ttk
import tkinter.filedialog
import google
import google.oauth2.service_account
import google.cloud.translate_v2
import google.auth.exceptions


class MainApp:
    def __init__(self, app_icon, credentials=None):
        self.credentials = credentials
        self.client = google.cloud.translate_v2.Client(credentials=self.credentials)
        self.root = tkinter.Tk()
        self.root.title("ASTUTE - ATEXIS Text-to-Speech App")
        self.root.geometry("480x300")
        self.root.resizable(0, 0)
        self.root.iconbitmap(app_icon.path)
        self.large = ("Segoe UI", 10)
        self.medium = ("Segoe UI", 8)
        self.small = ("Segoe UI", 6)

        self.language_codes = ["en-GB", "en-US", "es-ES"]
        self.genders = ["Male", "Female"]
        self.voice_types = ["Regular", "Wavenet"]
        self.available_voices = ["B", "A"]
        self.voice_speed = tkinter.IntVar()

        self.input_text_label = tkinter.Label(self.root, text="Input text", anchor="w")
        self.input_text_box = tkinter.scrolledtext.ScrolledText(self.root, font=self.large, width=60, height=6)

        self.language_code_label = tkinter.Label(self.root, text="Language Code", anchor="w")
        self.language_code_dropdown = tkinter.ttk.Combobox(self.root, value=self.language_codes)

        self.gender_label = tkinter.Label(self.root, text="Gender")
        self.gender_dropdown = tkinter.ttk.Combobox(self.root, value=self.genders)

        self.voice_type_label = tkinter.Label(self.root, text="Voice Type")
        self.voice_type_dropdown = tkinter.ttk.Combobox(self.root, value=self.voice_types)

        self.voice_label = tkinter.Label(self.root, text="Voice Name")
        self.voice_dropdown = tkinter.ttk.Combobox(self.root, value=self.available_voices)
        self.voice_dropdown.configure(postcommand=self.voice_dropdown.configure(values=self.get_voices()))

        self.speed_label = tkinter.ttk.Label(self.root, textvariable=self.voice_speed)
        self.speed_slider = tkinter.ttk.Scale(self.root, from_=0.2, to=2, variable=self.voice_speed)

        self.synthesize = tkinter.ttk.Button(self.root, text="Synthesize!", command=self.synthesize)

    def initialize(self):
        self.input_text_label.grid(padx=20, pady=5, row=0, column=0, sticky="w")
        self.input_text_box.grid(padx=20, pady=5, row=1, column=0, columnspan=3, rowspan=6)

        self.language_code_label.grid(padx=20, pady=5, row=8, column=0, sticky="w")
        self.language_code_dropdown.grid(padx=20, pady=5, row=8, column=2, sticky="e")

        self.gender_label.grid(padx=20, pady=5, row=9, column=0, sticky="w")
        self.gender_dropdown.grid(padx=20, pady=5, row=9, column=2, sticky="e")

        self.voice_label.grid(padx=20, pady=5, row=10, column=0, sticky="w")
        self.voice_dropdown.grid(padx=20, pady=5, row=10, column=2, sticky="e")

        self.speed_label.grid()
        self.speed_slider.grid(padx=20, pady=5, row=11, column=2, sticky="e")

        self.synthesize.grid(padx=20, pady=5, row=12, column=2, sticky="e")

        self.root.mainloop()

    def get_voices(self):
        pass

    def synthesize(self):
        pass
