#BIBLIOTECAS
from glob import glob
import os
from PIL import Image
import imagehash


# PROGRAMA COM FINALIDADE DE RETORNAR A IMAGEM MAIS SEMELHANTE DO BANCO DE DADOS COM A PASSADA PELO USUÁRIO
i = 0
hashes = {}

# DEFINIÇÃO DAS INFORMAÇÕES DA IMAGEM MODELO, QUE QUEREMOS COMPARAR COM O BANCO DE DADOS.
modelo = "C:\\ImageBD\\unqlo\\BLACK_HORSE.jpg"
hash_modelo = imagehash.whash(Image.open(modelo))
tamanho = len(hash_modelo)

# ALIMENTAÇÃO DA LISTA COM OS ARQUIVOS DO BANCO DE DADOS
img_names = glob(os.path.join(os.getcwd(), '*.jpg'))
print("")
# IMPRESSÕES REALIZADAS APENAS PARA ACOMPANHARMOS O PROCESSO QUE ESTAVA SENDO FEITO
print("LISTA COMPLETA")
for fn in img_names:
    print("Arquivo ", i + 1, " - ", img_names[i])
    # ACHEI MELHOR JÁ ALIMENTAR A LISTA JÁ COM A SIMILARIDADE CALCULADA
    hashes[i] = 100 - (((hash_modelo - imagehash.whash(Image.open(img_names[i])))/ tamanho) * 100)
    print("Similaridade Hash ", i + 1, " - ", hashes[i])
    i += 1

#CRIAÇÃO DO LOOP PARA IDENTIFICAR A MAIOR SIMILARIDADE E A QUE ARQUIVO PENTENCE
j = 0
mais_similar = 0
arquivo_similar = None

#print("tamanho lista hash = ", len(hashes))
for hs in hashes:
    if hashes[j] > mais_similar:
        mais_similar = hashes[j]
        arquivo_similar = img_names[j]
        j += 1
print("")
print("________________________")
print("")
print("A Imagem mais similar é a", arquivo_similar, ",com ", mais_similar, "% de similaridade.")
print("")
print("________________________")
print("")


