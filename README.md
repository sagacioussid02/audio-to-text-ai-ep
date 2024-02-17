## Description

This exposes a REST endpoint POST `/audio-to-text` to convert an audio file to text

## USAGE
This project is currently configured to use in local environments. This is not a production code.
- Clone this project locally.
- Install the dependencies:
    `pip install -r requirements.txt`
- Export the following API Key variable in your local:
   `OPENAI_API_KEY=<Your OPENAI API Key>`
- Replace with your own meeting transcripts audio file:
    `speech_file = '/tmp/meeting_minutes.mp3' # replace with your own audio file path`


## Run
Follow these steps to run the project:
- If you are using python virtual environment then install the dependencies:
   `pip install -r requirements.txt`
- Run the Flask project:
    `python app.py`

    ```
         * Serving Flask app 'app'
         * Debug mode: off
        WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
         * Running on http://127.0.0.1:8001
        Press CTRL+C to quit
    ```
