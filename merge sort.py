def merge(list):
    if len(list)>1:
        m=len(list)//2
        left=list[:m]
        right=list[m:]
        merge(left)
        merge(right)
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                list[k]=left[i]
                k+=1
                j+=1
            else:
                list[k] = right[i]
                k+=1
                j+=1
        while i<len(left):
            list[k]=right[i]
            i=i+1
            k=k+1
        while i < len(left):
            list[k] = right[j]
            j=j+1
            k=k+1


list=list(input("enter elements : ").split(' '))
merge(list)
print(list)