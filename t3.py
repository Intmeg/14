n = input('Введите название продукта: ')                                                            # Первый запрос названия наименования товара
flag1 = False                                                                                       # Флаг для определения первый запуск или нет
while n != 'плесень':                                                                               # Цикл проверяющий вводимое стоп-слово
    if flag1 == True:                                                                               # Проверка флага первого запуска
        n = input('Введите название продукта: ')                                                    # Запрос названия наименования товара
    flag1 = True                                                                                    # Флаг первого запуска
    f = open(r'.\products.txt',encoding='utf-8')                                                    # Открытие файла на чтение
    abs = 0                                                                                         # Переменная для сохранения общей суммы
    flag = False                                                                                    # Флаг на проверку был ли найден продукт с введённым наименованием
    k = 0                                                                                           # Выводит значение count
    for x in f:                                                                                     # Цикл, проходящий по каждой строке таблицы
        s = x.split('|')                                                                            # Разделение конкретной строки на столбцы
        if s[1] == n:                                                                               # Проверка совпадает ли необходимое наименование товара с наименованием в таблице
            if abs < int(float(s[3]))*int(s[4][:-3]):                                               # Проверка больше ли новая общая сумма старой общей суммы
                abs = int(float(s[3]))*int(s[4][:-3])                                               # Замена на новую общую сумму
                k = int(s[4][:-3])                                                                  # Заменяет на новый count
            flag = True                                                                             # Пометка о том, что продукт был найден
    if n != 'плесень':                                                                              # Проверка наименования продукта перед выводом
        if flag == False:                                                                           # Проверка был ли найден продукт
            print('Такого продукта нет на складе')
        else:
            print(f"На складе данного товара осталось {k} единиц на общую стоимость - {abs}")
