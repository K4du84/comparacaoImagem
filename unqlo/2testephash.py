import hashlib
from glob import glob
import numpy as np
import os
from PIL import Image
import imagehash
import cv2
import hashlib
import pathlib

os.rename("C:\\ImageBD\\HORSErenomeado.jpg","C:\\ImageBD\\HORSE1c.jpg")


index = {}  # Armazenar o nome da imagem e os histogramas
images = {}  # Armezar as próprias imagens

# Pegar as imagens na pasta
i = 0
hashes = {}
img_names = glob(os.path.join(os.getcwd(),'*.jpg'))
for fn in img_names:
    print("Arquivo ", i + 1, " - ", img_names[i])
  #  print("Hash - ", hash(img_names[i]))
  #  print(len(str(hash(img_names[i]))))
  #  print("Average Hash -", imagehash.average_hash(Image.open(img_names[i])))
  #  print(len(imagehash.average_hash(Image.open(img_names[i]))))
    hashes[i] = imagehash.whash(Image.open(img_names[i]))
    print("Wash Hash - ", imagehash.whash(Image.open(img_names[i])))
    print(len(imagehash.whash(Image.open(img_names[i]))))
    i += 1

#Figura 3 do array é a modelo HORSE_MODEL
#Figura 0 do array é a identica ao modelo HORSE1
print("-------------------------------------")
print("RESULTADO uniqlo_grey_hoodie MENOS uniqlo_jacket ",hashes[2], "/",hashes[0])
print(hashes[2]-hashes[0])
print("RESULTADO uniqlo_grey_hoodie MENOS uniqlo_black_wrap ",hashes[2], "/",hashes[1])
print(hashes[2]-hashes[1])
print("RESULTADO uniqlo_jacket MENOS uniqlo_black_wrap ",hashes[0], "/",hashes[1])
print(hashes[0]-hashes[1])

