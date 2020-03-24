"""Kullanıcıdan aldığınız bir sayının "Armstrong" olup olmadığını bulmaya çalışın.

Örnek olarak, Bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan herbirinin
4. kuvvetinin toplamı( 3 basamaklı sayılar için 3.kuvveti )
o sayıya eşitse bu sayıya "Armstrong" sayısı denir.

Örnek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4"""

"""
a = 1
b = 6
c = 3
d = 4
toplam = ((a**4)+(b**4)+(c**4)+(d**4))
print(toplam)"""

"""sayı = int(input("Sayıyı giriniz = "))
basamak = int(input("Basamak değerini giriniz = "))
sayı = 0
basamak = 0

toplam = 0
i = sayı

for x in range(0, basamak+1):
    rakam = i % 10
    toplam += rakam ** basamak
    i // 10

if (sayı == toplam):
    print("Bu bir ARMSTRONG sayısıdır.")
else:
    print("Bu bir ARMSTRONG sayısı değildir.")"""
# Python Armstrong Sayısı Bulma - Başka Bir Kod

sayi = int(input("Sayıyı Giriniz:"))
basamak = str(sayi)

toplam = 0

for x in basamak:
    rakam = int(x) ** len(basamak)
    toplam += rakam

if (sayi == toplam):
    print("Bu Bir Armstrong Sayısıdır.")
else:
    print("Armstong Sayısı Degildir.")

