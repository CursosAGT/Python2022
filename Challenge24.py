
'''
DESAFIO N~'24
 * ITERATION MASTER
 * Fecha publicación enunciado: 13/06/22
 * Fecha publicación resolución: 20/06/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Quiero contar del 1 al 100 de uno en uno (imprimiendo cada uno). 
 ¿De cuántas maneras eres capaz de hacerlo? Crea el código para cada una de ellas.
'''



#         ############################################1

print("**** 1 ****")

for index in range(1,101):
    print(index, end=", ")

print()

#         ############################################2

print("**** 2 ****")
class MyNumbers:
  def __iter__(self):
    self.index = 1
    return self

  def __next__(self):
    if self.index <= 100:
      x = self.index
      self.index += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)
print (list(myiter))

#         ############################################3

print("**** 3 ****")

index = 1
while index <101:
    print(index, end=", ")
    index+=1
print()
#         ############################################4

print("**** 4 ****")
import itertools
for index in itertools.count():
    print(index, end=", ")
    
    if index == 100:
        break
print()
#         ############################################5

print("**** 5 ****")

def print100(index) :
    if (index <= 100) :
        print(index, end=", ")
        return print100(index + 1)

print100(1)
print()
#         ############################################6

print("**** 6 ****")

print(f"{[index for index in range(1,101)]}")

#         ############################################7

print("**** 7 ****")

import numpy as np
vector=  np.arange(100, dtype=np.int64)
print (f"{vector=}")
