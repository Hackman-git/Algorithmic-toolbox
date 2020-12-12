def Euclidean(a,b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return Euclidean((max(a,b) % min(a,b)), min(a,b))

print(Euclidean(3284399392838490655555632936,8473746637283884334342325552585244))