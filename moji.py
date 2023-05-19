import os
from dotenv import load_dotenv
import math
import sys
from pytube import YouTube
from pydub import AudioSegment
import openai

# Load environment variables from .env file
load_dotenv()

# Set API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# YouTube URL
youtube_url = sys.argv[1]  # Get YouTube URL from command line argument

# Directories for saving audio files
output_dir = "output"
transcription_output_dir = "input"  # Directory for saving transcription results

# Length of audio segments to split (in milliseconds)
chunk_length_ms = 5 * 60 * 1000  # 10 minutes

# Download audio from YouTube
youtube = YouTube(youtube_url)
video = youtube.streams.first()
audio_file_path = video.download(output_dir)

# Convert audio to wav format
audio = AudioSegment.from_file(audio_file_path)
wav_file_path = os.path.join(output_dir, "audio.wav")
audio.export(wav_file_path, format="wav")

# Split the audio
audio = AudioSegment.from_wav(wav_file_path)
chunks = math.ceil(len(audio) / chunk_length_ms)

for i in range(chunks):
    start_time = i * chunk_length_ms
    end_time = (i + 1) * chunk_length_ms if (i + 1) * chunk_length_ms < len(audio) else len(audio)
    chunk = audio[start_time:end_time]

    # Save the split audio as a temporary file
    chunk_file_path = os.path.join(output_dir, f"chunk_{i}.wav")
    chunk.export(chunk_file_path, format="wav")

    # Transcribe the audio using the OpenAI API
    with open(chunk_file_path, 'rb') as audio_file:
        result = openai.Audio.transcribe("whisper-1", audio_file, language='en')

    # Display the result
    print(f"Chunk {i} transcription: {result['text']}")

    # Save the result to a text file
    with open(os.path.join(transcription_output_dir, f"transcription_{i}.txt"), 'w', encoding='utf-8') as output_file:
        output_file.write(result['text'])

    # Delete the temporary file
    os.remove(chunk_file_path)
