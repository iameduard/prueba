import numpy as np 

for n in range(1,554):
    div=[]
    for d in range(2,n/2+1):
        if not(n%d):
            div.append(d)
            max=d
    max=len(div)
    try:
        assert max
        flag=True
        for k in range(1,2**max-1):
            r=list(str(bin(k))[2:])
            r2=[int(c) for c in r]
            v=[0]*(max-len(r2))+r2 
            try:
                assert np.dot(div,v)-n
            except AssertionError:
                flag=False
                break
        print "%i has no subset whose sum is equal to %i" % (n,n) if flag else 'There is a subset equal to %i.'% n
    except AssertionError:
        print "%i is prime number" %n
