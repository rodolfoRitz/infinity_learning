def adicionar_candidato(candidatos:dict, nome_candidato:str) -> dict:
    '''
    função adicionar_candidato() em que você passa como 
    parâmetro um dicionário e o nome do candidato a ser adicionado.
    '''
    candidatos[nome_candidato] = 0
    return dict