s=0
a = int(input("Digite um número"))
for i in range(1):
    if a % 2== 0 and a % 1== i:
        print("É um número primo {}".format(a))
    else:
        print("Não e um número primo ")    
       