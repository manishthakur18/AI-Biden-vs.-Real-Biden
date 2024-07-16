from src.ai_response import generate_response
from src.text_to_speech import text_to_speech
from src.deepfake_video import create_deepfake_video
from src.video_audio_merge import merge_video_audio
from src.config import OPENAI_API_KEY

def main(question):
    print(f"Using OpenAI API Key: {OPENAI_API_KEY}")
    ai_response = generate_response(question)
    audio_file = 'data/ai_response.mp3'
    text_to_speech(ai_response, audio_file)
    create_deepfake_video(audio_file, 'data/final_output.mp4')
    merge_video_audio('data/final_output.mp4', audio_file, 'data/final_video.mp4')

if __name__ == "__main__":
    question = "What is your plan for healthcare?"
    main(question)
