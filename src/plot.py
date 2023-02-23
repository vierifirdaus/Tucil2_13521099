import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
import numpy as np
# np.random.seed(10)

def plot(arr,i,j) :
    xs=[]
    ys=[]
    zs=[]
    for ii in range(len(arr)) :
        xs.append(arr[ii][0])
        ys.append(arr[ii][1])
        zs.append(arr[ii][2])
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(xs,ys,zs)

    ax.scatter([arr[i][0],arr[j][0]],[arr[i][1],arr[j][1]],[arr[i][2],arr[j][2]],c='red',s=30)
    ax.plot([arr[i][0],arr[j][0]],[arr[i][1],arr[j][1]],[arr[i][2],arr[j][2]],color='red')
    ax.set_xlabel("Sumbu X")
    ax.set_ylabel("Sumbu Y")
    ax.set_zlabel("Sumbu Z")
    plt.show()

#show
# plt.show()    

# xs = [1,2,3,4,5]
# ys = [1,2,3,4,5]
# zs = [1,2,3,4,5]

# fig = plt.figure()

# ax = fig.add_subplot(111, projection='3d')

# #semua titik
# ax.scatter(xs,ys,zs)

# #titik terdekat
# ax.scatter([1,2],[1,2],[1,2],c='red',s=50)
# ax.plot([1,2],[1,2],[1,2],color='black')

# #label sumbu
# ax.set_xlabel("Sumbu X")
# ax.set_ylabel("Sumbu Y")
# ax.set_zlabel("Sumbu Z")

# #show
# plt.show()