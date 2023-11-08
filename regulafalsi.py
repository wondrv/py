# Definisi fungsi matematika yang akan dicari akarnya
def f(x):
    return x**2 - 6*x + 5

# Fungsi Regula Falsi untuk mencari akar
def false_position(a, b, tol, max_iterations):
    iteration = 0
    results = []

    while iteration < max_iterations:
        # Menghitung titik tengah c
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        f_c = f(c)
        results.append((iteration + 1, a, b, c, f(a), f(b), f_c))

        # Kondisi berhenti jika f(c) mendekati 0 atau selisih antara b dan a kurang dari toleransi
        if f_c == 0 or (b - a) < tol:
            break
        # Memperbarui batas a atau b berdasarkan tanda f(c)
        elif f_c * f(a) < 0:
            b = c
        else:
            a = c

        iteration += 1

    return c, results

# Inisialisasi batas awal, toleransi, dan jumlah maksimum iterasi
a = 3.0
b = 6.0
tolerance = 0.001  # Toleransi hingga 3 angka desimal
max_iterations = 7  # Jumlah maksimum iterasi

# Memanggil fungsi false_position untuk mencari akar
root, table = false_position(a, b, tolerance, max_iterations)

# Mencetak header tabel
print("| Iteration |   a   |   b   |   c   |  f(a)  |  f(b) |  f(c)  |")
print("|-----------|-------|-------|-------|--------|-------|--------|")

# Mencetak baris-baris tabel hasil iterasi
for row in table:
    print("|     {}     | {:.3f} | {:.3f} | {:.3f} | {:.3f} | {:.3f} | {:.3f} |".format(*row))

# Mencetak akar yang ditemukan setelah iterasi selesai
print("\nRoot of the equation: {:.3f}".format(root))

#| Iteration |   a   |   b   |   c   |  f(a)  |  f(b) |  f(c)  |
#|-----------|-------|-------|-------|--------|-------|--------|
#|     1     | 3.000 | 6.000 | 4.333 | -4.000 | 5.000 | -2.222 |
#|     2     | 4.333 | 6.000 | 4.846 | -2.222 | 5.000 | -0.592 |
#|     3     | 4.846 | 6.000 | 4.968 | -0.592 | 5.000 | -0.126 |
#|     4     | 4.968 | 6.000 | 4.994 | -0.126 | 5.000 | -0.026 |
#|     5     | 4.994 | 6.000 | 4.999 | -0.026 | 5.000 | -0.005 |
#|     6     | 4.999 | 6.000 | 5.000 | -0.005 | 5.000 | -0.001 |
#|     7     | 5.000 | 6.000 | 5.000 | -0.001 | 5.000 | -0.000 |

#Root of the equation: 5.000



