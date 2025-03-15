# Import library yang dibutuhkan
import cv2
import numpy as np
import matplotlib.pyplot as plt
from google.colab import files
from skimage import color

# Upload gambar
uploaded = files.upload()
image_path = list(uploaded.keys())[0]
img = cv2.imread(image_path)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Fungsi untuk menampilkan gambar
def display_images(images, titles):
    plt.figure(figsize=(15, 10))
    for i, (img, title) in enumerate(zip(images, titles)):
        plt.subplot(2, 3, i+1)
        plt.imshow(img, cmap='gray' if len(img.shape) == 2 else None)
        plt.title(title)
        plt.axis('off')
    plt.show()

# 1. Citra Negatif
def negative_image(img):
    return 255 - img

# 2. Transformasi Log
def log_transform(img):
    c = 255 / np.log(1 + np.max(img))
    log_image = c * (np.log(img + 1))
    return np.array(log_image, dtype=np.uint8)

# 3. Transformasi Power Law (Gamma)
def power_law_transform(img, gamma=0.5):
    c = 255 / (np.max(img) ** gamma)
    power_image = c * (img ** gamma)
    return np.array(power_image, dtype=np.uint8)

# 4. Histogram Equalization
def histogram_equalization(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    return cv2.equalizeHist(img_gray)

# 5. Histogram Normalization
def histogram_normalization(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    norm_img = cv2.normalize(img_gray, None, 0, 255, cv2.NORM_MINMAX)
    return norm_img

# 6. Konversi RGB ke HSI
def rgb_to_hsi(img):
    hsi = color.rgb2hsv(img)
    h, s, i = cv2.split(hsi)
    h = h * 360  # Konversi Hue ke derajat (0-360)
    s = s * 255  # Skala Saturation ke 0-255
    i = i * 255  # Skala Intensity ke 0-255
    return h, s, i

# Proses semua transformasi
neg_img = negative_image(img_rgb)
log_img = log_transform(img_rgb)
power_img = power_law_transform(img_rgb)
hist_eq_img = histogram_equalization(img_rgb)
hist_norm_img = histogram_normalization(img_rgb)
h, s, i = rgb_to_hsi(img_rgb)

# Tampilkan hasil
images = [img_rgb, neg_img, log_img, power_img, hist_eq_img, hist_norm_img]
titles = ['Original', 'Negative', 'Log Transform', 'Power Law', 
          'Histogram Equalization', 'Histogram Normalization']
display_images(images, titles)

# Tampilkan HSI secara terpisah
plt.figure(figsize=(15, 5))
plt.subplot(131); plt.imshow(h, cmap='hsv'); plt.title('Hue'); plt.axis('off')
plt.subplot(132); plt.imshow(s, cmap='gray'); plt.title('Saturation'); plt.axis('off')
plt.subplot(133); plt.imshow(i, cmap='gray'); plt.title('Intensity'); plt.axis('off')
plt.show()