from moviepy.editor import VideoFileClip



def video_to_audio(video_path, audio_path):
    # Define the input video file and output audio file
    mp4_file = video_path
    mp3_file = audio_path

    # Load the video clip
    video_clip = VideoFileClip(mp4_file)

    # Extract the audio from the video clip
    audio_clip = video_clip.audio
    
    audio_clip.write_audiofile(mp3_file)

    
    print("Audio extraction successful!")

  
    video_clip.close()
    audio_clip.close()
    
    