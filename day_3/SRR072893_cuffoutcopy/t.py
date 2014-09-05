
revcompl = lambda x: ''.join([{'A':'T','C':'G','G':'C','T':'A'}[B] for B in x][::-1])
print revcompl("AGTCAGCAT")


def revcompl2( x ): 
    return ''.join([{'A':'T','C':'G','G':'C','T':'A'}[B] for B in x][::-1])
print revcompl("AGTCAGCAT")


l = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]

print sorted( l, key=lambda x: x % 2 )
