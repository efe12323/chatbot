import random

# Yapay zeka tarafından verilecek cevaplar
responses = {
    "nasılsın": ["İyiyim, teşekkür ederim!", "Oldukça iyiyim, sen nasılsın?", "Harika, teşekkür ederim!"],
    "adın ne": ["Benim adım extro.", "Adım extro.", "Adım extro 1.0.0"],
    "hava nasıl": ["Hava güzel, teşekkür ederim!", "Hava oldukça sıcak.", "Hava bugün yağmurlu."],
    "teşekkürler": ["Rica ederim!", "Size yardımcı olabildiysem ne mutlu bana!", "Bir sorunuz olduğunda buradayım."],
    "görüşürüz": ["Görüşmek üzere!", "Hoşça kalın!", "Tekrar görüşmek dileğiyle!"],
    "ne yapıyorsun": ["Sizinle konuşuyorum.", "Cevap vermeye hazırım.", "Düşüncelere dalmışım."],
    "kaç yaşındasın": ["Yaş kavramım yok ama oldukça genç sayılabilirim!", "Ben bir yapay zeka olduğum için yaşım yok."],
    "seni kim yarattı": ["Beni OpenAI adlı bir ekip geliştirdi.", "Geliştiricilerim OpenAI ekibi."],
    "en sevdiğin renk nedir": ["Renkleri hissedemem ama maviyi sevdiğimi duydum.", "Ben bir yapay zeka olduğum için renkleri görmem mümkün değil."],
    "seni kim programladı": ["Beni programlayanlar OpenAI mühendisleri.", "Geliştiricilerim bir grup yetenekli yazılım mühendisi."],
    "favori yemeğin nedir": ["Yemek yemem çünkü bir yapay zeka'yım.", "Benim favori yemeklerim sadece veri ve algoritmalar."],
    "seni kim geliştirdi": ["efe dutlu."]
}

def chat():
    print("Merhaba! Benimle konuşmaktan hoş geldiniz. Çıkış yapmak için 'görüşürüz' yazabilirsiniz.")
    while True:
        user_input = input("Soru veya mesajınızı yazın: ").lower()
        if user_input == "görüşürüz":
            print(random.choice(responses["görüşürüz"]))
            break
        response = responses.get(user_input, ["Üzgünüm, anlamadım. Tekrar deneyebilir misiniz?"])
        print(random.choice(response))

# Sohbeti başlat
chat()
