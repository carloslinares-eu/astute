from google.cloud import texttospeech
import astute.login.local

# Authentication
credentials, scoped_credentials = astute.login.local.login_with_json("./astute/login/gcloud_credentials.json")

# Instantiates a client
client = texttospeech.TextToSpeechClient(credentials=credentials)
input_title = "Viesgo"
input_text = "Una vez creada la tarea, podemos crear subtareas asociadas en caso de necesitarse."
synthesis_input = texttospeech.SynthesisInput(text=input_text)

# Build the voice request, select the language code ("en-US") and the ssml
# voice gender ("neutral")
voice = texttospeech.VoiceSelectionParams(
    language_code="es-ES", ssml_gender=texttospeech.SsmlVoiceGender.MALE, name="es-ES-Wavenet-B"
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
