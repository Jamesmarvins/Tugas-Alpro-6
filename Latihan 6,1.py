def is_prime(num):
    if num < 2:
        return False
    return all(num % i != 0 for i in range(2, num))

def cari_prima_terdekat_dibawah_n(n):
    return next((i for i in range(n - 1, 1, -1) if is_prime(i)), None)

n = int(input("Masukkan bilangan n: "))
prima_dekat = cari_prima_terdekat_dibawah_n(n)
if prima_dekat:
    print(f"Bilangan prima terdekat yang lebih kecil dari {n} adalah {prima_dekat}")
else:
    print(f"Tidak ada bilangan prima terdekat yang lebih kecil dari {n}")