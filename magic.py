all_non_zero_digits=set(range(1,10))
for a in range(1,10):
    for b in range(1,10):
        candidate=(a,15-a-b,b,
                   5+b-a,5,5+a-b,
                   10-a,a+b-5,10-b)
        if set(candidate)==all_non_zero_digits:
            print(' {:} {:} {:}\n {:} {:} {:}\n {:} {:} {:}\n'.format(*candidate))
