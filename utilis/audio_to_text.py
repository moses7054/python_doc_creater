from openai import OpenAI
from dotenv import load_dotenv

def audio_to_text(audiopath, trascrtpath):
  load_dotenv()
  client = OpenAI()

  audio_file = open(audiopath, "rb")
  transcription = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file, 
    response_format="srt",

  )
  print("transcription successful")

  file_path = trascrtpath

  # Open the file in write mode
  with open(file_path, 'w') as file:
      # Write the SRT content to the file
      file.write(transcription)

  # File is automatically closed after the `with` block
  print(f"SRT file saved successfully at: {file_path}")