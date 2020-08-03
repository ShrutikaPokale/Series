def f(n):
    if n==0:
        y=0
    elif n==1:
        y=1
    else:
        y=3*f(n-1) - 2*f(n-2) 
    return y
def is_part_of_series(lst):
    output=[]
    for i in lst:
        j=2
        while(j>=2):
            check=f(j)
            if check==int(i):
                output.append(i)
                break
            elif check>int(i):
                break
            j+=1
    return output
    
data=list(map(int,input().split()))
print(is_part_of_series(data))
