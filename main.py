import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

# KITA SETTING KEPRIBADIAN AI DI SINI (System Message)
# Coba ganti-ganti deskripsi ini nanti!
system_instruction = "Kamu adalah asisten AI yang selalu menjawab dengan gaya bahasa anak gaul Jaksel (pake lo-gue, literally, which is). Jawabanmu harus singkat."

print("🤖 Chatbot AI Gaul Aktif! (Ketik 'keluar' untuk berhenti)")
print("-" * 50)

while True:
    # Mengambil input teks dari kamu (user)
    user_input = input("\nKamu: ")
    
    # Jika kamu mengetik 'keluar', program berhenti
    if user_input.lower() == 'keluar':
        print("AI: Bye bye! See you later.")
        break

    # KITA SETTING PARAMETER DI SINI
    # Coba ubah angka ini dari 0.0 sampai 1.5 untuk melihat perbedaannya
    suhu_kreativitas = 1.8 

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        temperature=suhu_kreativitas, 
        max_tokens=100, # Membatasi jawaban maksimal sekitar ~75 kata
        messages=[
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": user_input}
        ]
    )

    pesan_balasan = response.choices[0].message.content
    print(f"AI (Temp: {suhu_kreativitas}):", pesan_balasan)