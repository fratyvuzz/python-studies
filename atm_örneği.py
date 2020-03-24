print("********************\nATM sistemine hoşgeldiniz\n********************")

print("""
İşlemler:

1. Bakiye Sorgulama
2. Para Yatırma
3. Para Çekme
4. Kredi Ödeme

Programdan 'q' tuşu ile çıkabilirsiniz.

""")

bakiye = 1000

while True:
    işlem = input("İşlemi seçiniz")

    if (işlem == "q"):
        print("Yine bekleriz")
        break
    elif (işlem=="1"):
        print("Bakiyeniz {} tl'dir.".format(bakiye))

    elif (işlem=="2"):
        miktar = int(input("Miktarını giriniz.."))
        bakiye += miktar

    elif (işlem=="3"):
        miktar = int(input("Miktarı giriniz.."))
        if (bakiye-miktar<0):
            print("Böyle bir miktar çekemezsiniz.")
            continue
        bakiye-=miktar
    elif (işlem=="4"):
        kredi_borcu_ödeme = int(input("Miktarını giriniz.."))
        bakiye += kredi_borcu_ödeme

    else:
        print("Geçersiz işlem...")
