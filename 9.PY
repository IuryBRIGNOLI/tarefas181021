maior = 0
menor = 0
ct =0

for a in range(1,6):
    b = int(input("Digite um peso em quilos"))
    ct+=1
    
    if ct  == 1 :
        maior = menor = b 
    if b > maior :
        maior = b
    if b < menor:
        menor = b
print(f"O maior peso é {maior} e o menor peso é {menor}")
    