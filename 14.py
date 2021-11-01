contador = 0 
while True :
    a = int(input("Digite um número"))
    contador+=1
    h = a+a
    b = int(input("Deseja continuar?").upper())
    if b ==  "nao" or "não" :
        break 
print(h/contador)    



