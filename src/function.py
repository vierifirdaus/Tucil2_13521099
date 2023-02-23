def swap(a,b) :
    return (b,a)

def distance(a,b) :
    res=0.0
    if(type(a)==int) :
        return abs(a-b)
    for i in range(len(a)) :
        res+=(a[i]-b[i])**2
    return res**0.5