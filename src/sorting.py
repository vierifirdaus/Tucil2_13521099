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

def sort(arr,l,r) :
    if l<r :
        pi=partition(arr,l,r)
        sort(arr,l,pi-1)
        sort(arr,pi+1,r)

arr=[[1,2,12],[4,4,3],[2,6,5],[3,8,0]]
ar=[3,2,4,1,5]
sort(ar,0,len(ar)-1)
print(ar)
sort(arr,0,len(arr)-1)
print(arr)