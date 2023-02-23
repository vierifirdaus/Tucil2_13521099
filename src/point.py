from function import *
from brute_force import *

def Closest(point,start,end) :
    point_i=-1
    point_j=-1
    solution=float('inf')

    if(end-start<=3) :
        return brute_force(point,start,end)

    mid=(end+start)//2
    min_left=Closest(point,start,mid)
    min_right=Closest(point,mid+1,end)

    if(min_left[2]<min_right[2]) :
        point_i=min_left[0]
        point_j=min_left[1]
        solution=min_left[2]
    else :
        point_i=min_right[0]
        point_j=min_right[1]
        solution=min_right[2]

    temp_solution=[mid]

    for i in range(start,end+1) :
        # if(deltacondition(point,i,mid,solution) and i!=mid) :
        #     temp_solution.append(i)
        if(abs(point[i][0]-point[mid][0])<solution and i!=mid) :
            temp_solution.append(i)

    for i in range(len(temp_solution)) :
        for j in range(i+1,len(temp_solution)) :
            if(deltacondition(point,temp_solution[i],temp_solution[j],solution)) :
                if(distance(point[temp_solution[i]],point[temp_solution[j]])<solution) :
                    solution=distance(point[temp_solution[i]],point[temp_solution[j]])
                    point_i=temp_solution[i]
                    point_j=temp_solution[j]
    return (point_i,point_j,solution)

