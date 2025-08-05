# fibonacci.py

# Kullanıcıdan kaç adet Fibonacci sayısı istediğini al
n = int(input("Kaç adet Fibonacci sayısı istiyorsunuz? "))

# İlk iki Fibonacci sayısı
fibonacci = [0, 1]

# Fibonacci serisini oluştur
for i in range(2, n):
    yeni_sayi = fibonacci[i-1] + fibonacci[i-2]
    fibonacci.append(yeni_sayi)

# Fibonacci sayıları
print("Fibonacci Serisi:", fibonacci[:n])

# Ekstra: Fibonacci sayıların toplamı
toplam = sum(fibonacci[:n])
print("Toplam:", toplam)
