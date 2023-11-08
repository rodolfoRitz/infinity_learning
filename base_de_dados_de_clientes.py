BASE_DE_DADOS_CLIENTES = [

    """
        BASE DE DADOS DE CLIENTES:
            Nesta base de dados você encontrará 100 registros contendo nomes, e-mails, cidades, estados,
            números de telefone e um saldo aleatório,  que devem ser utilizados para povoar o seu banco.
            Apesar de não haver o número de ID, é  FUNDAMENTAL criá-lo na tabela  do banco   de   dados.
            Para adicionar os registros no seu banco  de dados, você deve utilizar um gerador aleatório
            para que os dados sejam salvos em ordens aleatórias.

        DESCRIÇÃO/ESTRUTURA DOS REGISTROS:
            nome_completo:
                afinidade de coluna: str
            e-mail:
                afinidade de coluna: str
            cidade:
                afinidade de coluna: str
            estado:
                afinidade de coluna: str
            telefone:
                afinidade de coluna: str
            saldo:
                afinidade de coluna: float
        
        OBSERVAÇÕES:    
            Os 50 primeiros registros são masculinos; os demais, femininos.
    """
# A idéia principal é saparar os arquivos de 6 em 6, para depois usar uma estrutura de repetição (for, while) e inserir todos os clientes simultaneamente com um comando PYTHON. 
    "Lucas Silva", "lucas.silva@email.com", "São Paulo", "SP", "(11) 1234-5678", 78.5,
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
    "Pedro Costa", "pedro.costa@email.com", "Curitiba", "PR", "(41) 4567-8901", 19.6,
    "Ana Silva", "ana.silva@email.com", "São Paulo", "SP", "(11) 1234-5678", 58.3,
    "Maria Santos", "maria.santos@email.com", "Rio de Janeiro", "RJ", "(21) 2345-6789", 45.6,
    "Juliana Pereira", "juliana.pereira@email.com", "Belo Horizonte", "MG", "(31) 3456-7890", 72.4,
    "Beatriz Oliveira", "beatriz.oliveira@email.com", "Curitiba", "PR", "(41) 4567-8901", 37.2,
    "Camila Souza", "camila.souza@email.com", "Recife", "PE", "(81) 5678-9012", 63.9,
    "Larissa Rodrigues", "larissa.rodrigues@email.com", "Brasília", "DF", "(61) 8901-2345", 89.8,
    "Isabela Lima", "isabela.lima@email.com", "Manaus", "AM", "(92) 0123-4567", 47.1,
    "Renata Carvalho", "renata.carvalho@email.com", "Curitiba", "PR", "(41) 1234-5678", 24.5,
    "Laura Gomes", "laura.gomes@email.com", "Salvador", "BA", "(71) 2345-6789", 56.7,
    "Giovanna Barbosa", "giovanna.barbosa@email.com", "Florianópolis", "SC", "(48) 3456-7890", 75.3,
    "Amanda Rocha", "amanda.rocha@email.com", "Natal", "RN", "(84) 4567-8901", 49.8,
    "Caroline Azevedo", "caroline.azevedo@email.com", "Fortaleza", "CE", "(85) 5678-9012", 68.2,
    "Isabella Nunes", "isabella.nunes@email.com", "Recife", "PE", "(81) 6789-0123", 32.7,
    "Bruna Cunha", "bruna.cunha@email.com", "Belo Horizonte", "MG", "(31) 7890-1234", 61.9,
    "Bianca Ribeiro", "bianca.ribeiro@email.com", "São Paulo", "SP", "(11) 0123-4567", 41.6,
    "Letícia Cardoso", "leticia.cardoso@email.com", "Rio de Janeiro", "RJ", "(21) 2345-6789", 78.7,
    "Vanessa Costa", "vanessa.costa@email.com", "Manaus", "AM", "(92) 3456-7890", 53.0,
    "Mariana Vieira", "mariana.vieira@email.com", "Belém", "PA", "(91) 4567-8901", 84.1,
    "Heloísa Fonseca", "heloisa.fonseca@email.com", "Goiânia", "GO", "(62) 5678-9012", 67.4,
    "Natália Pereira", "natalia.pereira@email.com", "Curitiba", "PR", "(41) 6789-0123", 29.7,
    "Júlia Silva", "julia.silva@email.com", "Porto Alegre", "RS", "(51) 7890-1234", 45.2,
    "Fernanda Reis", "fernanda.reis@email.com", "Florianópolis", "SC", "(48) 0123-4567", 50.6,
    "Raquel Marques", "raquel.marques@email.com", "Natal", "RN", "(84) 2345-6789", 36.9,
    "Larissa Santos", "larissa.santos@email.com", "Salvador", "BA", "(71) 3456-7890", 69.3,
    "Gabriela Soares", "gabriela.soares@email.com", "Recife", "PE", "(81) 5678-9012", 57.8,
    "Eduarda Sampaio", "eduarda.sampaio@email.com", "Brasília", "DF", "(61) 6789-0123", 53.7,
    "Luana Barbosa", "luana.barbosa@email.com", "São Paulo", "SP", "(11) 7890-1234", 72.8,
    "Manuela Oliveira", "manuela.oliveira@email.com", "Rio de Janeiro", "RJ", "(21) 0123-4567", 45.5,
    "Alice Alves", "alice.alves@email.com", "Belo Horizonte", "MG", "(31) 2345-6789", 39.4,
    "Renata Teixeira", "renata.teixeira@email.com", "Belém", "PA", "(91) 3456-7890", 61.2,
    "Vitoria Fernandes", "vitoria.fernandes@email.com", "Goiânia", "GO", "(62) 5678-9012", 29.0,
    "Emanuela Duarte", "emanuela.duarte@email.com", "Curitiba", "PR", "(41) 6789-0123", 47.8,
    "Lívia Coelho", "livia.coelho@email.com", "Florianópolis", "SC", "(48) 7890-1234", 64.7,
    "Valentina Fernandes", "valentina.fernandes@email.com", "Natal", "RN", "(84) 0123-4567", 56.1,
    "Isadora Santos", "isadora.santos@email.com", "Fortaleza", "CE", "(85) 2345-6789", 42.9,
    "Marcella Lima", "marcella.lima@email.com", "Salvador", "BA", "(71) 3456-7890", 71.5,
    "Sophia Gonçalves", "sophia.goncalves@email.com", "Recife", "PE", "(81) 5678-9012", 54.3,
    "Larissa Ribeiro", "larissa.ribeiro@email.com", "Manaus", "AM", "(92) 6789-0123", 60.9,
    "Giovana Menezes", "giovana.menezes@email.com", "Belém", "PA", "(91) 0123-4567", 43.7,
    "Aline Pereira", "aline.pereira@email.com", "Porto Alegre", "RS", "(51) 2345-6789", 53.8,
    "Adriana Melo", "adriana.melo@email.com", "São Paulo", "SP", "(11) 3456-7890", 48.7,
    "Nathalia Castro", "nathalia.castro@email.com", "Rio de Janeiro", "RJ", "(21) 5678-9012", 59.6,
    "Fernanda Silva", "fernanda.silva@email.com", "Brasília", "DF", "(61) 7890-1234", 35.2,
    "Rafaela Almeida", "rafaela.almeida@email.com", "Belo Horizonte", "MG", "(31) 0123-4567", 67.8,
    "Letícia Ferreira", "leticia.ferreira@email.com", "Manaus", "AM", "(92) 2345-6789", 45.3,
    "Camila Oliveira", "camila.oliveira@email.com", "Belém", "PA", "(91) 3456-7890", 29.8,
    "Mariana Oliveira", "mariana.oliveira@email.com", "Goiânia", "GO", "(62) 5678-9012", 71.2,
    "Ana Oliveira", "ana.oliveira@email.com", "Florianópolis", "SC", "(48) 6789-0123", 63.7,
    "Julia Costa", "julia.costa@email.com", "Natal", "RN", "(84) 0123-4567", 49.0,
    "Bianca Santos", "bianca.santos@email.com", "Salvador", "BA", "(71) 2345-6789", 55.6
]

for items in BASE_DE_DADOS_CLIENTES:
    print(items)