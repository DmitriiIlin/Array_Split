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
                for istart in range(0,len(array)):
                    if array[middle]>array[start]:
                        start+=1
                    else:
                        istart=0
                        break
                for ifinish in range(0,len(array)):
                    if array[middle]<array[finish]:
                        finish-=1
                    else:
                        ifinish=0
                        break
                if start==(finish-1) and array[start]>array[finish]:
                    array[start],array[finish]=array[finish],array[start]
                    break
                if start==finish or (start==(finish-1)) and array[start]>array[finish]:
                    #print(array)
                    return middle
                array[start], array[finish]=array[finish], array[start]
                #print(array)
            
"""       
a=[7,5,6,4,3,1,2]
print(ArrayChunk(a))
"""