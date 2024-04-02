lista_ativos = []
quant_ativos = int(input())

for a in range(quant_ativos):
    cod_ativo = input()
    lista_ativos.append(cod_ativo) 
    lista_ativos.sort()

for elemento in lista_ativos:
    print(elemento)

