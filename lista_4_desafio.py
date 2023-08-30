def ex1_10():
    '''
    1. Faça a declaração de um dicionário vazio "pessoas".
    2. Adicione uma entrada no dicionário "pessoas" com a chave "nome" e o valor "João".
    3. Acesse o valor correspondente à chave "nome" no dicionário "pessoas".
    4. Adicione mais duas entradas no dicionário "pessoas" com as chaves "idade" e "cidade", e seus respectivos valores.
    5. Verifique se a chave "altura" existe no dicionário "pessoas".
    6. Remova a entrada com a chave "cidade" do dicionário "pessoas".
    7. Atualize o valor correspondente à chave "idade" para um novo valor por meio da sobrescrita. Na sequência, faça 
       o mesmo procedimento com o método reservado para esse fim descrito nas Tabela 1.
    8. Imprima todas as chaves do dicionário "pessoas".
    9. Imprima todos os valores do dicionário "pessoas".
    10. Imprima todas as chaves e valores do dicionário "pessoas" em pares.
    11. 
    12. 
    '''
    pessoas = {'nome':'João'}

    print(pessoas['nome'])
    pessoas.update({'idade':31, 'cidade':'Cabul'})
    print(pessoas)

    if 'altura' in pessoas:
        print(pessoas['altura'])
    else:
        print('Não há nenhuma chave "altura".')

    pessoas.pop('cidade')
    print(pessoas)

    pessoas.update({'idade': 45})
    print(pessoas)

    print(pessoas.keys())
    print(pessoas.values())

    for keys in pessoas:
        print(f'Chaves: {pessoas.keys()}'+'-'+f'Valores: {pessoas.values()}.')
#ex1_10()

def ex11_20():
    '''
    11. Faça a declaração de um dicionário "estoque" com três entradas: 
        "item1" com valor 10, "item2" com valor 5 e "item3" com valor 20.
    12. Calcule o total de itens no estoque.
    13. Verifique se o item "item2" está no estoque.
    14. Remova o item "item3" do estoque.
    15. Adicione um novo item ao estoque com chave e valor de sua escolha.
    16. Faça a declaração de um dicionário vazio "frutas".
    17. Adicione três entradas no dicionário "frutas" com as chaves sendo nomes de frutas e 
        os valores sendo as quantidades dessas frutas.
    18. Faça um comentário explicando a saída de dados.
    19. Caso a chave "banana" não exista, crie a chave e atribua a ela um valor qualquer. 
        Na sequência, incremente seu valor em uma quantidade.
    20. Verifique se o dicionário "frutas" está vazio.

    '''
    estoque = {'item1': 10, 'item2': 5, 'item3': 20}

    for value in estoque:
        total_itens = sum(estoque.values())
        print(total_itens)
    
    if 'item2' in estoque:
        print('Consta o item2.')
    else:
        print('Não consta o item2.')

    estoque.pop('item3')
    print(estoque)

    estoque.update({'item3': 80})
    print(estoque)

    frutas = {} #frutas.fromkeys()
    print(frutas)

    frutas.update({'uva': 4, 'maca': 2, 'banana': 8})
    print(frutas)

    print(frutas['banana'])
    print('A saída de dados ou exibição, no dicionário é feita for meio da chamada do dicionário e em seguida')
    print('informando a chave que se quer obter o valor ou o valor da chave que está buscando.')

    for keys in frutas:
        if 'banana' in frutas:
            print(f"A chave 'banana' existe. E seu valor é: {frutas.get('banana')}")
            frutas.update({'banana': 4})
            print(frutas.get('banana'))
        else:
            frutas.update({'banana': 3})
            print("Não existe a chave informada, desta forma será criada uma nova chave 'banana'")
            print(frutas.get('banana'))

        print(frutas.items())
#ex11_20()

def ex21_25():
    '''
    Exercício 21
    Crie um arquivo Python exercicio21.py. Após, faça a declaração de um dicionário "notas" com cinco entradas,
    em que as chaves são nomes de alunos e os valores são suas respectivas notas.
    Exercício 22
    A partir do exercício desenvolvido anteriormente, crie um arquivo Python exercicio22.py. Após, calcule a
    média das notas dos alunos.
    Dica: lembre dos exercícios anteriores e de como fizemos para calcular somar itens a partir do laço de
    repetição for. É desejável o uso do laço para resolução desse exercício.
    Exercício 23
    A partir do exercício desenvolvido anteriormente, crie um arquivo Python exercicio23.py. Após, encontre o
    aluno com a nota mais alta no dicionário "notas".
    Dica: lembre dos exercícios anteriores e de como fizemos para calcular somar itens a partir do laço de
    repetição for. É desejável o uso do laço para resolução desse exercício.
    Exercício 24
    A partir do exercício desenvolvido anteriormente, crie um arquivo Python exercicio24.py. Após, remova o
    aluno com a nota mais baixa do dicionário "notas".
    Dica 1: lembre dos exercícios anteriores e de como fizemos para calcular somar itens a partir do laço de
    repetição for. É desejável o uso do laço para resolução desse exercício. Dica 2: utilize o método reservado
    para esse fim descrito na Tabela 1.
    Exercício 25
    A partir do exercício desenvolvido anteriormente, crie um arquivo Python exercicio24.py. Após, verifique se
    um aluno chamado "Maria" está presente no dicionário "notas".
    '''
    notas = {'pedro': 10, 'ana': 50, 'joao': 70, 'maria': 80, 'estevao': 99}

    for values in notas:
        media = sum(notas.values()) / 5
        print(media)

    for values in notas:
        maior_nota = max(notas, key=notas.get)
        print(maior_nota)

    #Nesta parte precisei remover o laço FOR pois ocorria um erro de iteração.
    menor_nota = min(notas, key=notas.get)
    print(menor_nota)
    del notas[menor_nota]
    print(notas)

    if 'maria' in notas:
        print(f"A chave 'maria' está no dicionário e seu valor é: {notas.get('maria')}")
#ex21_25()

def ex26_30():
    '''
    26. Faça a declaração de um dicionário "agenda" com três entradas, em que as chaves são nomes de pessoas e 
        os valores são seus respectivos números de telefone.
    27. Adicione uma entrada com a chave "Pedro" e o valor do número de telefone correspondente.
    28. Imprima todos os nomes de pessoas na agenda.
    29. Imprima todos os números de telefone na agenda.
    30. Remova todas as entradas da agenda. Na sequência, utilize a função print para exibir o dicionário 
        após a remoção dos valores.
        Dica: utilize o método reservado para esse fim descrito na Tabela 1.
    '''
    agenda = {'joao': 31986589234, 'maria': 31934534335, 'ana': 5532996546743}

    agenda.update({'pedro': 31934534534})
    print(agenda.keys())
    print(agenda.values())
    agenda.clear()
    print(agenda)
#ex26_30()

def sistema_v0_1():
    '''
    Crie um dicionário a partir das listas declaradas. Finalmente, crie um pequeno algoritmo que:
    a) Uma vez informado um valor a partir da função input(), verifique se esse valor é uma chave do dicionário.
    b) Caso o valor informado anteriormente esteja no dicionário, retorne a seguinte saída de dados: 
        "Produto: {nome_produto}.
        Valor: R$ {valor_produto}."
    c) Caso o valor informado anteriormente não esteja no dicionário, pergunte ao usuário se ele deseja
        adicioná-lo.
    d) Caso o usuário informe que deseja adicionar um novo produto ao dicionário, pergunte o nome do produto e
        qual o valor (preço em R$).
    e) Caso o usuário informe que não deseja adicionar um novo produto ao dicionário, retorne a lista de produtos
        e seus respectivos valores formatada conforme a saída de dados do item (b) do desafio.
    f) Após exibir a lista de produtos e de valores do dicionário, pergunte ao usuário se ele deseja atualizar o valor
        de algum produto. Se positivo, pergunte qual o valor será atualizado, faça a atualização do valor e 
        exiba a lista atualizada formatada conforme o item (b) do desafio. Se negativo, encerre.
    '''
    itens = ["Celular", "Batedeira", "Televisão", "Notebook", "Aparelho DVD"]
    valores = [1000.0, 350.0, 3450.0, 6700.00, 200.0]

    atacado = dict(zip(itens, valores))
    print(f'Estes são seus produtos: {atacado}')

    user_input = input('Digite um valor: ')
    if user_input in atacado:
        print(f'Produto: {user_input} \nValor: {atacado[user_input]}')
    else:
        question = input('Você deseja adicionar um produto? (S/N)')
        if question == 's' or question == 'S':
            new_iten = input('Digite o nome do produto: ')
            new_value = input('Digite o valor do produto: ')
            atacado.update({new_iten: new_value})
            print(f'Estes são seus produtos: {atacado}')

        if question == 'n' or question == 'N':
            print(f'Produtos: {atacado.keys()} \nValores: {atacado.values()}')
            question2 = input('Você deseja atualizar o valor de algum produto? (S/N)')
            if question2 == 'S' or question2 == 's':
                question3 = input('O valor de qual produto? ')
                question4 = input('Qual será o novo valor? ')
                atacado.update({question3: question4})
            print(f'Estes são seus produtos: {atacado}')
            if question2 == 'N' or question2 == 'n':
                print('Exiting program...')

sistema_v0_1()
