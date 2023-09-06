'''
from candidatos.adicionar_candidato import ex, ex2
from ..exemplo import funcao #Volta as pastas.
'''
def alterar_nome_candidato(dicio:dict, nome_antigo:str, nome_novo:str) -> dict:
    '''crie agora a função alterar_nome_candidato() com os parâmetros: 
    dicionário, nome_antigo e nome_novo e ao executar a função altere o nome do canditado.
    '''
    dicio[nome_antigo] = dicio[nome_novo]
    return dict