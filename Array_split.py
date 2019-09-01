def ArrayChunk(array):
#Метод сортирует массив на вокруг опорного элемента
    if len(array)==0:
        return None
    else:
        while len(array)>0:
            middle=len(array)//2
            start=0
            finish=len(array)-1
            while len(array)>0:
                while array[middle]>array[start]:
                    start+=1
                while array[middle]<array[finish]:
                    finish-=1
                if start==(finish-1) and array[start]>array[finish]:
                    array[start],array[finish]=array[finish],array[start]
                    break
                if start==finish or (start==(finish-1) and array[start]>array[finish]):
                    #print(array)
                    return middle
                array[start], array[finish]=array[finish], array[start]
            
"""           
a=[1,23]
print(ArrayChunk(a))
"""