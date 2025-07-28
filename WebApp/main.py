# main.py
from flask import Flask, request, jsonify, send_file, Response
from flask_cors import CORS
from tutor import get_ai_response_with_history
from elevenlabs import ElevenLabs
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

# Initialize ElevenLabs client
elevenlabs = ElevenLabs(api_key=os.getenv("ELEVEN_API_KEY"))

@app.route('/')
def index():
    return send_file('voice_tutor.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    transcript = data.get('transcript', '')
    history = data.get('history', [])
    
    try:
        response, updated_history = get_ai_response_with_history(
            transcript, history, max_turns=2
        )
        return jsonify({
            'response': response,
            'history': updated_history
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/tts', methods=['POST'])
def text_to_speech():
    data = request.json
    text = data.get('text', '')
    
    if not text.strip():
        return jsonify({'error': 'No text provided'}), 400
    
    try:
    
        audio_stream = elevenlabs.text_to_speech.stream(
            text=text,
            voice_id="JBFqnCBsd6RMkjVDRZzb",
            model_id="eleven_multilingual_v2"
        )
        
        
        audio_data = b""
        for chunk in audio_stream:
            audio_data += chunk
        
        return Response(
            audio_data,
            mimetype="audio/mpeg",
            headers={"Content-Disposition": "attachment; filename=speech.mp3"}
        )
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)