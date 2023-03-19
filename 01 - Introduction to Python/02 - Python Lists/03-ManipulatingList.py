# Change List Elements
# Add elements to the list
# Delete elements from the list

# Change List Elements
fam = ["liz", 1.73, "emma", 1.68, "mom", 1.71, "dad", 1.89]
print(fam)

fam[7] = 1.86
print(fam)

fam[0:2] = ["lisa", 1.74]
print(fam)

# Add elements to the list
fam = fam + ["me", 1.79]
print(fam)
fam_ext = fam + ["new", 2.56]
print(fam_ext)

# Delete elements from the list
del (fam_ext[2])
print(fam_ext)

# Copy a list
fam_copy = fam
print(fam_copy)
