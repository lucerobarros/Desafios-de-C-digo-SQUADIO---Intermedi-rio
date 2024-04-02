deposito = float(input())
saldo = 0

if deposito > 0:
  saldo = saldo + deposito
  print('Deposito realizado com sucesso! \nSaldo atual: R$ {:.2f}'.format(saldo))
elif deposito < 0:
   print('Valor invalido! Digite um valor maior que zero.')
else:
   print('Encerrando o programa...')