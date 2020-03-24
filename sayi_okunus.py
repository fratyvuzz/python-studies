# Kullanıcıdan 2 basamaklı bir sayı alın ve bu sayının okunuşunu yazınız
# örn= 97 ---> Doksan yedi


birler = ["","Bir","İki","Üç","Dört","Beş","Altı","Yedi","Sekiz","Dokuz"]
onlar = ["","On","Yirmi","Otuz","Kırk","Elli","Altmış","Yetmiş","Seksen","Doksan"]

def okunus(sayı):
    birinci = sayı % 10
    ikinci = sayı // 10

    return onlar[ikinci] + " " + birler[birinci]

sayı = int(input("Sayı:"))

print(okunus(sayı))

