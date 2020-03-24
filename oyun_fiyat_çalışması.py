"""Efe STEAM hesabından oyun almak istiyor.
CS:GO için; 1. 2. ve 3. versiyonları bulunmaktadır.
1. ve 2. versiyonları 30tl, 3. versiyon ise 40tl dir.
Garrys Mod için; tek bir versiyon bulunmakta ve 15tl dir.
Euro Truck için; 1. ve 2. versiyonu bulunmakta ve iki versiyon da 20tl dir.
Buna göre Efe’nin seçtiği oyuna göre ödeyeceği
ücreti söyleyen kod bloğu nasıl olmalıdır?"""


oyun = input("Hangi oyunu istiyorsunuz.?")

if oyun == ("CS Go"):
    versiyon = int(input("Hangi cs go versiyonunu istiyorsunuz.?"))

    if (versiyon == 1 or versiyon == 2):
        print("CS go",versiyon,"versiyonunun ücreti 30 tl dir.")
    elif versiyon == 3:
        print("CS go",versiyon,"versiyonunun ücreti 40 tl dir.")
    else:
        print("Aradığınız versiyon bulunmamaktadır.")

elif oyun == ("Garrys Mood"):
    print("Garrys Mood oyununun ücreti 15 tl dir.")

elif oyun == ("Euro Track"):
    versiyon = int(input("Hangi euro track versiyonunu istiyorsunuz"))

    if (versiyon == 1 or versiyon == 2):
        print("Euro Track",versiyon,"versiyonunun ücreti 20 tl dir.")
    else:
        print("Aradığınız versiyon bulunmamaktadır.")