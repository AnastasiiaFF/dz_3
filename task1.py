"""
Дан список повторяющихся элементов. 
Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.
"""

list = [1, 2, 8, 5, 3, 1, 5, 'A', 6, 7, 'C', 8, 3, 2, 11]
set_list = set(list)
new_list = []
for i in set_list:
    new_list.append(i)
print(list)
print(new_list)