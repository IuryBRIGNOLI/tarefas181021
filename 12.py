
menu = int(input("1-Somar \n 2-Multiplicar \n 3-Maior \n 4-Menor \n 5-Sair \n"))
a = int(input("Digite um valor "))
b =  int(input("Digite outro valor"))

while True:
    if menu == 1 :
        print(a+b)
        break
    if menu == 2 :
        print(a*b)
        break
    if menu == 3 and a > b:
        print(a)
        break
    else:
        print(b)
        break
    if menu == 4 and a > b:
        print (b)
        break
    else:
        print(a)
        break
    if menu == 5 : 
        break                   
