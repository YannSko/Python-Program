#Quicksort
def quicksort(l):
    qsort_loop(l, 0, len(l)-1)

def qsort_loop(l, imin, imax):
    if imax-imin == 1:
        if l[imin] > l[imax]:
            '''c = l[imin]
            l[imin] = l[imax]
            l[imax] = c'''
            l[imin], l[imax] = l[imax], l[imin]
        return
    if imax-imin == 0:
        return

    p = l[imax]
    a = 0
    for i in range(imin, imax):
        if l[i] <= p:
            l[a+imin], l[i] = l[i], l[a+imin]
            a += 1
    l[a+imin], l[imax] = p, l[a+imin]
    if a != 0:
        qsort_loop(l, imin, a+imin-1)
    if imax > a+imin+1 :
        qsort_loop(l, a+imin+1, imax)