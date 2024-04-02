# A senha deve ter no mínimo 8 caracteres. ok
# A senha deve conter pelo menos uma letra maiúscula (A-Z).
# A senha deve conter pelo menos uma letra minúscula (a-z).
# A senha deve conter pelo menos um número (0-9).
# A senha deve conter pelo menos um caractere especial, como !, @, #, $, %, etc.

senha = input().strip()
comprimento_minimo = 8
tem_letra_maiuscula = False
tem_letra_minuscula = False
tem_numero = False
tem_caractere_especial = False

if len(senha) < comprimento_minimo:
    print('Sua senha e muito curta. Recomenda-se no minimo {} caracteres.'.format(comprimento_minimo))
else:
    for caractere in senha:
        if caractere.isupper():
            tem_letra_maiuscula = True
        elif caractere.islower():
            tem_letra_minuscula = True
        elif caractere.isdigit():
            tem_numero = True
        else:
            tem_caractere_especial = True

    if tem_letra_maiuscula and tem_letra_minuscula and tem_numero and tem_caractere_especial:
        print('Sua senha atende aos requisitos de seguranca. Parabens!')
    else:
        print('Sua senha nao atende aos requisitos de seguranca.')


