# Alqoritmik Task
# Bir olimpiyadadır və burada iştirakçılar müxtəlif xallar qazanır.
# Biz isə onların topladığı xallara görə neçənci yeri tutduğunu print etməliyik.
# Misal üçün bizə xallar verilib. xallar = [5,3,4,2,1].
# Tutduğu yerlər də qazandıqları xalların sırasına uyğun sıralanacaq.  yerlər=['1-ci','3-cu','2-ci','4-cu','5-ci']
# Sortdan istifadə etdikdə xalların sırası pozulacağı üçün yerlər də o pozulmuş sıraya uyğun sıralanacaq və nəticə  düzgün olmayacaq.
# (taskı daha da asanlaşdırmaq üçün hərkəsin  xalı müxtəlif olacaq. Eyni xala sahib 2 şəxs olabilməz)
# Verilmiş xallara uyğun tutduğu yerləri gətirən bir funksiya yazın.


def find_order(my_list: list[int]) -> list[str]:
    result = [
        i[1] for i in sorted(enumerate(my_list), key=lambda x: x[1], reverse=True)
    ]
    return [str(result.index(i) + 1) + "-cu" for i in my_list]


my_list = [2, 4, 5, 3, 1]
print(find_order(my_list))