import requests
from selenium import webdriver
import time
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import json
import itertools


driver = webdriver.Edge(EdgeChromiumDriverManager().install())

page = driver.get('https://www.nonolive.com/37493967')

time.sleep(20)
#parantez içinde yazılı class ları bulma
level = driver.find_elements_by_class_name('level')
sender = driver.find_elements_by_class_name('sender')
mesaj = driver.find_elements_by_class_name('text')

#bulunan clasları listelere ekleme
liste = []
for i in level:
    liste.append(i.text)

senderlist = []
for j in sender:
    senderlist.append(j.text)

textlist = []
for j in mesaj:
    textlist.append(j.text)



#İstenmeyen harflerin listeden çıkarılması
elements_to_remove = ['', ' : ']
filtered_list = []

for element in liste:
    if element not in elements_to_remove:
        filtered_list.append(element)

sender_filtered_list = []
for element in senderlist:
    if element not in elements_to_remove:
        sender_filtered_list.append(element)

text_filtered_list = []
for element in textlist:
    if element not in elements_to_remove:
        text_filtered_list.append(element)

print(filtered_list)
print("LEVEL SAYISI",len(filtered_list))
print(sender_filtered_list)
print("KULLANICI ADI SAYISI",len(sender_filtered_list))
print(text_filtered_list)
print("MESAJ SAYISI",len(text_filtered_list))
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxx")




#itretools.chain zip fonksiyonuyla liste sırasıyla karıştırıldı
unionlist = list(itertools.chain(*zip(filtered_list,sender_filtered_list,text_filtered_list)))


print("************************************************************************")


try:
    new_list = []

    sayi = 0
    kullaniciadi = 1
    mesaj = 2
    while sayi < len(filtered_list):
        for i in unionlist:
            new_list.append({"level": unionlist[sayi],"Kullanıcı Adı": unionlist[kullaniciadi],"Mesaj":unionlist[mesaj]})
            sayi +=3
            kullaniciadi += 3
            mesaj += 3
except:
    print("Döngüden çıkıldı")



"""
print(new_list)"""





# directly called encode method of JSON

with open("sample.json", "w") as outfile: 
    json.dump(new_list, outfile) 

time.sleep(2)

with open("sample.json", "r") as read_file:
    print("Reading JSON serialized Unicode data from file")
    sampleData = json.load(read_file)

print("||||||")
print("/n")
print(sampleData)
print("the and")

for i in sampleData:
    print(i)

time.sleep(5)


"""
ÖNCELİKLİ GELİŞTİRME: MESAJLARI AYIRT ETME. ÖRNEĞİN EN ÇOK PUBG Mİ PUBG MOBİLE MI YAZIYOR GİBİ

SONRAKİ GELİŞTİRME: VERİLERİ ARAYÜZDE GÖSTERME. KİŞİNİN KULLANABİLECEĞİ ŞEKİLDE YAPMAK

WEBDRİVER SEÇİMİNİN KULLANICI TARAFINDAN YAPILMASI

webdriver ile açılan pencerenin görünmemesi veya küçültülmesi

programı serverda çalıştırabilme
"""


driver.close()



