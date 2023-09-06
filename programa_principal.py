from candidatos.adicionar_candidato import *
from candidatos.alterar_nome_candidato import *
from resultado_eleicao.anuncia_vencedor import *
from resultado_eleicao.calcula_total_votos import *
from resultado_eleicao.mostra_resultado import *

'''
simule uma urna eletrônica com 3 candidatos: Candidato A, Candidato B e Candidato C. 
Adicione um candidato chamado “Candidato D” por meio de uma função adicionar_candidato() 
em que você passa como parâmetro um dicionário e o nome do candidato a ser adicionado.
'''

candidatos = {'Candidato A': 0, 'Candidato B': 0, 'Candidato C': 0}

adicionar_candidato(candidatos, 'Candidato D')

print(candidatos)

#anuncia_vencedor()