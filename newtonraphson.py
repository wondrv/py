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
