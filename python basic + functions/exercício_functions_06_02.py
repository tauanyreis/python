

"""Exercício functions"""


produtos = ['beb46275','TFA23962','TFA69555','TFA56743','BSA45510','TFA44968','CAR75448','CAR23596']

def check_alcool(produtos_bebidas):
    produtos_bebidas = produtos_bebidas.upper()

    return produtos_bebidas


print(check_alcool(produtos[0]))

def ehalcoolico(bebida):
    bebida = bebida.upper()
    if "BEB" in bebida:
        return True
    
    else:
        return False
    
# print(ehalcoolico('beb46275'))


for cada_item in produtos:
    if ehalcoolico(cada_item):
        print(f'Enviar o produto {cada_item} para o setor de bebidas alcoólicas')

    else:
        print(f'Enviar o produto {cada_item} para o setor de bebidas não alcoólicas')




