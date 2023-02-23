from function import *
from sorting import *
point=[]
derajatcnt=0
titikcnt=0
def inp() :
    derajatcnt=checkkint("Masukkan banyak derajat : ")
    titikcnt=checkkint("Masukkan banyak titik : ")
    return (derajatcnt,titikcnt)

def pointinput(derajatcnt,titikcnt) :
    arr=[]
    for i in range(titikcnt) :
        arr.append([])
        for j in range(derajatcnt) :
            arr[i].append(random.uniform(-100,100))
    return arr

