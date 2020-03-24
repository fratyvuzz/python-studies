"""Mehmet manava gidiyor. Manavda sadece muz, elma ve üzüm var.
Manav, Mehmet’e hangi meyveden istediğini sorar.
Mehmet eğer muz isterse; manav kaç kilo istediğini sorar ve
kilosu 5tl olarak ödeyeceği ücreti hesaplayarak Mehmet’e söyler.
Mehmet eğer elma isterse; manav hangi renk elma istediğini sorar ve
 Mehmet kırmızı, sarı veya yeşil elma istediğini söyler.
 Manav kaç kilo istediğini sorar ve kilosu 2tl olarak
 ödeyeceği ücreti hesaplayıp Mehmet’e söyler.
Mehmet eğer üzüm isterse; mor veya yeşil olan üzümü seçer ve
mor üzüm için kilosu 3tl olarak ücret öder. Eğer yeşil üzüm seçerse,
 kilosuna 3.5tl ödeyecektir. Manav istediği üzümü sorar
 ve kaç kilo istiyorsa hesaplayıp ücreti söyler.
Mehmet’in manav alışverişinin kodları nasıl olmalıdır?"""

meyve = input("Hangi meyveyi istiyorsunuz?")

if meyve == ("muz"):
    kilo = int(input("Kaç kilo istiyorsunuz"))
    print(kilo*5,"tl ücret vericeksiniz")

elif meyve == ("elma"):
    renk = input("Hangi renk elma istiyorsunuz.")
    if renk == ("kırmızı"):
        kilo = int(input("Kaç kilo kırmızı elma istiyorsunuz"))
    elif renk ==  ("sarı"):
        kilo = int(input("Kaç kilo sarı elma istiyorsunuz"))
    elif renk == ("yeşil"):
        kilo = int(input("Kaç kilo yeşil elma istiyorsunuz"))
    else:
        print("Sadece kırmızı, sarı ve yeşil renkte elma var")

    print(kilo*2,"tl ücret vericeksiniz")

elif meyve == ("üzüm"):
    renk = input("Hangi renk üzüm istiyorsunuz.")
    if renk == ("mor"):
        kilo = int(input("Kaç kilo mor üzüm istiyorsunuz."))
        print(kilo*3,"tl vericeksiniz.")
    elif renk == ("yeşil"):
        kilo = int(input("Kaç kilo yeşil üzüm istiyorsunuz"))
        print(kilo*3,"tl vericeksiniz.")
    else:
        print("Sadece mor ve yeşil üzüm var.")

else:
    print("Manavda sadece muz elma ve üzüm vardır.")