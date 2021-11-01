contador = 0
contadores = 0
while True :
    a = int(input("Digite um número"))
    contadores +=1
    contador = contador+a
    if a == 1000:
        contador = contador - 1000
        break
contadores = contadores-1    
print(contador)
print(contadores)    
