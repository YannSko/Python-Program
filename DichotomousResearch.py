l = [1, 4, 6, 11, 12, 16, 20, 20, 22, 24, 25, 30, 33, 40]
# -> Index
# -> -1 : non trouvé



def Dichotomous(l, e, imin, imax):
    if imax-imin == 0:
        if l[imin] == e:
            return imin
        return -1
    if imax-imin == 1:
        if l[imin] == e:
            return imin
        if l[imax] == e:
            return imax
        return -1
    icenter = (imax+imin)//2
    if l[icenter] == e:
        return icenter
    if l[icenter] < e:
        return Dichotomous(l, e, icenter+1, imax)
    return Dichotomous(l, e, imin, icenter-1)

print(binary_search(l, 24, 0, len(l)-1))




