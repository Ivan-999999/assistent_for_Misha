
#Цель программы: принимая на вход два значения, количество квартир в доме и необходимый интервал,
#Выводил остаток.
#выводить в ряд числа в данном интервале. При этом формируя из них кортеж и присваивая ему порядковый номер.
#После завершения этого вычисления, повторить, увеличив начальное значение на 1.
#Сделть графический интерфейс.


# def assistent_for_Misha(apartments, intervals):
#     i = 1
#     while (i + intervals) <= apartments:
#         a.append(i)
#         i += intervals
#     return i
#
# apartments = int(input('Укажи количество квартир: '))
# intervals = int(input('Укажи интервал: '))
# c = assistent_for_Misha(apartments, intervals)
# print(c)

def assistent_for_Misha(apartments, intervals):
    i = 1
    a = []  # Объявляем пустой список
    while i <= apartments:
        a.append(i)
        i += intervals

    return str(a)


apartments = int(input('Укажи количество квартир: '))
intervals = int(input('Укажи интервал: '))
result = assistent_for_Misha(apartments, intervals)
print(result)






















