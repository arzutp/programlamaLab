#matrisi hashe donustur
#m*n boyutlarında butun elemanları -1 olan 2 boyutlu
import random
def my_function_create(m,n):
    my_list=[]
    for i in range(m):
        my_list.append([])
        
        for j in range(n):
            #s=random.randint(-5,-5)
            s=-1
            my_list[i].append(s)
    return my_list

def my_function_print(myList):
    m=len(myList)
    n=len(myList[0])
    for i in range(m):
        for j in range(n):
            print(myList[i][j],end=" ")
        print()

my_array=my_function_create(3,2)
my_function_print(my_array)

def my_function_convert_to_hash(myList): #hash yapısı
    my_dict={}
    m=len(myList)
    n=len(myList[0])
    for i in range(m):
        for j in range(n):
            my_dict[(i,j)]=myList[i][j]
    return my_dict

a=my_function_convert_to_hash(my_array)
print(a)

def my_function_print_hash(myHashList):
    for key in myHashList:
        print(myHashList[key],end=" ")

my_function_print_hash(a)
