import csv

#NOT1 : everythıng is in text. It is your responsibility to convert to proper data type as needed

csvFile1 = "/home/debinci/Desktop/NOVA_Dersler/Dersler/Ders-23/CSV/names.csv"
csvFile2 = "/home/debinci/Desktop/NOVA_Dersler/Dersler/Ders-23/CSV/gsml10y.csv"
csvFile3 = "/home/debinci/Desktop/NOVA_Dersler/Dersler/Ders-23/CSV/new_names.csv"

with open(csvFile1) as file:
    csvRead = csv.reader(file, delimiter=",")
    #next(csvRead)
    
    for line in csvRead:
        print(line)

#------------------------------------

lines = []
with open(csvFile1) as file:
    for line in file:
        lines.append(line.strip().split(","))

for i in lines:
    print(i[0])

#------------------------------------

lines = []
with open(csvFile1) as fileToRead:
    fTr = csv.reader(fileToRead)
    with open(csvFile3, "w") as fileToWrite:
        fTw = csv.writer(fileToWrite)

        for line in fTr:
            lines.append(line)
            fTw.writerow(line)
            print(line)

print(lines[0])
print("John" in lines[1])
