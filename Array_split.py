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

def Array_Division(array):
    #Сортировка
    middle=ArrayChunk(array)
    if len(array)<=1:
        return array
    else:
        left_part=Array_Limitation(array,0,middle-1)
        right_part=Array_Limitation(array,middle,len(array)-1)
        return Array_Division(left_part)+Array_Division(right_part)

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
"""
a=[67,78,3,4,6,5,2]
print(QuickSort(a,0,6))
print(a)
#ArrayChunk(a)
print(a)
"""