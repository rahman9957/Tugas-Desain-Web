import time
import sys

def teks_lirik():
    delay = [0.5] * 10  # durasi delay antar baris
    lirik = [
        "== Madaheen El Naby - Mostafa Atef ==",
        "صلوا على النبي صلوا عليه",
        "شفيع الأمة يوم الميعاد",
        "يا حبيب الله يا خير البرية",
        "نورك ساطع في كل البلاد",
        "مدحك شرف واللي يحبك يتشافى",
        "إنت الضياء ونورك كاسي الكوافة",
        "أنا قلبي حبك واتباهى بيك",
        "وكل ما أقول اسمك قلبي يطيب",
        "يا محمد يا رسول الله"
    ]

    for i, baris in enumerate(lirik):
        for karakter in baris:
            print(karakter, end='')
            sys.stdout.flush()
            time.sleep(0.05)  # delay antar huruf
        print()
        time.sleep(delay[i % len(delay)])

    print("=== coba === by intor.id === (Ibrahim Setiawan) ===")

teks_lirik()