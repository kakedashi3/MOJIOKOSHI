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

```bash
cp .env.example .env
```

Then, open the .env file and replace your_api_key_here with your OpenAI API key:

```dotenv
OPENAI_API_KEY=your_api_key_here
```

Usage
You can run the script from the command line with the YouTube video URL as an argument. For example:

```bash
python your_script.py https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

This script accomplishes a multi-step process: it downloads a YouTube video, extracts the audio, splits the audio into manageable chunks, and transcribes each chunk. The transcriptions are both displayed in the console and saved as individual text files in the 'input' directory. Additionally, each chunk of audio is stored as a .wav file in the 'output' directory.

To manage environment variables, such as your OpenAI API key, we use a .env file. To help set this up, we provide a .env.example file. This example file serves as a template, showing you the necessary format and variables needed for the script to work correctly.

The .env.example file should look like this:

dotenv
Copy code
# .env.example
OPENAI_API_KEY=your_api_key_here
To use it, simply make a copy of the .env.example file, rename it to .env, and replace your_api_key_here with your actual OpenAI API key.
