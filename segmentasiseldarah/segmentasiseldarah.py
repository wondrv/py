# Membuat kode Python untuk segmentasi sel darah putih menggunakan operasi morfologi dan watershed
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load gambar
image = cv2.imread('data/contoh_citra.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Thresholding untuk mendapatkan objek foreground
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Operasi morfologi (noise removal)
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

# Sure background area
sure_bg = cv2.dilate(opening, kernel, iterations=3)

# Sure foreground area menggunakan distance transform
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
_, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)

# Marker labelling
_, markers = cv2.connectedComponents(sure_fg)
markers = markers + 1
markers[unknown == 255] = 0

# Watershed
markers = cv2.watershed(image, markers)
image[markers == -1] = [255, 0, 0]  # Tanda batas (merah)

# Tampilkan hasil
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Citra Asli')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Thresholding')
plt.imshow(thresh, cmap='gray')
plt.axis('off')
plt.tight_layout()
plt.show()


# Simpan sebagai file Python
code_path = "/mnt/data/segmentasi_sel_darah.py"
with open(code_path, "w") as f:
    f.write(code)
code_path
