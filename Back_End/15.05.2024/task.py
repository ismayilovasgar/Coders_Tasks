# Salam,hərvaxtınız xeyir.
# 1) taskınız ilk olaraq bir text faylı yaradıb içərisinə istədiyiniz bir cümlə yazırsınız .
# 2) daha sonra həmin textin ilk sətrindəki  sözlərin bütün hərflərini böyük hərflərə çeviririk .
# 3) Ən sonda bu sözləri başqa  bir text faylı yaradıb onun içərisində yazırıq.

import os

text_content = """lorem ipsum, dolor sit amet consectetur 
adipisicing elit. Illo harum,suscipit esse asperiores 
praesentium quae ex pariatur, possimus at exercitationem 
eius dolores voluptatum laudantium nesciunt unde 
labore dolorem iusto explicabosoluta velit autem quaerat dicta!
"""
path_1 = os.path.dirname(__file__) + "/new_txt_1.txt"
path_2 = os.path.dirname(__file__) + "/new_txt_2.txt"

with open(path_1, encoding="utf-8", mode="w+") as data:
    data.write(text_content)
    data.seek(0)
    ilk_setir = [i.upper() for i in data.readlines()][0]


with open(path_2, encoding="utf-8", mode="w") as data:
    data.write(ilk_setir)
