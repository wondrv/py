import numpy as np

def newton_raphson(f, f_prime, x0):
  """
  Solusi persamaan non linier menggunakan metode Newton-Raphson

  Parameters
  ----------
  f : fungsi
  f_prime : turunan pertama fungsi
  x0 : titik awal

  Returns
  -------
  x : solusi persamaan
  """

  x = x0
  while True:
    f_x = f(x)
    f_prime_x = f_prime(x)
    x_new = x - f_x

"""
1. Persamaan Non Linier

Persamaan non linier yang diberikan adalah sebagai berikut:
3+x^{3}-x=4

Persamaan ini dapat diselesaikan dengan menggunakan metode Newton-Raphson. Metode Newton-Raphson adalah metode iteratif yang menggunakan pendekatan nilai fungsi di sekitar akar untuk menentukan nilai akar yang lebih akurat.

Langkah-langkah untuk menyelesaikan persamaan non linier menggunakan metode Newton-Raphson adalah sebagai berikut:

1. Pilih titik awal x0.
2. Hitung nilai fungsi f(x0).
3. Hitung turunan pertama fungsi f'(x0).
4. Hitung nilai akar baru x1 menggunakan persamaan berikut:
x1 = x0 - f(x0) / f'(x0)
5. Ulangi langkah 2-4 hingga nilai x konvergen.

Dalam kasus ini, kita dapat memilih titik awal x0 = 1. Nilai fungsi f(x0) = 2 dan nilai turunan pertama f'(x0) = 3x2 - 1.

Berikut adalah tabel iterasi penyelesaian persamaan non linier menggunakan metode Newton-Raphson:
Iterasi	x	      f(x)	       f'(x)	         x1
0	   | 1	            |   2	     |  3	    |   -0.1667
1	   | -0.1667   |	0.6667  |	2.25	    |    0.0833
2	   | 0.0833    |	0.0278  |	0.0282 |	0.0833


1. Persamaan Non Linier

Persamaan non linier yang diberikan adalah sebagai berikut:

3+x^{3}-x=4
Persamaan ini dapat diselesaikan dengan menggunakan metode Newton-Raphson. Metode Newton-Raphson adalah metode iteratif yang menggunakan pendekatan nilai fungsi di sekitar akar untuk menentukan nilai akar yang lebih akurat.

Langkah-langkah untuk menyelesaikan persamaan non linier menggunakan metode Newton-Raphson adalah sebagai berikut:

Pilih titik awal x0.
Hitung nilai fungsi f(x0).
Hitung turunan pertama fungsi f'(x0).
Hitung nilai akar baru x1 menggunakan persamaan berikut:
x1 = x0 - f(x0) / f'(x0)
Ulangi langkah 2-4 hingga nilai x konvergen.
Dalam kasus ini, kita dapat memilih titik awal x0 = 1. Nilai fungsi f(x0) = 2 dan nilai turunan pertama f'(x0) = 3x2 - 1.

Berikut adalah tabel iterasi penyelesaian persamaan non linier menggunakan metode Newton-Raphson:

Iterasi	x	f(x)	f'(x)	x1
0	1	2	3	-0.1667
1	-0.1667	0.6667	2.25	0.0833
2	0.0833	0.0278	0.0282	0.0833
Berdasarkan tabel iterasi, dapat dilihat bahwa nilai x konvergen ke nilai x = 0.0833.

2. Persamaan Linier

Persamaan linier yang diberikan adalah sebagai berikut:
2x-4=8

Persamaan ini dapat diselesaikan dengan menggunakan metode eliminasi Gauss. Metode eliminasi Gauss adalah metode yang menggunakan operasi baris untuk menghilangkan variabel-variabel dalam sistem persamaan linear.

Langkah-langkah untuk menyelesaikan persamaan linier menggunakan metode eliminasi Gauss adalah sebagai berikut:

1. Tulis sistem persamaan dalam bentuk matriks augmented.
2. Eliminasi variabel-variabel yang tidak diperlukan.
3. Selesaikan persamaan yang tersisa untuk variabel yang diinginkan.

Dalam kasus ini, sistem persamaan yang diberikan dapat ditulis dalam bentuk matriks augmented sebagai berikut:
| 2 | -4 | 8 |
| 0 | 1 | 2 |

Langkah pertama adalah menghilangkan variabel x dari persamaan pertama. Untuk melakukannya, kita dapat mengalikan baris pertama dengan 1/2.
| 1 | -2 | 4 |
| 0 | 1 | 2 |

Kemudian, kita dapat mengalikan baris kedua dengan -2 dan menambahkannya ke baris pertama.
| 1 | -2 | 4 |
| 0 | 0 | 0 |

Berdasarkan matriks augmented yang dihasilkan, dapat dilihat bahwa variabel x tidak ada di persamaan kedua. Oleh karena itu, variabel x memiliki nilai sembarang.

Untuk menentukan nilai x, kita dapat memasukkan nilai x ke persamaan pertama. Misalnya, jika kita menetapkan x = 1, maka kita akan mendapatkan:
2(1)-4=8
-2=8

Persamaan ini tidak memiliki solusi. Oleh karena itu, sistem persamaan ini memiliki solusi tak berhingga, dengan x sembarang.
"""
