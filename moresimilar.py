#BIBLIOTECAS
from glob import glob
import os
from PIL import Image
import imagehash


# PROGRAMA COM FINALIDADE DE RETORNAR A IMAGEM MAIS SEMELHANTE DO BANCO DE DADOS COM A IMAGEM PASSADA PELO USUÁRIO
i = 0
hashes = {}

# DEFINIÇÃO DAS INFORMAÇÕES DA IMAGEM MODELO, QUE QUEREMOS COMPARAR COM O BANCO DE DADOS.
model = "C:\\ImageBD\\unqlo\\HORSE_MODEL.jpg"
hash_model = imagehash.whash(Image.open(model))
size = len(hash_model)

# ALIMENTAÇÃO DA LISTA COM OS ARQUIVOS DO BANCO DE DADOS
img_names = glob(os.path.join("C:\\ImageBD", '*.jpg'))
print("")
# IMPRESSÕES REALIZADAS APENAS PARA ACOMPANHARMOS O PROCESSO QUE ESTAVA SENDO FEITO
#print("LISTA COMPLETA")
for fn in img_names:
   # print("Arquivo ", i + 1, " - ", img_names[i])
    # ACHEI MELHOR JÁ ALIMENTAR A LISTA JÁ COM A SIMILARIDADE CALCULADA
    hashes[i] = 100 - (((hash_model - imagehash.whash(Image.open(img_names[i])))/ size) * 100)
   # print("Similaridade Hash ", i + 1, " - ", hashes[i])
    i += 1

#CRIAÇÃO DO LOOP PARA IDENTIFICAR A MAIOR SIMILARIDADE E A QUE ARQUIVO PENTENCE
j = 0
more_similar = 0
similar_file = None

for hs in hashes:
    if hashes[j] > more_similar:
        more_similar = hashes[j]
        similar_file = img_names[j]
        j += 1
print("")
print("________________________")
print("")
print("A Imagem mais similar é a", similar_file, ",com ", more_similar, "% de similaridade.")
print("")
print("________________________")
print("")


