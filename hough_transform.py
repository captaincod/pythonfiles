import matplotlib.pyplot as plt
import json

dA = int(input())
dB = int(input())

with open('image_hough.json', 'r') as f:
    image = json.load(f)
    hough_space = [[0] * len(image)] * len(image)
    for x1 in range(len(image) - 1):
        for y1 in range(len(image[x1]) - 1):
            x2 = image[x1 + 1]
            y2 = image[y1 + 1]

            a = (y1 - y2) / (x1 - x2)
            b = (-y1 * x2 + y2 * x1) / (x1 - x2)

            As = 0
            Bs = 0

            i = (a - As) / dA
            j = (b - Bs) / dB

            hough_space[i][j] += 1

plt.imshow(image)
plt.show()
