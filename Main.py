
sequence = [10, 20, 30, 40, 50, 60, 70, 80, 90]

groupCount = 5

l = 0
g = 0

group = []


for i in range(len(sequence)-1, -1, -1): #записужмо в кожну групу шкафів крім останньої по одному починаючи з найбільшого
    if g < groupCount-1:
        l = 0
        group.append([]) #виділення памяті
        group[g].append(sequence[i])
        g += 1
    else: # в останню групу записуємо решту шкафів
        group.append([])
        group[g].append(sequence[i])
        l += 1

def summ(array): #пошук суми справ в групі
    suma = 0
    for i in range(0, len(array)): # в циклі по масиву сумуємо всі справи
        suma += array[i]
    return suma

def maximum(group, groupCount):
    suma = []
    for i in range(0, groupCount): #виділяємо память для підрахунку кількості папок в групі шкаф стажера
        suma.append(0)
    index = 0
    for i in range(0, groupCount): #шукаєм кількость папок в групі шкаф кожного стажера
        suma[i] = summ(group[i])

    max = suma[0] #присвоюємо змінній максимальної кількості справ перше значення

    for i in range(1, groupCount): #шукаємо максимальну кількість
        if suma[i] > max: #якщо поточний елемент більший за максимальний
            max = suma[i] #присвоюємо значення максимальному елементі поточне
            index = i #записуємо індек максимального елемента

    data = [] #змінна для повернення результату
    for i in range(0,3): #виділення памяті для результату
        data.append(0)
    data[0] = suma #запис масиву з сумами
    data[1] = max #запис максимальної суми
    data[2] = index #запис індекса максимальної суми

    return data # повернення результату

data = maximum(group, groupCount) #виклик функії знаходження сум та максимальної суми
sum = data[0] #запис результату
max = data[1]
index = data[2]

while(index>0): #поки індекс максимальної суми більший 0
    if sum[index-1] + group[index][0] <= max: #якщо сума справ ближньої групи + найбільший шкаф зі справами максимальної групи менша або рівна максимальної
        group[index-1].append(group[index][0]) # переносимо найбільший шкафчик в сусідній
        del(group[index][0]) #видаляємо найбільший шкафчик з поточної групи
        data = maximum(group, groupCount) # повторюємо підрахунок сум в нових групах
        sum = data[0]
        max = data[1]
        index = data[2]
    else: # в іншому випадку зупиняємо цикл
        break

for line in range(groupCount-1, -1, -1):  #вивід в циклі груп шкафчиків
    for row in range(len(group[line])-1, -1, -1):
        print(group[line][row])
    print("---")


