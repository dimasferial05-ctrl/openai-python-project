```markdown
# OpenAI API in Python (Groq Integration) 🤖

Proyek ini adalah implementasi *Command Line Interface* (CLI) Chatbot interaktif menggunakan Python. Proyek ini dibangun untuk menyelesaikan tantangan dari [roadmap.sh](https://roadmap.sh/projects/openai-api-python) dengan tujuan memahami cara berinteraksi dengan Large Language Models (LLMs) secara terprogram di luar antarmuka browser.

Karena limitasi kuota pada OpenAI API standar, proyek ini menggunakan **Groq API** yang 100% kompatibel dengan *library* OpenAI Python untuk mendemonstrasikan pemanggilan model secara gratis dan sangat cepat.

## ✨ Fitur & Konsep yang Dipelajari

- **API Integration:** Menghubungkan *library* resmi `openai` di Python ke *endpoint* kustom (Groq API).
- **Environment Variables:** Mengamankan kredensial (API Key) menggunakan pustaka `python-dotenv` agar tidak terekspos di dalam kode sumber.
- **LLM Parameters Tuning:** Bereksperimen dengan parameter inti LLM untuk mengontrol perilaku AI:
  - `system message`: Memberikan "persona" atau instruksi latar belakang kepada AI (misalnya: gaya bahasa Jaksel).
  - `temperature`: Mengontrol tingkat kreativitas/keacakan jawaban (0.0 untuk faktual/kaku, 0.8+ untuk lebih luwes/kreatif).
  - `max_tokens`: Membatasi panjang teks *output* untuk menghemat sumber daya.

## 🛠️ Teknologi yang Digunakan

- **Python 3.x**
- **Library `openai`** (>= 1.0.0)
- **Library `python-dotenv`**
- **Groq Cloud API** (Model: `llama-3.1-8b-instant`)

## 🚀 Cara Menjalankan Secara Lokal

1. **Clone repositori ini:**
   ```bash
   git clone https://github.com/dimasferial05-ctrl/openai-python-project.git
   cd openai-python-project
