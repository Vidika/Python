def fibonnaci_numbers_upto_n(n):
    previous=1
    current=1
    numbers=[]
    while current<=n:
        numbers.append(current)
        previous,current=current,previous+current
    return numbers
def encode(n):
    numbers=fibonnaci_numbers_upto_n(n)
    remainder=n
    bits=['0']*len(numbers)+['1']
    for i in range(len(numbers)-1,-len(numbers),-1):
        if remainder==0:
            break
        if remainder>=numbers[i]:
            bits[i]='1'
            remainder-=numbers[i]
    return ''.join(bits)

def decode(code):
    if len(code)<=2 or code[-2:]!='11':
        return 0
    previous=1
    current=1
    n=0
    previous_bit=False
    for bit in (int(c) for c in code[:-1]):
        if bit:
            if previous_bit:
                return 0
            n+=current
            previous_bit=True
        else:
            previous_bit=False
            previous,current=current,previous+current
    return n
