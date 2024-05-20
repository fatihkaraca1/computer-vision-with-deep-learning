#şablon
#düzenleme
import numpy as np 


def dairealan(r):
    alan = (np.pi) * (r**2)

    return alan

değişken = dairealan(3)

print(değişken)


#lambda fonsiyonları
#ileri seviye fonksiyonlardır

def carpma(x,y,z):
    return x*y*z

sonuc = carpma(1,2,3)
print(sonuc)

#aynı işlem

fonksiyon_lambda = lambda x,y,z : x*y*z