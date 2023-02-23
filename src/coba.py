def a(lis,n):
    for i in range(n):
        lis[i]=lis[i]+1

def swap(a,b) :
    return (b,a)

arr=[1,2,3,4]
c=[4,3,2,1]
(arr,c)=swap(arr,c)
print(arr)
print(c)
