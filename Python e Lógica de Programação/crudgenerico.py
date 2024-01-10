import sqlite3 as sql

class CRUDGenerico:
    def __init__(self, banco_dados, usuario, senha) -> None:      # Cláusulas de guarda (dunder objects)
        self.banco_dados = banco_dados
        self.usuario = usuario
        self.senha = senha
        
        self.conexao = None
        self.cursor = None
    
    def logar(self) -> bool:
        USUARIO = 'admin'
        SENHA   = 'admin'
        
        return True if self.usuario == USUARIO and  self.senha == SENHA else False
    
    def conectar(self) -> bool:
        if self.logar() == True: # Login bem-sucedido
            self.conexao = sql.connect(self.banco_dados)
            self.cursor  = self.conexao.cursor()
            return True
    
    def desconectar(self) -> None:
        if self.conectar == True: # Verifica se está conectado
            self.conexao.close()
    
    # Métodos do CRUD Genérico (manipular banco de dados)
    def inserir(self, tabela:str, colunas:tuple[str], valores: tuple[any]) -> None: # CREATE
        """
        Descrição: Insere dados no banco que dados.
        Args:
            tabela (str): nome da tabela
            colunas (tuple[str]): valores das colunas
            valores (tuple[any]): valores das variáveis
        """
        if self.conectar == True: # se estiver conectado
            self.cursor.execute(
                f"INSERT INTO {tabela} {colunas} VALUES {valores}"
            )
            self.conexao.commit()

    def consultar(self, tabela:str, id:int) -> list[tuple[any]]: # READ
        if self.conectar() == True: # se estiver conectado
            dados = self.cursor.execute(
                f"SELECT * FROM {tabela} WHERE id = {id}"
            ).fetchall()
            return dados
        
    def alterar(self) -> None: # UPDATE
        pass
    
    def apagar(self) -> None: # DELETE
        pass