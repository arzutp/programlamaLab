#hash table baslangıcta n boyutlu bir tablo olusturdur icinde 0 degerleri olsun
#sonra insert fonk olustur
import random
def createMyHashTable(N):  
    myTable = []
    for i in range(N):
        myTable.append(0)
    return myTable


def my_hash(size,numberToBeInserted):
    return numberToBeInserted%size

def insertMyHashTable(myTable,numberToBeInserted): 
    isCollision=False
    index=my_hash(len(myTable),numberToBeInserted) #nereye yerlesecegi
    if(myTable[index]==1):  # sadece 1 ve 0 yapıyoruz 
        isCollision=True
    else:
        myTable[index]=1
        #myTable[index]=numberToBeInserted #sayıyı ekliyoruz
    return isCollision
    

my=createMyHashTable(23)
print(my)
print(insertMyHashTable(my,20))
print(my)
print(insertMyHashTable(my,20))


#random.choice([0,1,2,3,4,5,6,7,8,9])

def myTest(size=13,numberOfInsert=10): 
    my=createMyHashTable(size)
    c=0
    for s in range(numberOfInsert): #kac defa true geldıgını olcmek
        #number=random.choice([0,1,2,3,4,5,6,7,8,9])
        number=random.randint(0,1000)
        if(insertMyHashTable(my,number)==True):
            c=c+1
    return c
print(myTest(203,50))
   
