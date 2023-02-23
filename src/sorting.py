def swap(a,b) :
    return (b,a)

def partition(arr,l,r) :
    if(type(arr[0])==int) :
        pivot=arr[r]
    else :
        pivot=arr[r][0]

    i=l-1
    
    for j in range(l,r) :
        if(type(arr[0])==int) :
            if arr[j]<pivot :
                i+=1
                arr[i],arr[j]=swap(arr[i],arr[j])
        else :
            if arr[j][0]<pivot :
                i+=1
                arr[i],arr[j]=swap(arr[i],arr[j])
    arr[i+1],arr[r]=swap(arr[i+1],arr[r])
    return i+1

def sorting(arr,l,r) :
    if l<r :
        pi=partition(arr,l,r)
        sorting(arr,l,pi-1)
        sorting(arr,pi+1,r)

