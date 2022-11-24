from glob import glob
import os
from PIL import Image
import imagehash


# Pegar as imagens jpg na pasta e verificar a Hash e o tamanho dela
i = 0
j = 0
h = 0
hashes = {}

#DEFINIÇÃO DAS INFORMAÇÕES DA IMAGEM MODELO, A QUE QUEREMOS COMPARAR COM O BANCO DE DADOS.
modelo = "C:\\ImageBD\\unqlo\\HORSE_MODEL.jpg"
hash_modelo = imagehash.whash(Image.open(modelo))
tamanho = len(hash_modelo)

# print("Hash = ", hash_modelo)

img_names = glob(os.path.join(os.getcwd(), '*.jpg'))
print("")
print("LISTA COMPLETA")
for fn in img_names:
    print("Arquivo ", i + 1, " - ", img_names[i])
    #hashes[i] = imagehash.whash(Image.open(img_names[i]))
    hashes[i] = 100 - (((hash_modelo - imagehash.whash(Image.open(img_names[i])))/ tamanho) * 100)
    print("Similaridade Hash ", i + 1, " - ", hashes[i])
    #if img_names[i] == modelo:
       # del (img_names[i])
        #del (hashes[i])
    i += 1

mais_similar = 0
arquivo_similar = None
print("tamanho lista hash = ", len(hashes))
for hs in hashes:
    if hashes[j] > mais_similar:
        mais_similar = hashes[j]
        arquivo_similar = img_names[j]
        j += 1
print("")
print("________________________")
print("A Imagem mais similar é a ",arquivo_similar, "com ", mais_similar, "% de similaridade.")



#lista_pesquisa = img_names
#hash_pesquisa = hashes

"""print("")
print("LISTA MENOS MODELO")
for lpesq in lista_pesquisa:
    print("Arquivo ", j + 1, " - ", lista_pesquisa[j])
    print("Arquivo ", j + 1, " - ", hash_pesquisa[j])
    j += 1

print("Maior Semelhança foi de : ", max(float(hash_pesquisa)))
#hash_mais_semelhante = 0.0
#arquivo_mais_semelhante = None"""

#for compare in lista_pesquisa:
    #resultado = 100 - (((hash_modelo - hashes[h]) / tamanho) * 100)
   # print("Resultado = ", resultado)
   # if resultado > hash_mais_semelhante:
       # hash_mais_semelhante = hashes[h]
       # arquivo_mais_semelhante = lista_pesquisa[h]
       # h += 1

#print("Arquivo Mais Semelhante = ", arquivo_mais_semelhante)
#print("com ", hash_mais_semelhante, " % de semelhança")

"""img_names = glob(os.path.join(os.getcwd(),'*.jpg'))
for fn in img_names:
    print("Arquivo ", i + 1, " - ", img_names[i])
    hashes[i] = imagehash.whash(Image.open(img_names[i]))
    print("Wash Hash - ", hashes[i])
    tamanho[i] = len(hashes[i])
    print(tamanho[i])   
    i += 1
#CALCULO DA DIFERENÇA ENTRE AS HASH
#Figura 4 do array é a modelo HORSE_MODEL
#Figura 0 do array é a identica ao modelo HORSE1
print("-------------------------------------")
print("RESULTADO MODELO MENOS FIGURA 1 ",hashes[4], "/",hashes[0])
print(hashes[4]-hashes[0])
print("A semelhança entre as imagens é de : ", 100-(((hashes[4]-hashes[0])/tamanho[4])*100) , "%")
print("-------------------------------------")
print("RESULTADO MODELO MENOS FIGURA 2 ",hashes[4], "/",hashes[1])
print(hashes[4]-hashes[1])
print("A semelhança entre as imagens é de : ", 100-(((hashes[4]-hashes[1])/tamanho[4])*100) , "%")
print("-------------------------------------")
print("RESULTADO MODELO MENOS FIGURA 3 ",hashes[4], "/",hashes[2])
print(hashes[4]-hashes[2])
print("A semelhança entre as imagens é de : ", 100-(((hashes[4]-hashes[2])/tamanho[4])*100) , "%")
print("-------------------------------------")
print("RESULTADO MODELO MENOS FIGURA 4 ",hashes[4], "/",hashes[3])
print(hashes[4]-hashes[3])
print("A semelhança entre as imagens é de : ", 100-(((hashes[4]-hashes[3])/tamanho[4])*100) , "%")
print("-------------------------------------")
print("RESULTADO MODELO MENOS MODELO ",hashes[4], "/",hashes[4])
print(hashes[4]-hashes[4])
print("A semelhança entre as imagens é de : ", 100-(((hashes[4]-hashes[4])/tamanho[4])*100) , "%")"""
