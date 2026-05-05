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
git clone <your-repo-url>
cd <your-repo-name>

# Setup Virtual Environment
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt