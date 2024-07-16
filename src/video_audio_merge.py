from moviepy.editor import VideoFileClip, AudioFileClip

def merge_video_audio(video_file, audio_file, output_file):
    video = VideoFileClip(video_file)
    audio = AudioFileClip(audio_file)
    final_video = video.set_audio(audio)
    final_video.write_videofile(output_file, codec="libx264", audio_codec="aac")
