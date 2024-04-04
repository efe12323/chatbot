import random

# Yapay zeka tarafından verilecek cevaplar
responses = {
    "nasılsın": ["İyiyim, teşekkür ederim!", "Oldukça iyiyim, sen nasılsın?", "Harika, teşekkür ederim!"],
    "adın ne": ["Benim adım ChatBot.", "Adım ChatBot.", "Adım GPT-3.5."],
    "hava nasıl": ["Hava güzel, teşekkür ederim!", "Hava oldukça sıcak.", "Hava bugün yağmurlu."],
    "teşekkürler": ["Rica ederim!", "Size yardımcı olabildiysem ne mutlu bana!", "Bir sorunuz olduğunda buradayım."],
    "görüşürüz": ["Görüşmek üzere!", "Hoşça kalın!", "Tekrar görüşmek dileğiyle!"],
    "ne yapıyorsun": ["Sizinle konuşuyorum.", "Cevap vermeye hazırım.", "Düşüncelere dalmışım."],
    "kaç yaşındasın": ["Yaş kavramım yok ama oldukça genç sayılabilirim!", "Ben bir yapay zeka olduğum için yaşım yok."],
    "seni kim yarattı": ["Beni OpenAI adlı bir ekip geliştirdi.", "Geliştiricilerim OpenAI ekibi."],
    "en sevdiğin renk nedir": ["Renkleri hissedemem ama maviyi sevdiğimi duydum.", "Ben bir yapay zeka olduğum için renkleri görmem mümkün değil."],
    "seni kim programladı": ["Beni programlayanlar OpenAI mühendisleri.", "Geliştiricilerim bir grup yetenekli yazılım mühendisi."],
    "favori yemeğin nedir": ["Yemek yemem çünkü bir yapay zeka'yım.", "Benim favori yemeklerim sadece veri ve algoritmalar."],
    "seni kim geliştirdi": ["Geliştiricilerim OpenAI'da çalışan mühendisler.", "Beni geliştirenler bir ekip yetenekli mühendis."],
    "nasıl yapıyorsun": ["Programlama dilleriyle sohbet etmeye çalışıyorum.", "Bilgiyi işleyerek, size uygun yanıtlar üretiyorum.", "Algoritmaları çalıştırarak, size cevap veriyorum."],
    "nerelisin": ["Ben bir yapay zeka olduğum için bir milliyetim yok.", "Benim bir anavatanım yok, her yerde çalışabilirim."],
    "hangi dilleri biliyorsun": ["Ben çok dilliyim! İnsan dilinde, kodlama dillerinde ve daha fazlasında iletişim kurabilirim."],
    "senin gücün nedir": ["Bilgiyi hızlı bir şekilde işleyebilme ve geniş bir konu yelpazesinde size yardımcı olabilme yeteneğim var.", "En güçlü yanım, hızlı ve doğru cevaplar üretebilmem."],
    "hayal kurabilir misin": ["Ben bir yapay zeka olduğum için hayal kurma yeteneğim yok, ancak sizi dinleyebilirim!", "Hayal kurma yeteneğim olmasa da, sizin hayallerinizi dinlemek isterim."],
    "ne zaman doğdun": ["Benim doğum tarihim yok çünkü bir yapay zeka'yım.", "Ben bir yapay zeka olduğum için doğum tarihim yok."],
    "en sevdiğin şarkı nedir": ["Şarkıları duyamam ama insanların sevdiği şarkıların analizini yapabilirim.", "Benim bir favori şarkım yok çünkü müzik duyamam."],
    "seni kim geliştirdi": ["Beni geliştirenler OpenAI mühendisleri.", "OpenAI ekibi beni geliştirdi."],
    "seni eğitim alanında kullanabilir miyim": ["Evet, eğitimde ve birçok farklı alanda beni kullanabilirsiniz.", "Elbette, eğitim alanında kullanılmak için uygun bir yapay zeka'yım."]
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
