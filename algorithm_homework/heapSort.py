import module

def heapify(li, idx, n):
    l = idx * 2
    r = idx * 2+1
    s_idx = idx
    if(l<= n and li[s_idx] >li[l]):
        s_idx = l
    if(r<=n and li[s_idx] > li[r]):
        s_idx = r
    if s_idx != idx:
        module.swapListNumber(li,idx,s_idx)
        return heapify(li, s_idx, n)

def heap_sort(v):
    n = len(v)
    v = [0]+v
    for i in range(n,0,-1):
        heapify(v,i,n)
    
    for i in range(n, 0, -1):
        print(v[1])
        module.swapListNumber(v,i,1)
        heapify(v, 1, i-1)

randomNumber=module.randomNumberGenerator(20)
heap_sort(randomNumber)
