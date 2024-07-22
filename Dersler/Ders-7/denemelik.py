foreGround = 0
backGround = 0
for method in dir(str):
    if "__" not in method:
        foreGround+=1
    else:
        backGround+=1
        
print("Görünürde   :", foreGround , \
      "Arka Planda :", backGround)

#------------------------------------------





#1: capitalize()

sampleText = """huysuz Öğretmen Acımasızca odev veriyor,
ama yine de ben Python öğenmekten asla vazgeçmeyeceğim..."""
print(sampleText.capitalize())


#2: casefold()

sampleText = """huysuz Öğretmen Acımasızca odev veriyor,
ama yine de ben Python öğenmekten asla vazgeçmeyeceğim..."""
print(sampleText.capitalize())
x=10
for i in range(1,x + 1):
    y=i
    for i in range (y):
        print("*", end="")
    print()
for row in range(10,0,-1):
    for i in range(row):
        print(*"*",end="")
    print()
