#
#* 1). Userden alinan 5 cavabi bir listde sirali seklinde yerlesdirin:
# Userden alinan 5 cavabi bir listde sirali seklinde yerlesdirin:
# [4,1,78,99,45] >> [1,4,45,78,99]

#* 2). Daxil edilmiş cümlənin bütün sözlərini alfabetik düzülüşlü sözlərə
#  çevirib nəticəni çap edin. Misal üçün ."sabahin xeyir". 
#  Bu şəkildə olacaq  : "abhins exiry".Hər bir sözdəki hərflər alfabetik sırasına görə düzüldü. 

#* 3.)Tutaq ki, n=13. istifadəçi bu n ededini inputda  daxil edənə qədər input alın ve 13 daxil etdikdə 
# desin ki, məsələn 5 cəhdə tapdız, yəni, neçə cəhdə tapdığını print etsin. while istifade edin . 
# Aşağıdakı inputlarlardakı dəyərlər sadəcə nümunədir. 
# ilk input== 4   
# ikinci input == 7
# ucuncu input == 2
# dorduncu input == 13
# tebrikler . 4 cehdde 13 reqemeni tapdiz

#* 4). 1 ile 100 arasinda sade ededleri print edin. (for loops)

#####################################################################################################

#*Task-1
# my_list=[]
# for i in range(1,6):
#     my_list.append(int(input(f"{i}. ededi daxil edin...")))
# my_list.sort()
# print(f"siralanmis list:{my_list}")


#*Task-2
# cumle=input("cumle daxil edin:").strip()

# soz_reverse=""
# for i in cumle.split(" "):
#     soz_reverse += "".join(sorted(i))
#     soz_reverse+=" "
# print(soz_reverse)
#demo


#*Task-3
# m=13
# daxil_olunanlar=[]
# while True:
#     eded=int(input("eded daxil edin:"))
#     daxil_olunanlar.append(eded)
#     if m == eded:
#         j =len(daxil_olunanlar)
#         print(f"\n{j} cehdde tapdiz !")
#         for i in range(j):
#             print(f"{i+1}-nci cehd: {daxil_olunanlar[i]} ")
#         break



#*Task-4
# sade_ededler=[]
# for i in range(1,101):
#     count = 0

#     for j in range(1,i+1):
#         if i % j == 0:
#             count+=1
        
#     if count == 2:
#         sade_ededler.append(i)
#         print(i)

# print(f"sade ededer:{sade_ededler}")

    
    
         
    