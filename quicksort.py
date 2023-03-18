a=[int(i) for i in input().split()]
def quickSort(a):
    if (len(a)<2):
        return a
    if (len(a)==2):
        if (a[0]<a[1]):
            return a[0],a[1]
        else:
            return a[1],a[0]
    b=len(a)//2
    #print(b)
    j=0 
    k=len(a)-1
    while a[j]<a[b]:
        j+=1
    while a[k]>a[b]:
        k-=1
    w=a[j]
    a[j]=a[k]
    a[k]=w
    return list(quickSort([x for x in a if x<a[b]]))+list([x for x in a if x==a[b]])+list(quickSort([x for x in a if x>a[b]]))
O=quickSort(a)
print(O)
