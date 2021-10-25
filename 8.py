contadorM = 0
contadorMR = 0 
ano = 2021
for v in range(1,8):
       a =  int(input("Digite sua data de nascimento"))

       idade = ano - a
       if idade < 18 :
        print("É de menor ") 
        contadorMR+=1
       else:
        print("É de maior ") 
        contadorM+=1
print("São {} maiores idade  e {} menores de idade: ".format(contadorM,contadorMR))
print(f'São {contadorM} maiores idade  e {contadorMR} menores de idade:')
