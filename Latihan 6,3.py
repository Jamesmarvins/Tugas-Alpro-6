def display_series(T, L):
    start = 1
    for i in range(T):
        for j in range(L):
            print(start, end=" ")
            start += 1
        print()

T = int(input("Masukkan tinggi: "))
L = int(input("Masukkan lebar: "))
display_series(T, L)