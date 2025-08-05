def asal_mi(sayi):
    if sayi < 2:
        return False
    for i in range(2, int(sayi**0.5) + 1):
        if sayi % i == 0:
            return False
    return True

# Kullanıcıdan sayı al
try:
    n = int(input("Bir sayı girin: "))
    if n < 1:
        print("Lütfen 1 veya daha büyük bir sayı girin.")
    else:
        print(f"1 ile {n} arasındaki asal sayılar:")
        for i in range(1, n + 1):
            if asal_mi(i):
                print(i, end=" ")
        print()  # Yeni satır
        # Girilen sayının asal olup olmadığını belirt
        if asal_mi(n):
            print(f"{n} bir asal sayıdır.")
        else:
            print(f"{n} bir asal sayı değildir.")
except ValueError:
    print("Lütfen geçerli bir tam sayı girin.")
