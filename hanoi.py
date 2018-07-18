def hanoi(n,peg_1,peg_3,peg_2):
    if n ==1:
        print(f'Move from {peg_1} to {peg_3}')
    else:
        hanoi(n-1,peg_1,peg_2,peg_3)
        print(f'Move from {peg_1} to {peg_3}')
        hanoi(n-1,peg_2,peg_3,peg_1)        

def permute(L):
    yield from heap_permute(L,len(L))

def heap_permute(L,length):
    if length <=1:
        yield L
    else:
        length-=1
        for i in range(length):
            yield from heap_permute(L,length)
            if length%2:
                L[i],L[length]=L[length],L[i]
            else:
                 L[0],L[length]=L[length],L[0]
        yield from heap_permute(L,length)
    
