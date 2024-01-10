def ex_01_09():
    """
    Defina uma variável do tipo lista (list) de números e preencha com 1 até 5. Em seguida, 
    utilize a função print para exibir os valores da variável.
    Utilize a função print para exibir o primeiro valor da lista, ou seja, o número 1.
    Utilize a função print para exibir o último valor da lista, ou seja, o número 5.
    Utilize a função print para exibir cada valor da lista separadamente. 
    Você pode fazer isso manualmente ou por meio do laço de repetição for.

    Utilize a função print para exibir o dobro de cada valor da lista separadamente.
    Uilize a função type combinada com a função print para exibir o tipo de dado da lista. 
    Na sequência, repita a mesma instrução para exibir o tipo de dado do elemento na 
    posição [2] da lista.
    Defina uma variável qualquer e atribua a ela o valor "AMOR".
    Utilize o laço de repetição for conforme o exemplo a seguir: for letra in palavra. 
    Utilize a função print para exibir os valores atribuídos à variável letra e faça 
    comentários sobre as saídas.
    Defina uma variável do tipo lista (list) e atribua a ela as letras 'A', 'M', 'O' e 'R', 
    todas maiúsculas. Na sequência, utilize o laço de repetição for e a função print 
    para exibir cada valor da lista separadamente.
    Defina uma variável do tipo lista (list) e atribua a ela as letras 'A', 'M', 'O' e 'R', 
    todas maiúsculas. Na sequência, utilize o laço de repetição for e a função print para 
    exibir cada valor da lista separadamente. No caso da função print, após chamar a variável 
    que será exibida, utilize o atributo end, conforme o exemplo a seguir: print(letra, end=""). 
    Comente a saída de dados (o que foi exibido na tela).
    """
    lista_1 = [1, 2, 3, 4, 5]
    lista_dobro = []

    print(lista_1)
    print(lista_1[0])
    print(lista_1[4])
    for items in lista_1:
        print(items, end=', ') #Por padrão o final do print tem um '\n', que pode ser editado pelo 'end='.
    
    for values in lista_1:
        lista_dobro.append(values * 2)
        print(lista_dobro)

    

ex_01_09()

def ex10_15():
    '''
    Atividade 10
    Crie um arquivo Python atividade10.py. Após, defina uma variável do tipo lista (list) e atribua a ela cinco
    palavras, sendo: "limão", "laranja", "maracujá", "abacaxi" e "mexerica". Depois, peça ao usuário que informe
    uma fruta, e atribua o valor lido a uma variável fruta. Finalmente, utilize a condicional if e verifique se a fruta
    informada pelo usuário faz parte da lista de frutas que você definiu anteriormente. Se verdadeiro, exiba o
    nome da fruta; caso contrário, informe ao usuário: "A fruta informada não está na lista". Dica: utilize o operador
    relacional in para resolver esse exercício.
    Atividade 11
    Crie um arquivo Python atividade11.py. Após, defina uma variável do tipo lista (list) e atribua a ela cinco
    notas, sendo: 9.9, 10, 7.1, 7.8. Em seguida, utilize o laço de repetição for para somar essas notas e, ao final,
    exibir ao usuário a média simples.
    Dica 1: a média simples é calculada a partir da soma dos valores divido pela quantidade desses valores.
    Assim, se temos quatro notas, a média será: (nota1 + nota 2 + nota3 + nota4) / 4.
    Dica 2: crie uma variável para que a soma seja armazenada. Assim, você utilizará o for apenas para somar. Ao
    final, utilize a função print e exiba a média ao usuário.
    Atividade 12
    A partir do arquivo criado na atividade anterior, crie um arquivo Python atividade12.py. Após, defina uma
    variável do tipo lista (list) e atribua a ela cinco notas, sendo: 9.9, 10, 7.1, 7.8. Em seguida, utilize o laço de
    repetição for para somar essas notas e, ao final, exibir ao usuário a média ponderada. Considere os seguintes
    pesos para cada nota, respectivamente: 4, 2, 3, 1.
    Atividade 13
    Crie um arquivo Python atividade13.py. Após, peça que o usuário informe uma palavra qualquer e armazene
    o valor lido em uma variável. Na sequência, utilize o laço for para verificar quantas vogais têm na palavra em
    questão. Ao final, exiba ao usuário a seguinte mensagem: print(f"A palavra {palavra} tem {quantidade}
    vogais.")
    Atividade 14
    Repita os procedimentos da atividade anterior em um arquivo Python atividade14.py. Dessa vez, utilize o
    algoritmo anterior para contar a quantidade de consoantes.
    Atividade 15
    Repita os procedimentos da atividade anterior em um arquivo Python atividade15.py. Após, peça que o
    usuário informe uma frase qualquer e armazene o valor lido em uma variável. Na sequência, utilize o laço for
    para verificar quantos espaços há na frase em questão. Ao final, exiba ao usuário a seguinte mensagem:
    print(f"A frase {frase} tem {quantidade} espaços.")
    '''
    p =1

#ex10_15()
