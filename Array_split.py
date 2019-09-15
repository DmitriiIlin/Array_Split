def ArrayChunk(array):
#Метод сортирует массив на вокруг опорного элемента
    if len(array)==0:
        return None
    else:
        while len(array)>0:
            middle=len(array)//2
            middle_value=array[middle]
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
                if start==finish or (start==(finish-1) and array[start]>array[finish]):
                    for imiddle in range(0,len(array)):
                        if array[imiddle]==middle_value:
                            return imiddle
                array[start], array[finish]=array[finish], array[start]
                #print(array)

def ArrayChunk_2(array):
    left=0
    right=len(array)-1
    middle=len(array)//2
    middle_value=array[middle]
    i=left-1
    j=right+1
    while True:
        i+=1
        while array[i]<middle_value:
            i+=1
        j-=1
        while array[j]>middle_value:
            j-=1
        if i>=j:
            #print(array)
            return j

def Bounds_Checking(array,left,right):
    #Проверка индексов
    if (type(array) is list) and (type(left) is int) and (type(right) is int):
        q_ty=len(array)
        if left>=0 and right<=q_ty-1 and right>left:
            return True
        else:
            return False
    return False
 
def Array_Limitation(array,left,right):
    #Ф-ция определяющая массив для работы
    result=[]
    for i in range(left,right+1):
        result.append(array[i])
    return result

def Array_Parts(array,left,right):
    # Возвращает левую, центральную и правую части массива-до элемента left левая часть после элемента right правая, между средняя
    left_part=[]
    right_part=[]
    middle_part=[]
    res=[]
    size=len(array)
    if Bounds_Checking(array,left,right)==True:
        for i in range(0,left):
            left_part.append(array[i])
        for l in range(left,right+1):
            middle_part.append(array[l])    
        for j in range(right+1,size):
            right_part.append(array[j])
        res.append(left_part)
        res.append(middle_part)
        res.append(right_part)
        return res
    else:
        return False

def Array_Division(array):
    #Сортировка
    middle=ArrayChunk(array)
    if len(array)<=1:
        return array
    else:
        return Array_Division(Array_Limitation(array,0,middle-1))+Array_Division(Array_Limitation(array,middle,len(array)-1))

def QuickSort(array,left,right):
    #Головная функция
    out=array 
    Res=Bounds_Checking(array,left,right)
    if Res!=True:
        return False
    else:
        diff_left=left-0
        left_part=[]
        right_part=[]
        sort_part=[]
        for i in range(0,diff_left):
            left_part.append(array[i])
        if right<len(array)-1:
            for j in range(right+1,len(array)):
                right_part.append(array[j])
        sort_part=Array_Limitation(array,left,right)
        sort_part=Array_Division(sort_part)
        array=left_part+sort_part+right_part
        out.clear()
        for all_index in range(0,len(array)):
            out.append(array[all_index])
        return out


def Array_Partitions(array,low,high):
    i=low-1
    pivot=array[high]
    for j in range(low,high):
        if array[j]<pivot:
            i+=1
            array[i],array[j]=array[j],array[i]
    array[i+1],array[high]=array[high],array[i+1]
    return (i+1)

def QuickSortTailOptimization(array,left,right):
    while (left<right):
        pivot=Array_Partitions(array,left,right)
        if (pivot-left)<(right-pivot):
            QuickSortTailOptimization(array,pivot+1,right)
            left=pivot+1
        else:
            QuickSortTailOptimization(array,pivot+1,right)
            right=pivot-1 

       
"""

b=[23,4,567,3,78,90,6785]
a=[67,78,3,444,6,5,255]
QuickSortTailOptimization(b,0,6)
print(b)
"""