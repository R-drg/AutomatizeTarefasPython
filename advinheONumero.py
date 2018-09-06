# coding: utf-8
import random

x=random.randint(1,20)
print("Estou pensando em um numero entre 1 e 20. Você tem 5 chances para advinha-lo")
for i in range(1,6):
    print("Chute um número:")
    chute = int(input())

    if chute<x:
        print('Muito baixo')
    elif chute>x:
        print('Muito alto')
    else:
        break

if chute == x:
     print("Parabéns! Você acertou em " + str(i) + " tentativas.")
else:
    print("Que pena. O número era "+ str(x))
