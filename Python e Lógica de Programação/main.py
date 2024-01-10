from modelos.crudgenerico import CRUDGenerico

banco= CRUDGenerico(
        banco_dados="teste.db",
        usuario="admin",
        senha="admin"
)

banco.inserir(
    tabela="usuarios",
    colunas=("nome", "idade"),
    valores=("Rodolfo", 12)
)