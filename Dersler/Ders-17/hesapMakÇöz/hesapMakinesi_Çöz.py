# + Toplama
# + Çıkarma
# + Çarpma
# + Bölme
# + Karakök Alma
# + Kuvvetini alma
# + Bölümden kalanı bulma

# işlemlerini yerine getirecek bir hesap makinesi 


#from kutups.kutup import main # type: ignore
# import kutups.kutup as k

# while True:
#     k.main()

def toplama(*num):
    res = 0
    for i in num:
        res+= int(i)
    print(*num)
    return res

a = input("gİR :").split(" ")

print(toplama(*a))