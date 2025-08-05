# hesap_makinesi.py

def hesapla(sayi1, sayi2, islem):
    if islem == '+':
        return sayi1 + sayi2
    elif islem == '-':
        return sayi1 - sayi2
    elif islem == '*':
        return sayi1 * sayi2
    elif islem == '/':
        if sayi2 == 0:
            return "Hata: Sıfıra bölünemez!"
        return sayi1 / sayi2
    else:
        return "Geçersiz işlem!"

print("Basit Hesap Makinesi")
print("İşlemler: +, -, *, /")
print("Çıkmak için 'q' yazın\n")

while True:
    islem = input("İşlem türü (+, -, *, / veya q): ")
    if islem.lower() == 'q':
        print("Hesap makinesi kapatılıyor...")
        break

    try:
        sayi1 = float(input("Birinci sayıyı girin: "))
        sayi2 = float(input("İkinci sayıyı girin: "))
        sonuc = hesapla(sayi1, sayi2, islem)
        print("Sonuç:", sonuc)
    except ValueError:
        print("Hata: Lütfen geçerli bir sayı girin.")
    
    print()  # Boş satır
