import cv2
import numpy as np
import matplotlib.pyplot as plt
import urllib.request

# URL gambar
url = 'https://2.bp.blogspot.com/-3cbXaJoGm50/UsfFu_kyeAI/AAAAAAAAAIA/LwU8hgWBtBE/s1600/little-cute-cat.jpg'

# Unduh gambar dari URL
urllib.request.urlretrieve(url, 'input_image.jpg')

# Baca gambar yang sudah diunduh
img = cv2.imread('input_image.jpg')

# Cek apakah gambar berhasil dibaca
if img is None:
    print("Error: Gambar tidak ditemukan atau gagal dibaca.")
else:
    # Fungsi untuk melakukan histogram equalization
    def histogram_equalization(img):
        # Konversi gambar ke skala abu-abu jika berwarna
        if len(img.shape) == 3:
            img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        else:
            img_gray = img

        # Histogram equalization
        img_equalized = cv2.equalizeHist(img_gray)

        return img_gray, img_equalized

    # Lakukan histogram equalization
    img_gray, img_equalized = histogram_equalization(img)

    # Tampilkan hasil
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.title('Original Grayscale Image')
    plt.imshow(img_gray, cmap='gray')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.title('Histogram Equalized Image')
    plt.imshow(img_equalized, cmap='gray')
    plt.axis('off')

    plt.show()

    # Simpan hasil gambar
    cv2.imwrite('equalized_image.jpg', img_equalized)
