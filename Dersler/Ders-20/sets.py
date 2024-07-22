set0 = {"Begonya", "Sümbül"}
set1 = {"Begonya","Kardelen","Lavanta","Sümbül","Begonya","Kardelen","Lavanta", "Sümbül",1,4}
set2 = {1,4,7,6,3,4,3,2,1,3,4,"Lavanta", False, "Adıyaman","Üzüm"}
set3 = {True,False,True, False,False}
list1 = ["Elma","Armut", "Üzüm",4,122,"g",1,4,2,6,"Üzüm","Armut"]
tuple1 = ("İzmit", "Mersin","Adıyaman","Diyarbakır")

# print("Set 1 : ", set1)
# print("Set 2 : ", set2)
# print("Set 3 : ", set3)


# print(len(set1))

# for i in set1:
#     print(i)

# if "Begonya" in set1:
#     print("Evet burda...")

#------------
#Add Function
#------------

#Eleman Ekleme

# set1.add(123)
# print(set1)

#------------
#Update/Union Function
#------------
"""Amacı iki veya daha fazla seti birleştirmek"""

#Başka bir set ekleme
# set1.update(set2)
# print(set1)

#Union presentation "|"
#set1.union(set3,set4)
# print(set1)

# set4 = set1 | set2 | set3
# print(set4)
#set1 |=set2


#Bir Listeyi ekleme
# listem = ["Arzu", "Leyla", "İnci"]

# set1.update(listem)
# print(set1)

#---------------
#removing element or set
#---------------

# set1.remove("Begonya")
# print(set1)
# set1.discard("Ebru")
# print(set1)
# set1.pop()
# print(set1)
# set1.clear()
# print(set1)

# del set1

#---------------
#Joining Sets
#---------------
#Ortak Elemanlar Kümesi

# set4 = set1.intersection(set2)
# set5 = set1 & set2
# set1.intersection_update(set2)
#set1 &= set2


#---------------
#Difference Fark Sets
#---------------
"""Set1 de olan ama diğer set te olmayan elemanları verir"""
# set4 = set1.difference(set2)
# set5 = set1 - set2
# set1.difference_update(set2)
# set1 -=set2
# print(set1)



#---------------
#Simetrik Fark Sets 
#---------------
"""Her iki sette ortak olmayan elemanları listeler"""

# set4 = set1.symmetric_difference(set2)
# set5 = set1 ^ set2
# set1.symmetric_difference_update(set2)
# set5 ^= set2

#Kesişen elemanları varsa False, yoksa True
#print(set1.isdisjoint(set0))

#set0 set1 in alt kümesimidir.
print(set0.issubset(set1))

#set1, set0 ı kapsar mı?
print(set1.issuperset(set0))