# código para obtenção da porcentagem de semelhança entre as imagens analisadas

from PIL import Image
import imagehash


first_hash = imagehash.whash(Image.open("C:\\ImageBD\\unqlo\\HORSE_MODEL.jpg"))
second_hash = imagehash.whash(Image.open("C:\\ImageBD\\HORSE1.jpg"))
size = len(first_hash)

similarity = 100 - (((first_hash - second_hash) / size) * 100)

print("-------------------------------------")
print("A semelhança entre as imagens é de : ", similarity , "%")
print("-------------------------------------")
