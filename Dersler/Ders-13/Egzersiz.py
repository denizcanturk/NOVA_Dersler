#import platform

#print(dir(platform))
#print(platform.machine())
#print(platform.version())


dersler = ("Python", "C++", "HTML", "CSS")

for ders in dersler:
    if "HTML" in dersler:
        idx = dersler.index("HTML")
        dersler[idx] = "Perl"
        
print(dersler)



