list = [1,2,3,4,5,6,7]

print(type(list))

hafta = ["pazartesi","salı","çarşamba"]

#ilk eleman
print(hafta[1])

#liste uzunluğu
print(len(hafta))

#son elemanı
print(hafta[-1])

#1-4 elemanları yazdırma  //4 dahil değil
print(hafta[1:4])

#listeye eleman eklenme 
list.append(7)
print(list)

#listeyi ters çevirme 
list.reverse

#listeden eleman çıkarma
list.remove

#listeyi sıralama
sayilar = [1,5,2,9,7]
sayilar.sort()