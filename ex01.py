#
#
# autores: Cristiano, Michel
# 18/09/2023
#
lista01 = [1, '2', 3]
tupla01 = (1, '2', 3)

# lendo
print(lista01[1])
print(tupla01[1])

# gravando
lista01.append(4)
# tupla.append(4)  # essa linha gera um error!
print(lista01)

lista02 = list(tupla01)
print(lista02)

tupla02 = tuple(lista01)
print(tupla02)

tupla03 = (1, [1,2,3], 4)
tupla03[1].append(5)
print(tupla03)

lista05 = []
tupla04 = ()
lista06 = [1]
tupla06 = (1,)
tupla07 = (1)
print(tupla06)
print(tupla07)

tupla08 = tuple(range(6))
print(tupla08)
print(tupla08[2:4])