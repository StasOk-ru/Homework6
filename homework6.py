#homework6

my_dict = {'Stas': 1981, 'Irina': 1982, 'Volodja': 1980}
print(my_dict)
print('Год рождения Стаса: ', my_dict.get('Stas'))
print('Год рождения Романа: ', my_dict.get('Roman', 'в словаре, не найден'))

my_dict.update({'Valera': 1985, 'Kolja': 1988})
print('Словарь изменен, добавлены Валера и Коля : ', my_dict)
а = my_dict.pop("Volodja")
print('Словарь изменен, из словаря удалён Володя, г.р: ', а)
print('Последние данные в словаре:', my_dict)
print('')
my_set = {1, 2, 3, 4, 1, 2, 3, 'test', 'Test', 'test'}
print('Создано множество: ', my_set)

#Вторая часть - множества
my_set.update({45, 55})
print('Можество изменено: ', my_set)
my_set.remove(4)
print('Из множества удален элемент: ', my_set)
