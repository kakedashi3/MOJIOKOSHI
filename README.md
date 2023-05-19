# YouTube Audio Transcription using OpenAI

This script downloads a YouTube video, extracts the audio, and transcribes it using the OpenAI API.

## Requirements

To run this script, you need the following packages:

```Requirements
python-dotenv==0.19.1
pytube==11.0.1
pydub==0.25.1
openai==0.27.0
```

You can install these packages using pip:

```bash
pip install -r requirements.txt
```

## OpenAI API Key
This script uses the OpenAI API for transcription. To use it, you need an OpenAI API key. Set this key as an environment variable in a .env file in the same directory as your script.

First, make a copy of the .env.example file:

bash
Copy code
cp .env.example .env
Then, open the .env file and replace your_api_key_here with your OpenAI API key:

dotenv
Copy code
OPENAI_API_KEY=your_api_key_here
Usage
You can run the script from the command line with the YouTube video URL as an argument. For example:

```bash
Copy code
python your_script.py https://www.youtube.com/watch?v=dQw4w9WgXcQ
This will download the video, extract and chunk the audio, and transcribe each chunk. The transcriptions will be printed to the console and also saved as text files in the input directory. Each chunk's audio is saved as a .wav file in the output directory.



---

The `.env.example` file is used as a template for the `.env` file. This allows users to easily set environment variables. The `.env.example` file should be created as follows

```dotenv
# .env.example

OPENAI_API_KEY=your_api_key_here
