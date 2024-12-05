import cv2
import numpy as np
from google.colab.patches import cv2_imshow

def detect_shapes(image_path):
    # Baca gambar
    img = cv2.imread(image_path)
    if img is None:
        print("Gambar tidak ditemukan atau path salah.")
        return

    # Ubah gambar ke skala abu-abu
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Blur gambar untuk mengurangi noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Thresholding untuk mendapatkan gambar biner
    _, thresh = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY)

    # Deteksi kontur pada gambar
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Iterasi setiap kontur
    for contour in contours:
        # Approximate kontur menjadi poligon
        epsilon = 0.04 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        # Tentukan koordinat bounding box
        x, y, w, h = cv2.boundingRect(approx)

        # Deteksi bentuk berdasarkan jumlah sisi poligon
        if len(approx) == 3:
            shape = "Segitiga"
        elif len(approx) == 4:
            # Periksa apakah bentuk adalah persegi panjang atau persegi
            aspect_ratio = float(w) / h
            shape = "Persegi" if 0.95 <= aspect_ratio <= 1.05 else "Persegi Panjang"
        elif len(approx) > 4:
            shape = "Lingkaran"
        else:
            shape = "Tidak dikenal"

        # Gambar kontur dan nama bentuk pada gambar
        cv2.drawContours(img, [approx], -1, (0, 255, 0), 2)
        cv2.putText(img, shape, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

        # Tampilkan informasi bentuk yang terdeteksi
        print(f"Bentuk terdeteksi: {shape} pada koordinat x:{x}, y:{y}")

    # Tampilkan hasil
    cv2_imshow(img)

# Ubah 'image.jpg' dengan path gambar Anda
detect_shapes("image.jpg")
