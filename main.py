from sqlite3 import connect

conexao = connect(database="rod_sai.db")

cursor = conexao.cursor()

cursor.execute(
    "INSERT INTO clientes (nome, email, cidade, estado, telefone, saldo) VALUES (?, ?, ?, ?, ?, ?)",
        ("Lucas Silva", "lucas.silva@email.com", "São Paulo", "SP", "(11) 1234-5678", 78.5,
        "Pedro Oliveira", "pedro.oliveira@email.com", "Rio de Janeiro", "RJ", "(21) 2345-6789", 42.3,
        "Gustavo Pereira", "gustavo.pereira@email.com", "Belo Horizonte", "MG", "(31) 3456-7890", 64.7,
        "Rafael Santos", "rafael.santos@email.com", "Curitiba", "PR", "(41) 4567-8901", 90.2,
        "Matheus Almeida", "matheus.almeida@email.com", "Recife", "PE", "(81) 5678-9012", 15.0,
        "André Ferreira", "andre.ferreira@email.com", "Fortaleza", "CE", "(85) 6789-0123", 33.8,
        "Leonardo Souza", "leonardo.souza@email.com", "Salvador", "BA", "(71) 7890-1234", 72.1,
        "Thiago Rodrigues", "thiago.rodrigues@email.com", "Brasília", "DF", "(61) 8901-2345", 57.6,
        "Bruno Lima", "bruno.lima@email.com", "Porto Alegre", "RS", "(51) 9012-3456", 10.5,
        "Felipe Carvalho", "felipe.carvalho@email.com", "Manaus", "AM", "(92) 0123-4567", 87.9,
        "Victor Gomes", "victor.gomes@email.com", "Belém", "PA", "(91) 1234-5678", 29.4,
        "João Barbosa", "joao.barbosa@email.com", "Goiânia", "GO", "(62) 2345-6789", 55.2,
        "Gabriel Rocha", "gabriel.rocha@email.com", "Florianópolis", "SC", "(48) 3456-7890", 8.7,
        "Luiz Azevedo", "luiz.azevedo@email.com", "Natal", "RN", "(84) 4567-8901", 45.3,
        "Carlos Nunes", "carlos.nunes@email.com", "Fortaleza", "CE", "(85) 5678-9012", 21.6,
        "Ricardo Cunha", "ricardo.cunha@email.com", "Salvador", "BA", "(71) 6789-0123", 36.0,
        "Fernando Ribeiro", "fernando.ribeiro@email.com", "Recife", "PE", "(81) 7890-1234", 69.8,
        "Eduardo Cardoso", "eduardo.cardoso@email.com", "Brasília", "DF", "(61) 8901-2345", 95.2,
        "Luís Costa", "luis.costa@email.com", "São Paulo", "SP", "(11) 0123-4567", 73.4,
        "Marcelo Vieira", "marcelo.vieira@email.com", "Rio de Janeiro", "RJ", "(21) 2345-6789", 52.1,
        "Daniel Fonseca", "daniel.fonseca@email.com", "Belo Horizonte", "MG", "(31) 3456-7890", 14.8,
        "José Pereira", "jose.pereira@email.com", "Curitiba", "PR", "(41) 4567-8901", 18.3,
        "Anderson Silva", "anderson.silva@email.com", "Porto Alegre", "RS", "(51) 5678-9012", 61.7,
        "Marcos Reis", "marcos.reis@email.com", "Manaus", "AM", "(92) 6789-0123", 93.5,
        "Tiago Marques", "tiago.marques@email.com", "Belém", "PA", "(91) 7890-1234", 12.6,
        "Renato Santos", "renato.santos@email.com", "Goiânia", "GO", "(62) 0123-4567", 31.2,
        "Wagner Soares", "wagner.soares@email.com", "Florianópolis", "SC", "(48) 2345-6789", 77.0,
        "Henrique Sampaio", "henrique.sampaio@email.com", "Natal", "RN", "(84) 3456-7890", 5.4,
        "Lucas Barbosa", "lucas.barbosa@email.com", "Fortaleza", "CE", "(85) 4567-8901", 38.9,
        "Fábio Oliveira", "fabio.oliveira@email.com", "Salvador", "BA", "(71) 5678-9012", 47.3,
        "Antônio Alves", "antonio.alves@email.com", "Recife", "PE", "(81) 6789-0123", 60.1,
        "Diego Teixeira", "diego.teixeira@email.com", "Brasília", "DF", "(61) 8901-2345", 84.7,
        "Samuel Fernandes", "samuel.fernandes@email.com", "São Paulo", "SP", "(11) 0123-4567", 22.6,
        "Leandro Duarte", "leandro.duarte@email.com", "Rio de Janeiro", "RJ", "(21) 2345-6789", 50.2,
        "Roberto Coelho", "roberto.coelho@email.com", "Belo Horizonte", "MG", "(31) 3456-7890", 65.3,
        "Maurício Fernandes", "mauricio.fernandes@email.com", "Curitiba", "PR", "(41) 4567-8901", 9.8,
        "Igor Santos", "igor.santos@email.com", "Porto Alegre", "RS", "(51) 5678-9012", 34.7,
        "Junior Lima", "junior.lima@email.com", "Manaus", "AM", "(92) 6789-0123", 76.5,
        "Cláudio Gonçalves", "claudio.goncalves@email.com", "Belém", "PA", "(91) 7890-1234", 29.2,
        "Arthur Ribeiro", "arthur.ribeiro@email.com", "Goiânia", "GO", "(62) 0123-4567", 43.1,
        "Caio Menezes", "caio.menezes@email.com", "Florianópolis", "SC", "(48) 2345-6789", 12.3,
        "Alan Pereira", "alan.pereira@email.com", "Natal", "RN", "(84) 3456-7890", 76.9,
        "Douglas Melo", "douglas.melo@email.com", "Fortaleza", "CE", "(85) 4567-8901", 58.0,
        "Sergio Castro", "sergio.castro@email.com", "Salvador", "BA", "(71) 5678-9012", 38.7,
        "Marcelo Silva", "marcelo.silva@email.com", "Recife", "PE", "(81) 6789-0123", 24.9,
        "Gustavo Almeida", "gustavo.almeida@email.com", "Brasília", "DF", "(61) 8901-2345", 51.4,
        "Lucas Ferreira", "lucas.ferreira@email.com", "São Paulo", "SP", "(11) 0123-4567", 37.0,
        "Rafael Oliveira", "rafael.oliveira@email.com", "Rio de Janeiro", "RJ", "(21) 2345-6789", 80.2,
        "Thiago Gonçalves", "thiago.gonçalves@email.com", "Belo Horizonte", "MG", "(31) 3456-7890", 63.8,
        "Pedro Costa", "pedro.costa@email.com", "Curitiba", "PR", "(41) 4567-8901", 19.6)
)


# Aproveitamos o uso da TUPLA "()" em python para realizar comandos que serão lidos no SQL. 
conexao.commit()

# Comandos do editor do SQL (View -> SQL Editor): INSERT INTO produtos (nome, preco, qntd_estoque)
#                                                 VALUES ("coxinha", 8.00, 40)