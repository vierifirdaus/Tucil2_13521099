from input import *
from point import *
from sorting import *
from plot import *
import time
def main() :

    point=[]
    (derajatcnt,titikcnt)=inp()
    point=pointinput(derajatcnt,titikcnt)
    sorting(point,0,len(point)-1)

    dncawal=time.time()
    iDNC,jDNC,solutionDNC,cntDNC=Closest(point,0,titikcnt-1)
    dncakhir=time.time()
    iBF,jBF,solutionBF,cntBF=brute_force(point,0,titikcnt-1)
    bfakhir=time.time()

    aa=(dncakhir-dncawal)
    bb=(bfakhir-dncakhir)
    print("Solusi koordinat titik berdasarkan DNF: ")
    print(point[iDNC])
    print(point[jDNC])
    print("Dengan jarak :",solutionDNC)
    print("Solusi koordinat titik berdasarkan BF: ")
    print(point[iBF])
    print(point[jBF])
    print("Dengan jarak :",solutionBF)
    print("DNC :",aa*1000,"ms")
    print("BF :",bb*1000,"ms")

    print("Banyak proses DNC:",cntDNC)
    print("Banyak proses BF:",cntBF)

    if(derajatcnt==2 or derajatcnt==3) :
        tampilkan=input("Apakah ingin menampilkan plot dalam 2D atau 3D? (y/n): ")
        if(tampilkan=="y") :
            if(derajatcnt==3) :
                plot3d(point,iDNC,jDNC)
            if(derajatcnt==2) :
                plot2d(point,iDNC,jDNC)

main()
