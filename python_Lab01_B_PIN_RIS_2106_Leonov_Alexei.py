#python_lab01_B_PIN_RIS_2106_Leonov_Alexei

import sys,os,time

#метод шейкерной сортировки
def shaker_sort(array):
    length = len(array)
    swapped= True
    start_index=0
    end_index=length-1

    while (swapped==True):

        swapped=False

        #Проход слева на право
        for i in range(start_index, end_index):
            if(array[i]>array[i+1]):
                #обмен элементов
                array[i], array[i+1] = array[i+1],array[i]
                swapped=True
        
        #Если не было обменов прерываем цикл
        if(not(swapped)):
            break

        swapped=False

        end_index= end_index-1

         #Проход права на лево
        for i in range(end_index-1, start_index-1,-1):
            if(array[i]>array[i+1]):
                #обмен элементов
                array[i], array[i+1] = array[i+1],array[i]
                swapped=True
        
        start_index=start_index+1
        


print("Шейкерная сортировка целочисленного массива:")
array=[]
count=10

for i in range(0,5):

    #открытие файла и запись его в массив
    with open('NoSort'+str(count)+'.txt') as f:
        for line in f:
            array.append([int(x) for x in line.split()])
    f.close()

    #время начала сортировки
    start_time = time.time()
    
    #запуск сортировки
    shaker_sort(array)
    
    #время окончания сортировки
    end_time = time.time()
    
    #разница между конечным и начальным временем
    elapsed_time = end_time - start_time
    print('Время сортировки ('+str(count)+') элементов массива: ', elapsed_time)
    
    #запись отсортированного массива в файл
    with open('Sort'+str(count)+'.txt','w+') as f:
        f.write(str(array))
    f.close
    count=count*10
    

