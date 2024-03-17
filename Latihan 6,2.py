def faktorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

n = int(input("Masukkan nilai n: "))
for i in range(n, 0, -1):
    print(faktorial(i), end=" ")
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()