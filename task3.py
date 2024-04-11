"""
Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
Достаточно вернуть один допустимый вариант.*Верните все возможные варианты комплектации рюкзака.
"""
from operator import itemgetter

things = {
    'палатка': 4,
    'нож': 0.2,
    'спальный мешок': 1,
    'спички': 0.05,
    'еда': 4,
    'вода': 5,
    'карта': 0.2
}

max_weight = 15
weight = 0
capacity_weight = 0
print("список вещей: ", things)
print("список вещей по максимально возможной грузоподьемности рюкзака в ", max_weight, "кг")
for t, value in dict(sorted(things.items(), key=itemgetter(1))).items():
    weight += things[t]

    if weight <= max_weight:
        print(things, ' = ', value)
        capacity_weight += things[t]

print("общий вес рюкзака c вещами: ", capacity_weight)

