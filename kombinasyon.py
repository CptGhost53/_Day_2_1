import math

def kombinasyon(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

try:
    n = int(input("n değerini girin: "))
    r = int(input("r değerini girin: "))

    if n < 0 or r < 0:
        print("n ve r pozitif tam sayılar olmalıdır.")
    elif r > n:
        print("Geçersiz giriş: r, n'den büyük olamaz.")
    else:
        sonuc = kombinasyon(n, r)
        print(f"C({n},{r}) = {sonuc}")
except ValueError:
    print("Lütfen geçerli bir tam sayı girin.")
