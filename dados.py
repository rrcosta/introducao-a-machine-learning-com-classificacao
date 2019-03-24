import csv

def carregar_acessos():
    X = []
    Y = []

    arquivo = open('acesso.csv', 'rb')
    leitor = csv.reader(arquivo)

    leitor.next() # Ignora a primeira linha

    for home, como_funciona, contato, comprou in leitor:
        X.append([int(home), int(como_funciona), int(contato)])
        Y.append([int(comprou)])

    arquivo.close()

    return X, Y

def carregar_buscas():
    X = []
    Y = []

    arquivo = open('busca.csv','rb')
    leitor = csv.reader(arquivo)
    leitor.next()

    for home, busca, logado, comprou in leitor:
        dado = [int(home), busca, int(logado)]

        X.append(dado)
        Y.append(int(comprou))

    arquivo.close()
    return X, Y
