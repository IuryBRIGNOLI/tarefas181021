contF = 0
somaidade = 0
maior = 0  
for a in range(1,5):
    nome = input("Digite seu nome ")
    Idade = int(input("Digite sua idade"))
    sexo  = str(input("Digite seu sexo M, F ")).upper()

    somaidade += Idade
    media=(somaidade)/4

    if sexo == "M":
        if Idade > maior:
            maior = Idade
            nomeM = nome

    elif sexo == "F" and Idade < 20:
        contF += 1
print(f"Média de idade {media}")  
print(f"Quantidade de mulheres menores de 20 anos {contF}") 
print(f"Homem mais velho {nomeM}") 




