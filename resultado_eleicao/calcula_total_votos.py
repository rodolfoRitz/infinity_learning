from ..programa_principal import candidatos

def calcula_total_votos():
    '''
    crie uma função calcula_total_votos() que retorna a soma de todos os votos de todos os candidatos.
    '''
    total_votos = sum(candidatos.values)
    return total_votos