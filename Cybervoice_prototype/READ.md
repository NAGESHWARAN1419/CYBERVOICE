
# CyberVoice – Cybersecurity Awareness Assistant

**Speak in your language. Understand the threat. Stay safe online.**

## About the Project

CyberVoice is a beginner-friendly Python cybersecurity awareness prototype designed to help users recognize potential warning signs in suspicious messages.

It checks user-provided text for predefined keywords and provides relevant cybersecurity safety recommendations.

## Problem Statement

Many smartphone users struggle to identify phishing messages, fake bank alerts, suspicious links and online scams.

CyberVoice aims to make basic cybersecurity awareness easier to understand.

## Features

- Suspicious keyword detection
- English and Tamil safety recommendations
- Warning severity classification
- Cybersecurity safety tips
- Interactive menu
- Basic input validation

## Technologies Used

- Python
- Visual Studio Code

## How It Works

1. The user selects a language.
2. The user enters a suspicious message.
3. CyberVoice converts the message to lowercase.
4. It checks for predefined warning keywords.
5. It displays detected keywords and related safety advice.

## Installation

1. Install Python 3.
2. Clone this repository.
3. Open the project folder in VS Code.
4. Run:

```bash
python cybervoice.py
```

On Windows, you can also use:

```powershell
py cybervoice.py
```

## Current Limitations

- Uses keyword matching, not artificial intelligence.
- Does not understand the full context of a message.
- May produce false positives and miss suspicious messages.
- Does not currently support voice input or speech output.
- A low or high warning level is not proof that a message is fraudulent or legitimate.

## Future Improvements

- Voice input and speech output
- Tamil and English voice interaction
- Tanglish support
- Context-aware scam detection
- AI-assisted cybersecurity explanations
- Improved privacy protection

## Safety Notice

Do not enter real OTPs, passwords, PINs or banking credentials.

CyberVoice is an educational prototype and should not be used as a substitute for professional security verification.

## Project Status

Version 1.0 – Basic Python prototype.
