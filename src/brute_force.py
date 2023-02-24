from function import *

def brute_force(point,start,end) :
    cnt_distance=0
    solution=float('inf')
    point_i=start
    point_j=end
    for i in range(start,end+1) :
        for j in range(i+1,end+1) :
            cnt_distance+=1
            if(distance(point[i],point[j])<solution) :
                solution=distance(point[i],point[j])
                point_i=i
                point_j=j

    return (point_i,point_j,solution,cnt_distance)

