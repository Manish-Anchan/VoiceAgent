# 🧞‍♂️ Genie - AI Voice Tutor

An interactive voice-based English tutor designed for children aged 6-12. Genie uses advanced AI to provide personalized English learning through natural conversation, with high-quality text-to-speech and real-time speech recognition.

## ✨ Features

- **🎙️ Continuous Voice Recognition**: Real-time speech-to-text using Web Speech API
- **🔊 High-Quality Text-to-Speech**: Premium voice synthesis powered by ElevenLabs
- **🤖 AI-Powered Tutoring**: Intelligent responses using Groq's Llama 3.3 70B model
- **👶 Child-Friendly Design**: Safe, encouraging, and age-appropriate interactions
- **💬 Interactive Conversations**: Maintains conversation history for contextual responses
- **🌐 Web-Based Interface**: No installation required, works in any modern browser
- **📱 Responsive Design**: Works on desktop, tablet, and mobile devices

## 🚀 Live Demo

Try Genie live at: **https://voiceagent-edjq.onrender.com/**

## 🛠️ Technology Stack

- **Frontend**: Vanilla JavaScript, HTML5, CSS3
- **Backend**: Python Flask
- **AI Model**: Groq Llama 3.3 70B Versatile
- **Speech Recognition**: Web Speech API
- **Text-to-Speech**: ElevenLabs API
- **Deployment**: Railway/Render/Heroku compatible

## 📋 Prerequisites

- Python 3.8+
- Modern web browser (Chrome, Edge, Firefox, Safari)
- API Keys for:
  - [Groq](https://groq.com/) - For AI responses
  - [ElevenLabs](https://elevenlabs.io/) - For text-to-speech
  - [LangSmith](https://smith.langchain.com/) - For monitoring (optional)

## 🔧 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/voice-tutor.git
cd voice-tutor
```

### 2. Create Virtual Environment
```bash
python -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file in the project root:
```env
GROQ_API_KEY=your_groq_api_key_here
ELEVEN_API_KEY=your_elevenlabs_api_key_here
LANGSMITH_API_KEY=your_langsmith_api_key_here
LANGSMITH_TRACING=true
LANGSMITH_PROJECT=VoiceAssistant
```

### 5. Run the Application
```bash
python main.py
```

Visit `http://localhost:5000` in your browser.

## 📁 Project Structure

```
voice-tutor/
├── main.py                 # Flask web application
├── voice_tutor.html        # Frontend interface
├── requirements.txt        # Python dependencies
├── Procfile               # For deployment
├── .env                   # Environment variables (create this)
├── .gitignore            # Git ignore file
├── README.md             # This file
└── backend/
    ├── tutor.py          # AI conversation logic
    ├── logger.py         # Logging configuration
    ├── tts_client.py     # ElevenLabs TTS client (legacy)
    └── stt_client.py     # AssemblyAI STT client (legacy)
```

## 🎯 How to Use

1. **Start the Application**: Run `python main.py` and open `http://localhost:5000`

2. **Begin Conversation**: Click the microphone button to start continuous listening mode

3. **Talk Naturally**: Speak in English - Genie will listen continuously and respond when you pause

4. **Interactive Learning**: Genie will:
   - Correct mistakes gently
   - Ask follow-up questions
   - Encourage continued practice
   - Maintain conversation context

5. **Controls**:
   - 🎤 **Microphone Button**: Start/stop continuous listening
   - 🗑️ **Clear Button**: Reset conversation history
   - ⏹️ **Stop Button**: Stop current speech playback

## 🔧 Configuration

### Customize AI Behavior
Edit `backend/tutor.py` to modify:
- Conversation prompts
- Response style
- Learning objectives
- Age-appropriate content filters

### Change Voice Settings
Modify `main.py` to adjust:
- Voice ID (line with `voice_id=`)
- Speech model (`model_id=`)
- Voice parameters

### UI Customization
Edit `voice_tutor.html` to change:
- Colors and styling
- Layout and animations
- Button behavior
- Status messages

## 📚 API Endpoints

- `GET /` - Serves the web interface
- `POST /api/chat` - Processes conversation input
  ```json
  {
    "transcript": "Hello, how are you?",
    "history": ["previous", "messages"]
  }
  ```
- `POST /api/tts` - Generates speech audio
  ```json
  {
    "text": "Hello there!"
  }
  ```

## 🔒 Security & Privacy

- All conversation data is processed in real-time
- No conversation history is permanently stored
- API keys are securely handled via environment variables
- Child-safe content filtering is implemented
- No personal data collection

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Troubleshooting

### Common Issues

**Speech Recognition Not Working**:
- Use Chrome or Edge browser
- Ensure microphone permissions are granted
- Check if HTTPS is enabled (required for speech recognition)

**No Audio Output**:
- Verify ElevenLabs API key is valid
- Check browser audio permissions
- Ensure speakers/headphones are connected

**AI Not Responding**:
- Verify Groq API key is valid
- Check internet connection
- Review Flask server logs for errors

### Getting Help

- Check the [Issues](https://github.com/yourusername/voice-tutor/issues) page
- Review Flask and browser console logs
- Test API endpoints individually

## 🙏 Acknowledgments

- [Groq](https://groq.com/) for fast AI inference
- [ElevenLabs](https://elevenlabs.io/) for high-quality voice synthesis
- [LangChain](https://langchain.com/) for AI orchestration
- [Flask](https://flask.palletsprojects.com/) for the web framework

## 📊 Monitoring

The application includes LangSmith integration for monitoring AI interactions:
- Track conversation quality
- Monitor response times
- Analyze user engagement patterns
- Debug AI behavior

## 🔮 Future Enhancements

- [ ] Multi-language support
- [ ] Progress tracking and analytics
- [ ] Custom voice training
- [ ] Mobile app version
- [ ] Offline mode capabilities
- [ ] Advanced conversation topics
- [ ] Parent dashboard
- [ ] Learning games integration

---

**Built with ❤️ for young English learners everywhere!**
