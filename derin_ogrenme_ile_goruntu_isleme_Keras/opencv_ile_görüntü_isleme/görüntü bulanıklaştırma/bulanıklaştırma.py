import cv2
import matplotlib.pyplot as plt
import numpy as np

import warnings
warnings.filterwarnings("ignore")


img  = cv2.imread("opencv_ile_görüntü_işleme\\bisiklet.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure(), plt.imshow(img), plt.axis("off"), plt.title("orjinal"), plt.show()

#ortalma bulanıklaştırma yöntemi

dst2 = cv2.blur(img, ksize= (3,3))
plt.figure(),plt.imshow(dst2),plt.axis(), plt.title("ortalama blur")


# guassian blur

gb =  cv2.GaussianBlur(img, ksize=(3,3), sigmaX=7)
plt.figure(), plt.imshow(gb), plt.axis("off"), plt.title("gauss blur")

#medyan blur

mb =  cv2.medianBlur(img, ksize=(3,3), sigmaX=7)
plt.figure(), plt.imshow(gb), plt.axis("off"), plt.title("median blur")

def gausianNoise(image):
    row,col,ch = image.shape
    mean = 0
    var = 0.05
    sigma =  var** 0.5

    gauss = np.random.normal(mean, sigma, (row,col,ch))
    gauss = gauss.reshape(row,col,ch)
    noisy = image + gauss

    return noisy

#içe aktarmaları normalize et

img = cv2.imread("bisiklet.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)/255
plt.figure(), plt.imshow(img), plt.axis("off"), plt.title("orginal")

gausianNoisyimage = gausianNoise(img)
plt.figure(), plt.imshow(gausianNoisyimage), plt.axis("off"), plt.title("gauss noisy")

gb2 = cv2.GaussianBlur(gausianNoisyimage, ksize= (3,3), sigmaX=7)
plt.figure(), plt.imshow(gb2), plt.axis("off"), plt.title("with gauss blur")

def saltpepperNoise(image):
    row, col, ch = image.shape
    s_vs_p = 0.5

    amount = 0.004

    noisy  = np.copy(image)

    num_salt = np.ceil(amount + image.size * s_vs_p)
    coords = [np.random.randint(0, i-1, num_salt) for i in image.shape]
    noisy[coords] = 1

    num_pepper = np.ceil(amount + image.size *1- s_vs_p)
    coords = [np.random.randint(0, i-1, num_salt) for i in image.shape]
    noisy[coords] = 0

    return noisy

spImage = saltpepperNoise(img)
plt.figure(), plt.imshow(spImage), plt.axis("off"), plt.title("SP image")

mb2 = cv2.medianBlur(spImage.astype(np.float32), ksize=3)
plt.figure(), plt.imshow(mb2), plt.axis("off"), plt.title("with median blur")

