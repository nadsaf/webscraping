from bs4 import BeautifulSoup
import requests
import csv
import mysql.connector 

url = 'https://wikimon.net/Visual_List_of_Digimon'
x = requests.get(url)

soup = BeautifulSoup(x.content, 'html.parser')
names = []
images = []

for a in soup.find_all('table', style="text-align: center; width: 130px; float: left; margin: 0px 4px 2px 0px; background-color: #222222;"):
    for b in a.find_all('a'):
        nama = b.text
        if nama == '':
            pass
        else: 
            names.append(nama)
        
    for c in a.find_all('img'):
        # print(c)
        judul = c.get('src')
        if judul == None:
            pass
        else:
            images.append('https://wikimon.net/'+judul)

print(len(names))
print(len(images))

#Jadiin Dictionary =================================================================
allData = []
csv_column = ['nama', 'gambar']
for y in range(len(names)):
    dataDict = {
        'nama' : names[y],
        'gambar' : images[y] 
    }
    allData.append(dataDict)

print(allData)

# Save as CSV dari Dictionary =======================================================
with open('5.digimondict.csv', 'w', encoding="utf-8", newline='') as writeFile:
        writer = csv.DictWriter(writeFile, fieldnames=csv_column)
        writer.writeheader()
        writer.writerows(allData)

'''
# IMPORT TO MSQL =======================================================
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'NadyaSaffira',
    passwd = '12345',
    database = 'digimon'
)

for z in range(len(names)):
    y = mydb.cursor()
    y.execute('insert into digimon (nama, gambar) values (%s, %s)', (names[z], images[z]))          #di database usia otomatis berubah jadi int sesuai format database
mydb.commit() 
'''