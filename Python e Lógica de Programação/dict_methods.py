'''
.clear() - Limpa o dicionário
.copy() - Faz uma cópia das chaves e dos valores do dicionário.
.fromkeys() - Cria um dicionário a partir das chaves e dos valores específicados.
.get() - Retorna o valor da chave informada.
.items() - Retorna uma lista contendo uma tupla para cada chave e valor.
.keys() - Retorna uma lista contendo todas as chaves do dicionário.
.pop() - Remove a chave e seu respectivo valor informado.
.popitem() - Remove a "última" chave e seu respectivo valor informado.
.update() - Atualiza o valor da chave informada (sobescreve).
.values() - Retorna uma lista contendo os valores do dicionário.

.fromkeys(chave,valor) - Será construído um dicionário a partir da(s) chave(s) e valor(es) informado(s).
.get(chave) - Exibe o valor da chave informada.
.pop(chave) - Ao informar a chave, será removida a chave e seu valor.
.update({chave,valor}) - Atualiza o valor(informado) da chave (informada).

.zip(keys, values) combina as duas listas em pares chave-valor, e em seguida, a função 
.dict() - Cria um dicionário a partir desses pares.
Caso as duas listas tenham tamanhos diferentes, a criação do dicionário será interrompida no 
comprimento da lista mais curta. Qualquer elemento excedente na lista mais longa será ignorado.
Lembre-se de que as chaves do dicionário devem ser únicas. Se houver chaves duplicadas na lista 
de chaves, apenas a última ocorrência será mantida no dicionário resultante.

print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for chave, valor in pessoas.items():
    print(chave, '-', valor)
'''
