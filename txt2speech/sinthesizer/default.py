from google.cloud import texttospeech



# Importing JSON


# Instantiates a client
client = texttospeech.TextToSpeechClient(credentials=credentials)
input_title = "Slide15"
input_text = "A Wing is a type of fin that produces lift, while moving through air or some other fluid. As such, wings have streamlined cross-sections that are subject to aerodynamic forces and act as airfoils. A wing's aerodynamic efficiency is expressed as its lift-to-drag ratio. The lift a wing generates at a given speed and angle of attack can be one to two orders of magnitude greater than the total drag on the wing. A high lift-to-drag ratio requires a significantly smaller thrust to propel the wings through the air at sufficient lift. The selection of the configuration of the wing goes a lot depending on the requirements of operation. The aspects related to the different characteristics structural needs and aerodynamics can be decisive factors when choosing an initial setup. The final decision must be subject to maximizing the flexibility of operation of the final design."
synthesis_input = texttospeech.SynthesisInput(text=input_text)

# Build the voice request, select the language code ("en-US") and the ssml
# voice gender ("neutral")
voice = texttospeech.VoiceSelectionParams(
    language_code="en-GB", ssml_gender=texttospeech.SsmlVoiceGender.MALE, name="en-GB-Wavenet-B"
)

# Select the type of audio file you want returned
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3, speaking_rate=0.80
)

# Perform the text-to-speech request on the text input with the selected
# voice parameters and audio file type
response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

# The response's audio_content is binary.
with open(input_title + ".mp3", "wb") as out:
    # Write the response to the output file.
    out.write(response.audio_content)
    print("Audio content written to file " + input_title + ".mp3")
