
#tersten okunusu ile aynı olan kelimeleri test eden fonk
#kazak
def palindrom(myString):
    a=True
    for i in range(len(myString)//2):
        if(myString[i]!=myString[(len(myString)-1)-i]):
            a=False
            break
    return a

i='nedden'
print(palindrom(i))
           
        
    
                   
