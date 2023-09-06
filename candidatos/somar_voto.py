def somar_voto(dicio: dict, chave: str) -> dict:
    '''
    crie agora a função somar_voto() com os parâmetros: dicionário e candidato, e adicione 1 voto no candidato. 	
    '''
    dicio[chave] += 1
    return dict