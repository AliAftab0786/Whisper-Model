from openai import OpenAI
api_key = "use_your_open-ai_api-key"
client = OpenAI(api_key=api_key)

audio_file= open("./audio/test5.m4a", "rb")
print("---------------------------------")
print("Transcribing audio...")
print("This may take a few Time.")
print("Please wait...")
print("---------------------------------")
transcription = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file
)
print(transcription.text)

with (open("./txt_files/speech_to_text_4.txt", "w" , encoding="utf-8")) as file:
  file.write(transcription.text)
