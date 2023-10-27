import nltk
# nltk.download()

# texto = "Nessa videoaula você será apresentado a noções introdutórias sobre a  biblioteca NLTK (Natural Language Toolkit) em Python para Processamento de Linguagem Natural. Confira o passo a passo dos recursos básicos dessa biblioteca para você iniciar o estudo nessa área. A aula faz parte do curso 'Mineração de Emoção em Texto com Python e NLTK' que está disponível para assinantes IA Expert Academy. "

# # frases = nltk.tokenize.sent_tokenize(texto, language='portuguese')
# # for i in frases:
# #     print(i)

# tokens = nltk.word_tokenize(texto, language='portuguese')
# # for i in tokens:
# #     print(i)

# classes = nltk.pos_tag(tokens)
# # for i in classes:
# #     print(i)

# entidades = nltk.ne_chunk(classes)
# print(entidades)

base = [('eu sou admirada por muitos','alegria'),
        ('me sinto completamente amado','alegria'),
        ('amar e maravilhoso','alegria'),
        ('estou me sentindo muito animado novamente','alegria'),
        ('eu estou muito bem hoje','alegria'),
        ('que belo dia para dirigir um carro novo','alegria'),
        ('o dia esta muito bonito','alegria'),
        ('estou contente com o resultado do teste que fiz no dia de ontem','alegria'),
        ('o amor e lindo','alegria'),
        ('nossa amizade e amor vai durar para sempre', 'alegria'),
        ('estou amedrontado', 'medo'),
        ('ele esta me ameacando a dias', 'medo'),
        ('isso me deixa apavorada', 'medo'),
        ('este lugar e apavorante', 'medo'),
        ('se perdermos outro jogo seremos eliminados e isso me deixa com pavor', 'medo'),
        ('tome cuidado com o lobisomem', 'medo'),
        ('se eles descobrirem estamos encrencados', 'medo'),
        ('estou tremendo de medo', 'medo'),
        ('eu tenho muito medo dele', 'medo'),
        ('estou com medo do resultado dos meus testes', 'medo')]

stopwords = ['a', 'agora', 'algum', 'alguma', 'aquele', 'aqueles', 'de', 'deu', 'do', 'e', 'estou', 'esta', 'esta',
             'ir', 'meu', 'muito', 'mesmo', 'no', 'nossa', 'o', 'outro', 'para', 'que', 'sem', 'talvez', 'tem', 'tendo',
             'tenha', 'teve', 'tive', 'todo', 'um', 'uma', 'umas', 'uns', 'vou']

stopwordsNLTK = nltk.corpus.stopwords.words('portuguese')
print(stopwordsNLTK)
# def removeStopWords(texto):
#     frases = []
#     for (palavras, emocao) in texto:
#         semStop = [p for p in palavras.split() if p not in stopwords]
#         frases.append((semStop, emocao))
#     return frases

