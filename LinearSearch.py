#linear search(l,e)
#--> index first occurence
# --> -1: if nothing found

def linear_search(l,e):
    for i in range(len(l)):
        if l[i]==e:
            return i
    return -1