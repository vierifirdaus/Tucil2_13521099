import random
def swap(a,b) :
    return (b,a)

def distance(a,b) :
    res=0.0
    for i in range(len(a)) :
        res+=(a[i]-b[i])**2
    return res**0.5

def checkkint(msg):
    while 1:
        try:
            n = input(msg)
            return(int(n))
        except ValueError:
            print("Masukkan sebuah bilangan bulat")

def deltacondition(point,i,mid,temp_min) :
    res=True
    for j in range(len(point[0])) :
        if(abs(point[i][j]-point[mid][j])<temp_min) :
            res=True
        else :
            return False
    return res