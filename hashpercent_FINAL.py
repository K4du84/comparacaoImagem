# código para obtenção da porcentagem de semelhança entre as imagens analisadas
from glob import glob
import os
from PIL import Image
import imagehash


# Pegar as imagens jpg na pasta e verificar a Hash e o tamanho dela
i = 0
hashes = {}
tamanho = {}
img_names = glob(os.path.join(os.getcwd(),'*.jpg'))
for fn in img_names:
    print("Arquivo ", i + 1, " - ", img_names[i])
    hashes[i] = imagehash.whash(Image.open(img_names[i]))
    print("Wash Hash - ", hashes[i])
    tamanho[i] = len(hashes[i])
    print(tamanho[i])
    i += 1
#CALCULO DA DIFERENÇA ENTRE AS HASH
"""""""COMO O CALCULO DA DIFERENÇA DO HASH VARIA DE 0 A 100, ONDE ZERO SIGNIFICA QUE É MAIS SEMELHANTE, " \
"PARA TERMOS O RETORNO EM PORCENTAGEM É NECESSÁRIO FORMATAR O RESULTADO -- 100 - (((HASH1 - HASH2)/ LEN DO HASH) * 100)"""
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
print("A semelhança entre as imagens é de : ", 100-(((hashes[4]-hashes[4])/tamanho[4])*100) , "%")
