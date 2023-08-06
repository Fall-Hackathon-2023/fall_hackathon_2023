# Make sure to run pip install Flask pytube
# Run this file with python app.py
# Open your browser and go to http://localhost:5000

from flask import Flask, request, render_template, send_file
from pytube import YouTube
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download_audio():
    youtube_url = request.form['youtube_url']
    output_path = './downloads'
    
    try:
        # Use your existing Python code to download the audio
        yt = YouTube(youtube_url)
        stream = yt.streams.filter(only_audio=True, file_extension='mp4').first()
        if stream is not None:
            stream.download(output_path=output_path)
            original_file_path = os.path.join(output_path, stream.default_filename)
            mp3_file_path = os.path.join(output_path, yt.title + ".mp3")
            os.rename(original_file_path, mp3_file_path)
            return send_file(mp3_file_path, as_attachment=True)
        else:
            return "No audio stream available for this video."
    except Exception as e:
        return "Error occurred: " + str(e)

if __name__ == '__main__':
    app.run(debug=True)
