from flask import Flask, request, jsonify
from openai import OpenAI
from gtts import gTTS
from flask_cors import CORS
client = OpenAI()

app = Flask(__name__)
CORS(app) 


@app.route('/audio-to-text', methods=['POST'])
def audio_to_text():
    try:
        print("Converting audio to text...")
        audio_file = request.files['audio']
        temp_filename = '/tmp/temp.m4a'
        audio_file.save(temp_filename)
        audio_file = open(temp_filename, 'rb')

        # Convert audio to text using Whisper ASR
        transcript = convert_audio_to_text(audio_file)
        print("Transcript:", transcript)

        # Generate meeting minutes from the provided transcript
        meeting_minutes = generate_meeting_minutes(transcript)
        print("Meeting Minutes:", meeting_minutes)

        # Convert meeting minutes to speech
        speech_file = convert_text_to_speech(meeting_minutes)

        # Return the meeting minutes
        return jsonify({'meeting_minutes': meeting_minutes})

    except Exception as e:
        print(e)
        return jsonify({'error': 'Internal Server Error'}), 500

def convert_audio_to_text(audio_file):
    try:
        print("Creating transcripts")
        # Make a call to OpenAI API to transcribe audio
        response = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
            response_format="text"
        )

        return response
    except Exception as e:
        print(e)
        raise e
    

def generate_meeting_minutes(transcript):
    try:
        # Send the provided prompt to OpenAI API
        prompt = """
            Generate captivating meeting minutes from the provided meeting transcript. 

            Meeting Highlights:
            - Summarize the most exciting and noteworthy moments from the meeting in a paragraph format.

            Meeting Minutes:
            - Include a comprehensive summary of the topics and agendas discussed during the meeting.

            Actionable Insights:
            - Provide actionable insights or key takeaways from the meeting that can drive future decisions or actions.

            TODOs:
            - Take note of any action items or tasks mentioned by team members.

            Additional Facts/Insights:
            - Provide any relevant additional information or insights related to the meeting.
        """
        response = client.chat.completions.create(
            model="gpt-3.5-turbo", # replace witht the model you are using
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": "Meeting Transcript:\n" + transcript}
            ],
            stream=False
        )

        return response.choices[0].message.content
    except Exception as e:
        print(e)
        raise e

def convert_text_to_speech(text):
    try:
        # Convert text to speech using gTTS
        tts = gTTS(text=text, lang='en')
        speech_file = '/tmp/meeting_minutes.mp3' # replace with your own audio file path
        tts.save(speech_file)

        return speech_file
    except Exception as e:
        print(e)
        raise e

if __name__ == "__main__":
    app.run(port=8001)
