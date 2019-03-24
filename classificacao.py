# Caracteristicas:
    # eh gordinho?
    # tem perna curta?
    # faz auau?

porquinho1 = [1, 1, 0]
porquinho2 = [1, 1, 0]
porquinho3 = [1, 1, 0]

cachorrinho1 = [1, 1, 1]
cachorrinho2 = [0, 1, 1]
cachorrinho3 = [0, 1, 1]

# Dados

dados = [
         porquinho1, porquinho2, porquinho3,
         cachorrinho1, cachorrinho2, cachorrinho3
]

# marcacoes:
   #  1 => porco
   # -1 => cao
marcacoes = [1, 1, 1, -1, -1, -1]
#marcacoes = [ 'Porco', 'Porco', 'Porco', 'Cao', 'Cao', 'Cao']

from sklearn.naive_bayes import MultinomialNB

modelo = MultinomialNB()

modelo.fit(dados, marcacoes)  # Treina o algoritmo com os dados e com as marcacoes

# animais que deseja se saber a origem

misterioso1 = [1, 1, 1]
misterioso2 = [1, 0, 0]
misterioso3 = [0, 0, 1]

# coloca todos os animais no array para se verificar
animais_misteriosos = [misterioso1, misterioso2, misterioso3]

# Resultado que eu espero que seja
marcacoes_teste = [-1, 1, -1]

# resultado da analise
resultado = modelo.predict(animais_misteriosos)

# Diferenca entre o resultado obtido do resultado que eu esperava que seria
diferencas = resultado - marcacoes_teste

#print("Meu resultado foi: {}".format(resultado))
#print("Minha Diferenca e {}".format(diferencas))

# analisa a diferenca entre o esperado e o obtido,
# adicionando no array os valores que "cruzados", ou seja, os valores que bateram
acertos = [ d for d in diferencas if d == 0 ]

total_de_acertos = len(acertos)
total_de_elementos_analisados = len(animais_misteriosos)

taxa_de_acerto = 100.0 * (total_de_acertos / total_de_elementos_analisados)

print("Meu acerto total da analise foi {} do universo de {} elementos, com o percentual de {} % de acerto".format(total_de_acertos, total_de_elementos_analisados, taxa_de_acerto))


