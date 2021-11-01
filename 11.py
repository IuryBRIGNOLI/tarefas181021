next = 1
 
while(next == 1):
    sexo = input('Digite seu sexo (M ou F):')
    if(sexo == "M" or sexo == "F"):
        next = 0
    else: print("Errado digite novamente!!")