import sqlite3 as sql

def conectar(banco_dados: str) -> tuple:
    conexao = sql.connect(banco_dados)
    cursor = conexao.cursor()
    return conexao, cursor

def inserir(banco_dados:str, nome_tabela:str, colunas_tabela:tuple, valores_tabela:tuple) -> None:
    """Método para inserir dados/registros na tabela do banco de dados"""
    conectar(banco_dados)[1].execute(f"INSERT INTO {nome_tabela} {colunas_tabela} VALUES {valores_tabela}")
    conectar(banco_dados)[0].commit()
    

def funcao_1() -> tuple:
    return "conexao", 12 # O retorno de duas informações(valores) gera uma TUPLA.

def funcao_2(*args: tuple) -> tuple:
    return args

def funcao_3(**kwargs: tuple) -> dict: # Key (chave) + wargs (valores [args = argumentos]) = retorna um dicionário.
    return kwargs

print(funcao_2('opa', 21))
print(funcao_3(
    nome= "Rodolfo",
    idade= 18,
    habilitado= True,
    altura= 1.77
    )
)

print(type(funcao_2))
print(type(funcao_3))