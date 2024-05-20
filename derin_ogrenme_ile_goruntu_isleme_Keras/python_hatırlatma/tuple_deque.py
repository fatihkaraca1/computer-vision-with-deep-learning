#değiştirilmez ve sıralı bir veri türüdür

tuple_veritipi = (1,2,3,4,5,6)

print(tuple_veritipi[0])

#2.indexten sonraki elemanları yazdır
print(tuple_veritipi[2:])

################## DEQUE kuyruk ##############

from collections import deque

dq = deque(maxlen = 3)

#kuyruğun sonuna 1 ekledik
dq.append(1)
# ''       ''     2  ''
dq.append(2)

#soldan ekleme
dq.appendleft(5)

#kuyruğun içini boşaltma
dq.clear() 