from collections import Counter
import pandas as pd

# Teste Inicial:
# home, busca,logado ==> comprou

data_frame = pd.read_csv('busca.csv')
#data_frame = pd.read_csv('buscas2.csv')

X_df = data_frame[['home','busca','logado']]
Y_df = data_frame['comprou']

Xdummies_df = pd.get_dummies(X_df)
Ydummies_df = Y_df

X = Xdummies_df.values
Y = Ydummies_df.values

porcentagem_treino = 0.9

tamanho_de_treino = int(porcentagem_treino * len(Y))
tamanho_de_teste  = len(Y) - tamanho_de_treino

treino_dados     = X[:tamanho_de_treino]
treino_marcacoes = Y[:tamanho_de_treino]

teste_dados     = X[-tamanho_de_teste:]
teste_marcacoes = Y[-tamanho_de_teste:]

def fit_and_predict(modelo, origem, treino_dados, treino_marcacoes, teste_dados, teste_marcacoes):
    modelo.fit(treino_dados, treino_marcacoes)

    resultado  = modelo.predict(teste_dados)

    diferencas = resultado - teste_marcacoes

    acertos = [ d for d in diferencas if d == 0  ]

    total_de_acertos   = len(acertos)
    total_de_elementos = len(teste_dados)

    taxa_de_acertos = 100.0 * total_de_acertos / total_de_elementos

    print('Minha taxa de acertos utilizando {} foi {} % \n'.format(origem, taxa_de_acertos))
    print('   Meu total de acertos foi {} registros do universo total de {} registros'.format(total_de_acertos, tamanho_de_teste))

    # Eficiencia do algoritmo que chuta tudo 1 ou 0 - Algoritmo Base
    acerto_base = max(Counter(teste_marcacoes).itervalues())
    tx_acerto_base = 100.0 * acerto_base / len(teste_marcacoes)
    print('   Taxa de acertos do Algoritmo Base {} % \n'.format(tx_acerto_base))



from sklearn.naive_bayes import MultinomialNB
modelo = MultinomialNB()
fit_and_predict(modelo, 'MultinomialNB', treino_dados, treino_marcacoes, teste_dados, teste_marcacoes)


from sklearn.ensemble import AdaBoostClassifier
modelo = AdaBoostClassifier()
fit_and_predict(modelo, 'AdaBoostClassifier', treino_dados, treino_marcacoes, teste_dados, teste_marcacoes)


