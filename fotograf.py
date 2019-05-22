import matplotlib.pyplot as plt
import numpy as np

file_name = "kus.jpg"
im_1 = plt.imread(file_name)

#print(im_1)
#print(type(im_1))
#print(im_1.shape) #rgb ise son deger 3 gelir

#print(im_1[0, 0, 0], im_1[0, 0, 1], im_1[0, 0, 2])#son taraf 3ten büyük olamaz
#print(im_1[0, 0, :])
import matplotlib.pyplot as plt
import numpy as np

file_name = "bird.jpg" #resmi aldik
im = plt.imread(file_name) #okuduk degiskene aldi

type(im)
print(im.shape) #boyutu
#her bir pikselde 3lu deger var
im[0,0,0] #ilk pikselin kirmizi degeri
im[0,0,1] #diger renk bilgisi
im[0,0,:] #hepsi
im[:,0,0] #ilk sutunun renk bilgisi

plt.imshow(im) #resmi gosterdik
plt.show()

#goruntu isleme
im=im+1 #liste olsaydi +1 hata olurdu resim oldugu icin degil
im[:,:,0]=im[:,:,0]+10 #kirmizi tonu arttir

im2=np.transpoze(im)#resmi 90 derece saat yonunde
im.shape

def my_rot(im_100):
    m = im_1.shape[0]
    n = im_1.shape[1]

    my_new_image = np.zeros((n, m, 3), dtype = int)#
    #im_1 = np.transpose(im_1) 5 birim döndürme
    for row in range(m):    
        for column in range(n):
            my_new_image[column, row, :] = im_100[row, column, :] #satirlari sutunla yer degistir
    return my_new_image

im_2 = my_rot(im_1)
print(plt.imshow(im_2))
print(plt.subplot(1, 2, 1))#1 e 2 lik yere yazdır
print(plt.imshow(im_1))
print(plt.subplot(1, 2, 2))
print(plt.imshow(im_2))

print(im_1[0, 0, :])#bu degerleri tek bir degiskene atabilir miyiz?
def my_norm(my_v):
    return int(((my_v[0]**2) + (my_v[1]**2) + (my_v[2]**2))**0.5) #a^2 + b^2 + c^2 kökünü aldık

print(my_norm(im_1[0, 0, :]))    


def my_convert_rgb_to_gray(im_100):
    m = im_1.shape[0]
    n = im_1.shape[1]

    my_new_image = np.zeros((m, n), dtype = int)
    #im_1 = np.transpose(im_1) 5 birim döndürme
    for row in range(m):    #her konum için
        for column in range(n):
            my_new_image[row, column] = my_norm(im_100[column, row, :])
    return my_new_image

im_3 = my_convert_rgb_to_gray(im_2)
print(plt.imshow(im_2))
print(plt.subplot(1, 3, 2))#1 e 2 lik yere yazdır
print(plt.imshow(im_2))
print(plt.subplot(1, 3, 3))
print(plt.imshow(im_3))

def my_norm_1(my_v):
    s = int(((my_v[0]**2) + (my_v[1]**2) + (my_v[2]**2))**0.5) #kökünü aldık
    if(s > 130):
        return 1
    else:
        return 0


def my_convert_rgb_to_bw(im_100):
    m = im_1.shape[0]
    n = im_1.shape[1]

    my_new_image = np.zeros((m, n), dtype = int)
    #im_1 = np.transpose(im_1) 5 birim döndürme
    for row in range(m):    #her konum için
        for column in range(n):
            my_new_image[row, column] = my_norm_1(im_100[column, row, :])
    return my_new_image

im_4 = my_convert_rgb_to_bw(im_2)
print(plt.imshow(im_2))
print(plt.subplot(1, 4, 2))
print(plt.imshow(im_2))
print(plt.subplot(1, 4, 3))
print(plt.imshow(im_3,cmap='gray'))
print(plt.subplot(1, 4, 4))
print(plt.imshow(im_4))
