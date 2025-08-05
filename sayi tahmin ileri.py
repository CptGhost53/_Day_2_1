import random

# Rastgele sayı üret (1-100)
sayi = random.randint(1, 100)
max_deneme = 7
deneme_sayisi = 0

print("1 ile 100 arasında bir sayı tuttum.")
print(f"{max_deneme} tahmin hakkın var. Başlayalım!")

while deneme_sayisi < max_deneme:
    try:
        tahmin = int(input(f"{deneme_sayisi + 1}. tahminin: "))
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")
        continue

    deneme_sayisi += 1

    if tahmin < sayi:
        print("Daha büyük bir sayı dene.")
    elif tahmin > sayi:
        print("Daha küçük bir sayı dene.")
    else:
        print(f"Tebrikler! {deneme_sayisi}. denemede doğru tahmin ettin.")
        break
else:
    print(f"Maalesef bilemedin. Doğru cevap: {sayi}")
