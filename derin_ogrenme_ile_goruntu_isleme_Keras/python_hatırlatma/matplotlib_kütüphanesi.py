import matplotlib.pyplot as plt 
import numpy as np 

x = np.array([1,2,3,4])
y = np.array([4,3,2,1])

plt.figure()
plt.plot(x,y,color="red",alpha = 0.3,label = "line")
plt.legend() #label yazması için legend kullanıyoruz

#noktalar kullnıyoruz
plt.scatter(x,y,color = "blue",alpha=0.7, label = "scatter")
plt.legend()

plt.title("matplotlib")

#çizgi ekler
plt.grid()

#bölülere ayırır
plt.xticks([0,1,2,3,4,5])


#-----------------------#
fig,axes = plt.subplots(2,1, figsize= (9,7))
fig.subplots_adjust(hspace=0.5)

x = [1,2,3,4,5,6,7,8,9,10]
y = [10,9,8,7,6,5,4,3,2,1]

axes[0].scatter(x,y)
axes[0].set_title("sub1")
axes[0].set_ylabel("sub1-y")
axes[0].set_xlabel("sub1-x")

axes[0].scatter(y,x)
axes[0].set_title("sub2")
axes[0].set_ylabel("sub2-y")
axes[0].set_xlabel("sub2-x")




plt.show()