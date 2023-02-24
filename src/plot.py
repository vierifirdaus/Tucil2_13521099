import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def plot3d(arr,i,j) :
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

def plot2d(arr,i,j) :
    xs=[]
    ys=[]
    for ii in range(len(arr)) :
        xs.append(arr[ii][0])
        ys.append(arr[ii][1])
    plt.scatter(xs,ys)
    plt.scatter([arr[i][0],arr[j][0]],[arr[i][1],arr[j][1]],c='red',s=30)
    plt.plot([arr[i][0],arr[j][0]],[arr[i][1],arr[j][1]],color='red')
    plt.show()
