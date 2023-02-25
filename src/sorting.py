def swap(a,b) :
    return (b,a)

def partition(arr,l,r,param) :
    pivot=arr[r][param]
        
    i=l-1
    
    for j in range(l,r) :
        if arr[j][param]<pivot :
            i+=1
            arr[i],arr[j]=swap(arr[i],arr[j])
            
    arr[i+1],arr[r]=swap(arr[i+1],arr[r])
    return i+1

def sorting(arr,l,r,param) :
    if l<r :
        pi=partition(arr,l,r,param)
        sorting(arr,l,pi-1,param)
        sorting(arr,pi+1,r,param)

