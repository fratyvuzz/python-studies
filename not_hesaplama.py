"""
Kullanıcının girdiği vize1,vize2,final notlarına notlarına göre harf notunu hesaplayın.

    Vize1 toplam notun %30'una etki edecek.

    Vize2 toplam notun %30'una etki edecek.

    Final toplam notun %40'ına etki edecek.
"""

vize1 = int(input("Vize1'i giriniz = "))
vize2 = int(input("Vize2'i giriniz = "))
final = int(input("Finali giriniz = "))

ortalama = ((vize1*(30/100))+(vize2*(30/100))+(final*(40/100)))
print(ortalama)

if ortalama > 90:
    print("AA")
elif ortalama >= 85:
    print("BA")
elif ortalama >= 80:
    print("BB")
elif ortalama >= 75:
    print("CB")
elif ortalama >= 70:
    print("CC")
elif ortalama >= 65:
    print("DC")
elif ortalama >= 60:
    print("DD")
elif ortalama >= 55:
    print("FD")
else:
    print("FF")
