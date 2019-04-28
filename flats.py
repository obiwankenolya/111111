import csv

flats_list = list()

with open('output.csv', newline='') as csvfile:
	flats_csv = csv.reader(csvfile, delimiter=';')
	flats_list = list(flats_csv)
headers = flats_list.pop(0)
count = 0
flat_count = 0
subway_set = set()

# for flat in flats_list:
#   if "новостройка" in flat:
#     print("Квартира {} - новостройка.".format(flat[0]))
#     count += 1
# print("Всего новостроек: {}.".format(count))
# print()


# # TODO 2:
# # 1) Сделайте описание квартиры в виде словаря, а не списка. Используйте следующие поля из файла output.csv: ID, Количество комнат;Новостройка/вторичка, Цена (руб).

# flat_info = {"ID":flat[0], "Комнат":flat[1], "Тип":flat[2], "Цена":flat[11]}

# # 2) Измените код, который создавал словарь для поиска квартир по метро так, чтобы значением словаря был не список ID квартир, а список описаний квартир в виде словаря, который вы сделали в п.1

# subway_dict = {}
# for flat in flats_list:
#   subway = flat[3].replace("м.", "")
#   if subway not in subway_dict.keys():
#     subway_dict[subway] = dict()
#     subway_dict[subway] = {"ID":flat[0], "Комнат":flat[1], "Тип":flat[2], "Цена":flat[11]}

# print(subway_dict)
# print()

# # # 3) Самостоятельно напишите код, который подсчитывает и выводит, сколько квартир нашлось у каждого метро.

flats_dict = {}
i = 0

# for flat in flats_list:
#   subway = flat[3].replace("м.", "")
#   subway_set.add(subway)
#   if subway not in flats_dict.keys():
#     flats_dict[subway] = []
#   flats_dict[subway].append(flat[0])
# print(flats_dict)

# for flat in flats_list:
#   subway = flat[3].replace("м.", "")
#   subway_set.add(subway)
#   for subway in subway_set:
#     if subway in flats_list:
#       i += 1
#   print(subway, i)
# # # for subway in subway_set:


print(flats_list)