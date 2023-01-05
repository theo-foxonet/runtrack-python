L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
vmax = L[0]
vmin = L[0]
for i in L:
    if i > vmax:
        vmax = i
    elif i < vmin:
        vmin = i
print("Valeur minimum :", vmin)
print("Valeur maximum :", vmax)