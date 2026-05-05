# 🎙️ AI Audio Transcriber
> **High-speed, local audio transcription using Django & Faster-Whisper.**

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092e20.svg?style=for-the-badge&logo=django&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![TailwindCSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white)

---

## ⚡ Overview
This is a modular transcription service that utilizes **FastAPI**, and the **Faster-Whisper** engine. It leverages **8-bit quantization** via CTranslate2 to enable efficient CPU-based execution, bringing transcription times down from minutes to seconds.



## 🛠️ Installation & Setup

### 1. Environment Configuration
Clone the repo and set up your isolated environment:
```bash
# Clone the repository
git clone https://github.com/zaheerfarman/transcribe.git
cd transcribe

# Setup Virtual Environment
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```


### 2. Database & Storage
Initialize the database and create local media storage:

```bash
python manage.py makemigrations
python manage.py migrate
mkdir media
```


## 🚀 How It Works
> **Normalization: Incoming audio is normalized to 16kHz Mono using pydub and FFmpeg to reduce the Word Error Rate (WER).

> **Inference: The WhisperModel is loaded globally (stateless) into RAM using int8 compute type.

> **Output: The pipeline returns structured text with timestamps and confidence scores.