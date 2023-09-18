#
#
# autores: Cristiano, Michel
# 18/09/2023
#

# 1 – gere tupla dinamicamente de tamanho 5, de valores 
# aleatório entre 1 e 20

import random

lista =[]
for i in range(5):
  lista.append(random.randint(1,20))
  
tupla = tuple(lista)
print(tupla)
