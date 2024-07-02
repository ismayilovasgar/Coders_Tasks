def samitleri_al(cumle):
    saitler = ["a", "e", "i", "o", "u"]
    return [i for i in cumle if i.isalpha() and i.lower() not in saitler]
