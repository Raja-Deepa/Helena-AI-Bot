# Helena-AI-Bot
Helena is a Python-based personal assistant that automates tasks and provides a hands-free user experience. It can greet the user, search Wikipedia, open websites and applications, send emails, report the time, and more, all through voice commands.

# Features
Greeting: Wishes the user based on the time of day.
Voice Commands: Listens and responds to user commands.
Wikipedia Search: Fetches and reads Wikipedia summaries.
Web Navigation: Opens popular websites like YouTube and Google.
Application Launch: Opens local applications like Spotify and VS Code.
Email Sending: Sends emails via Gmail.
Time Reporting: Announces the current time.
Shutdown Command: Exits the assistant on command.

# Technologies Used
Python:Core language.
pyttsx3: Text-to-speech.
SpeechRecognition: Speech-to-text.
wikipedia: Wikipedia API.
webbrowser: Web browser control.
os: Operating system interactions.
smtplib: Email sending.
subprocess: Process management.

# Installation
Clone the repository and install dependencies:

(bash)
git clone https://github.com/yourusername/helena.git
cd helena
pip install -r requirements.txt

# Usage
Run the main script:
(bash)
python helena.py
Helena will start and listen for your voice commands

# Example Commands
"Wikipedia Albert Einstein"
"Open YouTube"
"Send email to Deepa"
"What time is it?"
"Quit Helena"

# Security Note
Handle email credentials securely using environment variables or secure storage solutions
