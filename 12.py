aaaa = 1
menu = int(input("1-Somar \n2-Multiplicar \n3-Maior \n4-Menor \n5-Sair"))
a = int(input("Digite um valor "))
b =  int(input("Digite outro valor"))

while(aaaa==1):
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
    if menu == 4 and a < b:
        print (b)
        break
    else:
        print(a)
        break
    if menu ==5 :
        aaaa = 0 
        break                   
