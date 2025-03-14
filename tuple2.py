# add
set  = {1, 1,2,4, 7, 7, 8, 9}
print("set:", set)

set.add(3)
print("added set:", set)


# set intersection
seti = {1,2,3,4,5,5}
setii = {4,5,6,7,8,9,9}

print("original sets")
print(seti)
print(setii)

setiii = seti.intersection(setii)
print(setiii)


#union

setU = {"mango", "peach", "orange", "orange"}
setUU = {"grape", "grape", "grape", "apple"}

print(setU)
print(setUU)
setUUU = setU.union(setUU)
print(setUUU)


#symetrical differences

setD = {1, 2, 6, 7, 8}
setDD = {8, 8, 9}
print(setD)
print(setDD)

print("difference:")
print(setD.difference(setDD))
print(setD.symmetric_difference(setDD))