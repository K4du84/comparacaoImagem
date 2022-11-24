import pathlib
from glob import glob
import os

i = 0
img_names = glob(os.path.join(os.getcwd(), '*.*'))
for fn in img_names:
    file_extension = pathlib.Path(img_names[i]).suffix
    print("Arquivo ", i+1, "- ", img_names[i])
    print("File Extension: ", file_extension)

    if file_extension != ".jpg":
        print()
        print("Extensão inválida, por favor incluia arquivo com extensão .jpg")
    else:
        print("Arquivo válido!")
    i += 1
