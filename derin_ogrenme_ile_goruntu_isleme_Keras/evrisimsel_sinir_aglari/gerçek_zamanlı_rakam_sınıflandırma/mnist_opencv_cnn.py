import numpy as np
import cv2
import os 
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense, Conv2D, MaxPooling2D, Flatten, Dropout, BatchNormalization
from keras.utils import to_categorical
from keras.preprocessing.image import ImageDataGenerator


import pickle

# Veri seti yolunu tanımla
path = "myData"

# Veri setindeki sınıfları al
myList = os.listdir(path)
noOfClasses = len(myList)

print("Label(sınıf) sayısı: ", noOfClasses)

# Görüntüleri ve etiketleri depolamak için listeler oluştur
images = []
classNo = []

# Her sınıftaki görüntüleri oku ve listelere ekle
for i in range(noOfClasses):
    myImageList = os.listdir(os.path.join(path, str(i)))
    for j in myImageList:
        img = cv2.imread(os.path.join(path, str(i), j))
        img = cv2.resize(img, (32,32))
        images.append(img)
        classNo.append(i)
        
print(len(images))
print(len(classNo))

# Listeleri numpy dizilerine dönüştür
images = np.array(images)
classNo = np.array(classNo)

print(images.shape)
print(classNo.shape)

# Veriyi eğitim, test ve doğrulama kümelerine ayır
x_train, x_test, y_train, y_test = train_test_split(images, classNo, test_size = 0.5, random_state = 42)
x_train, x_validation, y_train, y_validation = train_test_split(x_train, y_train, test_size = 0.2, random_state = 42)

print(images.shape)
print(x_train.shape)
print(x_test.shape)
print(x_validation.shape)

# Görüntü ön işleme fonksiyonu tanımla
def preProcess(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Görüntüyü gri tonlamaya dönüştür
    img = cv2.equalizeHist(img)  # Histogram eşitleme
    img = img / 255  # Normalizasyon
    
    return img

# Eğitim, test ve doğrulama verilerini ön işlemden geçir
x_train = np.array(list(map(preProcess, x_train)))
x_test = np.array(list(map(preProcess, x_test)))
x_validation = np.array(list(map(preProcess, x_validation)))

# Giriş verilerinin boyutunu yeniden şekillendirme
x_train = x_train.reshape(-1,32,32,1)
print(x_train.shape)
x_test = x_test.reshape(-1,32,32,1)
x_validation = x_validation.reshape(-1,32,32,1)

# Veri artırma
dataGen = ImageDataGenerator(width_shift_range = 0.1,height_shift_range = 0.1,zoom_range = 0.1, rotation_range = 10)

dataGen.fit(x_train)

# Etiketleri kategorik hale getirme
y_train = to_categorical(y_train, noOfClasses)
y_test = to_categorical(y_test, noOfClasses)
y_validation = to_categorical(y_validation, noOfClasses)

# Model oluşturma
model = Sequential()
model.add(Conv2D(input_shape = (32,32,1), filters = 8, kernel_size = (5,5), activation = "relu", padding = "same"))
model.add(MaxPooling2D(pool_size = (2,2)))

model.add(Conv2D( filters = 16, kernel_size = (3,3), activation = "relu", padding = "same"))
model.add(MaxPooling2D(pool_size = (2,2)))

model.add(Dropout(0.2))
model.add(Flatten())
model.add(Dense(units=256, activation = "relu" ))
model.add(Dropout(0.2))
model.add(Dense(units=noOfClasses, activation = "softmax" ))

# Modeli derleme
model.compile(loss = "categorical_crossentropy", optimizer="Adam", metrics = ["accuracy"])

# Eğitim parametreleri
batch_size = 250

# Modeli eğit
hist = model.fit(dataGen.flow(x_train, y_train, batch_size = batch_size), validation_data = (x_validation, y_validation),epochs = 15, steps_per_epoch = len(x_train)//batch_size, shuffle = 1)

# Modeli kaydet
with open("model_trained_new.p","wb") as pickle_out:
    pickle.dump(model, pickle_out)

# Eğitim geçmişini görselleştirme
plt.figure()
plt.plot(hist.history["loss"], label = "Eğitim Loss")
plt.plot(hist.history["val_loss"], label = "Val Loss")
plt.legend()
plt.show()

plt.figure()
plt.plot(hist.history["accuracy"], label = "Eğitim accuracy")
plt.plot(hist.history["val_accuracy"], label = "Val accuracy")
plt.legend()
plt.show()

# Test seti üzerinde modelin performansını değerlendirme
score = model.evaluate(x_test, y_test, verbose = 1)
print("Test loss: ", score[0])
print("Test accuracy: ", score[1])

# Doğrulama seti üzerinde modelin tahminlerini yapma ve karışıklık matrisi oluşturma
y_pred = model.predict(x_validation)
y_pred_class = np.argmax(y_pred, axis = 1)
Y_true = np.argmax(y_validation, axis = 1)
cm = confusion_matrix(Y_true, y_pred_class)

# Karışıklık matrisini görselleştirme
f, ax = plt.subplots(figsize=(8,8))
sns.heatmap(cm, annot = True, linewidths = 0.01, cmap = "Greens", linecolor = "gray", fmt = ".1f", ax=ax)
plt.xlabel("predicted")
plt.ylabel("true")
plt.title("cm")
plt.show()
