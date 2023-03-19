# Lists in Python
fam = [1.73, 1.68, 1.71, 1.89]
print(fam)

fam2 = ["Liz", 1.73, "Emma", 1.68, "Mom", 1.71, "Dad", 1.89]
print(fam2)

fam3 = [["Liz", 1.73], ["Emma", 1.68], ["Mom", 1.71], ["Dad", 1.89]]
print(fam3)

print(type(fam))

# Subsetting Lists
print(fam2[3])
print(fam2[6])
print(fam2[-1])
print(fam2[7])

# List Slicing
# [start:end] - start is inclusive and end is exclusive
print(fam[3:5])
print(fam[1:4])
print(fam[:4])
print(fam[5:])

# List Manipulation
fam_new = ["Liz", 1.73, "Emma", 1.68, "Mom", 1.71, "Dad", 1.89]
fam_new = fam_new + ["Me", 1.79]
print(fam_new)

del (fam_new[2])

fam_new[2] = "Nabeel"
print(fam_new)

# copy lists
list1 = [1, 2, 3, 4, 5]
list2 = list1
list2[0] = 10
print(list1)
print(list2)

list3 = list1[:]
list3[0] = 1
print(list1)
print(list3)
