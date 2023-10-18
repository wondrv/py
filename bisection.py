def f(x):
    return x**2 - 6*x + 5

def bisection(func, a, b, tol=0.001):
    if func(a) * func(b) >= 0:
        raise ValueError("Tidak ada perubahan tanda pada interval [a, b]. Bisection tidak berlaku.")

    while (b - a) / 2.0 > tol:
        c = (a + b) / 2.0
        if func(c) == 0.0:
            return c
        elif func(c) * func(a) < 0:
            b = c
        else:
            a = c

    akar = (a + b) / 2.0
    return round(akar, 3)  # Membulatkan hasil ke 3 angka di belakang koma

# Menjalankan bisection untuk mencari akar dalam interval [3, 6] dengan toleransi 0.001
akar = bisection(f, 3, 6, 0.001)
print("Akar persamaan: ", akar)
