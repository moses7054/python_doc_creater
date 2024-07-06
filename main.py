from utilis.video_to_audio import video_to_audio
from utilis.audio_to_text import audio_to_text
from utilis.load_srt import load_srt
from utilis.get_doc import gettingdoc
from utilis.write_md import write_md


video_path = "D:/coding/python_whisper_srt/static/source.mp4"  # Path to get the video file.
audio_path = "D:/coding/python_whisper_srt/static/audio.mp3"  # Path where audio file will be saved. 
transcription_path = "D:/coding/python_whisper_srt/static/transcription.srt"   # Path where transcription file will be saved.
md_path = "D:/coding/python_whisper_srt/static/loom_guide.md"   # Path where .md file will be saved.


video_to_audio(video_path, audio_path)  
audio_to_text(audio_path, transcription_path)

srttext = load_srt(transcription_path) # Loads srt file into srttext variable.
prompt = "You are a technical writer, specializing in writing easy to understand documentation.You are provided with a srt file of a presentation.Please create documentaion"
# prompt varible is used to send the peompt to llm.

document_md = gettingdoc(srttext, prompt)  # sending srt text and prompt to llm and getting the the reply and storing it into a variavle.

write_md(document_md, md_path)  # Saving the .md file  