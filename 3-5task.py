# 1.) verilmiş listdəki ədədlərin hansılarının hər hansı bir ədədin kvadratı olduğunu define funksiyasında yazıb və listin içərisində ekrana çıxarın. 
# mylist=[-4,-16,0,1,4,5,9,16,25,36,49,64,81,100]


# import math
# def kokAlma(mylist):
#     newlist=[]
#     for i in mylist:
#         if i > 0: 
#             square_root = math.sqrt(i)
#             if square_root.is_integer():
#                 newlist.append(i)
#     return newlist
# mylist = [-4, -16, 0, 1, 4, 5, 9, 16, 25, 36, 49, 64, 81, 100]
# print(kokAlma(mylist))

# ve ya

# import math
# mylist = [-4, -16, 0, 1, 4, 5, 9, 16, 25, 36, 49, 64, 81, 100]
# print(list(filter(lambda x: x > 0 and math.sqrt(x).is_integer(), mylist)))






# ---------------------------------------------------------------------------------------------------------------------







#  2)Funksiya yazin list qebul etsin ve tekrarlanmayan elementleri bizə qaytarsın:


# listLen = int(input("listin uzunluğunu daxil edin: "))
# firstList = []
# for i in range(listLen):
#     element = input("elementi daxil edin: ")
#     firstList.append(element)  
# myList = list(filter(lambda x: firstList.count(x) == 1, firstList))
# print(myList)






# ---------------------------------------------------------------------------------------------------------------------------------------






# 3) Verilmiş inputdakı bütün rəqəmlərin bir birlərinə hasilini icra edən funksiya yazın

# def hasiliHesapla():
#     listLen = int(input("listin uzunlugunu daxil edin: "))
#     i=0
#     hasil=1
#     for i in range(listLen):
#         eded = int(input("eded daxil edin: "))
#         hasil*=eded
#         i+=1
#     return hasil
# print(hasiliHesapla())







# ------------------------------------------------------------------------------------------------------------------------------------






# 4) verilmiş ədədin bölənlərini list comprehension istifadə edərək yazın

# eded = int(input("Ededi daxil edin: "))
# newlist = [i for i in range(1, eded) if eded % i == 0 ]
# print(newlist)


# ---------------------------------------------------------------------------------------------------------------------------------------






# 5)Əlininzdə ayların olduğu bir list var siz ay qarşısında uzunluğu olduğu bir dictionary yaradın və bunu comprehension ilə edin və alınan listi print etdirin.
# mənim listim
# mylist=['may','iyun','iyul']
# bu şəkildə olacaq
# {'may': 3, 'iyun': 4, 'iyul': 4}



# myList = ['may', 'iyun', 'iyul']
# myDict = lambda myList: {i: len(i) for i in myList}
# dict = myDict(myList)
# print(dict)







# ----------------------------------------------------------------------------------------------------------------






# 6)names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]
#  verilmiş list-dən yalnız adların olduğu və kiçik hərflərlə yazıldığı list düzəldin və bunu conprehension ilə edin (əlavə olaraq funksiya da 
# istifadə edəbilərsiz).
# ['rick', 'morty', 'summer', 'jerry', 'beth']



# def getName(names):
#     newlist = []
#     for i in names:
#         name = i.split()[0]
#         newlist.append(name.lower())
#     return newlist
# names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]
# print(getName(names))

# ve ya

# names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]
# newlist=list(x.split()[0].lower() for x in names)
# print(newlist)






# ----------------------------------------------------------------------------------------------------------------






# 7) verilmiş iki listdəki ədədlərin indexlərinə uyğun olaraq ortalamasını tapın.
# nums1 = [1, 2, 3]
# nums2 = [4, 5, 6]
# results=[ 2.5, 3.5, 4.5]



# def cem(newList):
#     for i, j in zip(nums1, nums2):
#         a = (i + j) / 2
#         newList.append(a)
# nums1 = [1, 2, 3]
# nums2 = [4, 5, 6]
# newList = []
# cem(newList)
# print(newList)

#ve ya

# nums1 = [1, 2, 3]
# nums2 = [4, 5, 6]
# newList = list(map(lambda i, j: (i + j) / 2, nums1, nums2))
# print(newList)





# 1     +
# 2     ?
# 3     +
# 4     +
# 5     +
# 6     +
# 7     +