def oddsum(a,b):
    sum = 0
    for i in range(a,b+1):
        if(i%2==0):
            pass
        else:
            sum += i
    return sum

print(oddsum(4298,9290))
