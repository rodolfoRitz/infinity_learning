from crudgenerico import CRUDGenerico as CRUD

banco = CRUD(
    banco_dados="loja.db",
    usuario="admin",
    senha="admin"
)

print(
    """
    1 - Novo Registro
    2 - Consultar Registro
    3 - Listar Registro
    4 - Atualizar Registro
    5 - Apagar Registro
    """
)

opcao = input("Informe a opção desejada: ")

match opcao:
    case '1':
        tabela = input('Informe o nome da tabela: ')
        colunas = input('Informe as colunas (separadas por vírgula): ')
        valores = input('Informe os valores (separadas por vírgula): ')
        
        banco.inserir(
            tabela=tabela,
            colunas=colunas,
            valores=valores
        )
    case '2':
        pass
    case '3':
        pass
    case '4':
        pass
    case '5':
        pass