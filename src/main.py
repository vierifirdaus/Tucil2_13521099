from input import *
from point import *
from sorting import *
from plot import *
import time
def main() :
    point=[]
    (derajatcnt,titikcnt)=inp()
    point=pointinput(derajatcnt,titikcnt)
    # print((point))
    sorting(point,0,len(point)-1)
    # print((point))
    dncawal=time.time()
    # print(dncawal)
    ii,jj,solution=Closest(point,0,titikcnt-1)
    # print(Closest(point,0,titikcnt-1))
    dncakhir=time.time()
    ii,jj,solution=brute_force(point,0,titikcnt-1)
    # print(dncakhir)
    # print(brute_force(point,0,titikcnt-1))
    bfakhir=time.time()
    aa=(dncakhir-dncawal)
    bb=(bfakhir-dncakhir)
    print("DNC : ",aa*1000,"ms")
    print("BF : ",bb*1000,"ms")
    if(derajatcnt==3) :
        plot(point,ii,jj)
    # while(1) :
    #     point=pointinput(derajatcnt,titikcnt)
    #     sorting(point,0,len(point)-1)
    #     if(Closest(point,0,titikcnt-1)!=brute_force(point,0,titikcnt-1)) :
    #         print("error")
            # break
    # while(Closest(point,0,titikcnt-1)==brute_force(point,0,titikcnt-1)) :
    #     point=pointinput(derajatcnt,titikcnt)
main()
