import nltk

base = [('eu sou admirada por muitos','alegria'),
        ('me sinto completamente amado','alegria'),
        ('amar e maravilhoso','alegria'),
        ('estou me sentindo muito animado novamente','alegria'),
        ('eu estou muito bem hoje','alegria'),
        ('que belo dia para dirigir um carro novo','alegria'),
        ('o dia est� muito bonito','alegria'),
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

stop_words = ['a', 'agora', 'algum', 'alguma', 'aquele', 'aqueles', 'de', 'deu', 'do', 'e', 'estou', 'esta', 'esta',
             'ir', 'meu', 'muito', 'mesmo', 'no', 'nossa', 'o', 'outro', 'para', 'que', 'sem', 'talvez', 'tem', 'tendo',
             'tenha', 'teve', 'tive', 'todo', 'um', 'uma', 'umas', 'uns', 'vou']

nltk.download('stopwords')

stop_words_nltk = nltk.corpus.stopwords.words("portuguese")

def remove_stop_words(text):
    frases = []
    for palavras,emocao in text:
        sem_stop = [p for p in palavras.split() if p not in stop_words_nltk]
        frases.append((sem_stop,emocao))
    return frases

def aplicar_stemmer(text):
    stemmer = nltk.stem.RSLPStemmer()
    frases_stemmer = []
    for palavras,emocao in text:
        com_steming = [str(stemmer.stem(p)) for p in palavras.split() if p not in stop_words_nltk]
        frases_stemmer.append((com_steming,emocao))
    return frases_stemmer

def busca_palavras(frases):
    todas_palavras = []
    for palavras,emocao in frases:
        todas_palavras.extend(palavras)
    return todas_palavras

def busca_frequencia(palavras):
    palavras = nltk.FreqDist(palavras)
    return palavras

def busca_palavras_unicas(frequencia):
    freq = frequencia.keys()
    return freq

def extrator_palavras(documento):
    doc = set(documento)
    caracteristicas = {}
    for palavras in palavras_unicas:
        caracteristicas["%s" % palavras] = (palavras in doc)
    return caracteristicas

frases_com_stemming = aplicar_stemmer(base)
palavras = busca_palavras(frases_com_stemming)
frequencia = busca_frequencia(palavras)
palavras_unicas = busca_palavras_unicas(frequencia)
caracteristicas_frase = extrator_palavras(["am","nov","dia"])
base_completa = nltk.classify.apply_features(extrator_palavras,frases_com_stemming)