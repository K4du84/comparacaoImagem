#VALIDAÇÃO DA EXTENSÃO DO ARQUIVO DA IMAGEM A SER SALVA

import pathlib
from glob import glob
import os

i = 0
img_names = glob(os.path.join("C:\\ImageBD", '*.*'))
for fn in img_names:
    file_extension = pathlib.Path(img_names[i]).suffix
    print("Arquivo ", i + 1, "- ", img_names[i])
    print("File Extension: ", file_extension)

    if (file_extension == ".jpg") or (file_extension == ".jpeg"):
        print("Arquivo válido!")
    else:
        print("Extensão inválida, por favor incluia arquivo com extensão .jpg")
    i += 1
