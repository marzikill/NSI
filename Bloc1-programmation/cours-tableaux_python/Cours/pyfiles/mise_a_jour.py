def mise_a_jour(t):
    # On ne peut pas avoir 21/20.
    if t[0] <= 19:
        t[0] = t[0] + 1
    if t[2] <= 19:
        t[2] = t[2] + 1
    return t

# Test
t = [5, 7, 6, 9, 10, 11, 10]
print('Après mise à jour des notes :', mise_a_jour(t))
# Output :
# Après mise à jour des notes : [6, 7, 7, 9, 10, 11, 10]
