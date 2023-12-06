'''
SELECT *
FROM clientes c
INNER JOIN pedidos p ON c.id_cliente = p.id_cliente
WHERE id_cliente=1

SELECT *
FROM pedidos p
INNER JOIN clientes c ON p.id_cliente = c.id_cliente
WHERE id_cliente=1
ORDER BY total_pedidos
'''

import sqlite3 as sql

class CRUDGenerico:
    def __init__(self, banco_dados, usuario, senha) -> None:
        # Cláusulas de guarda (dunder objects)
        self.banco_dados = banco_dados
        self.usuario = usuario
        self.senha = senha
        
        self.conexao = None
        self.cursor = None
    
    def logar(self) -> bool:
        '''
        Método para logar no sistema (ESTES SEIS PONTINHOS DEIXAM A LETRA MAIOR)
        ------ 
        '''
        USUARIO = 'admin'
        SENHA   = 'admin'
        
        return True if self.usuario == USUARIO and  self.senha == SENHA else False
    
    def conectar(self) -> bool:
        if self.logar() == True: # Login bem-sucedido
            self.conexao = sql.connect(self.banco_dados)
            self.cursor  = self.conexao.cursor()
            return True
    
    def desconectar(self) -> None:
        if self.conectar() == True: # Verifica se está conectado
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
        
    def alterar(self, tabela:str, id:int, coluna:str, novo_valor=any) -> list[tuple[any]]: # UPDATE
        backup = self.consultar(tabela=tabela, id=id)
        if self.conectar() == True:
            self.cursor.execute(
                f"UPDATE {tabela} SET {coluna} VALUES {novo_valor} WHERE id={id}"
        )
        self.conexao.commit()
        novo_registro_atualizado = self.consultar(tabela=tabela, id=id)
        return backup, novo_registro_atualizado
    
    def apagar(self, tabela:str, id:int) -> list[tuple[any]]: # DELETE
        backup = self.consultar(tabela=tabela, id=id)
        if self.conectar() == True:
            self.cursor.execute(
                f"DELETE FROM {tabela} WHERE id={id}"
        )
        self.conexao.commit()
        return backup