# Напишите программу, которая определит позицию второго
# вхождения строки в списке либо сообщит, что её нет.
# Пример:
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1
all_list = ["123", "234", 123, "567"]
text = "123"
count = 0
for i in range(len(all_list)):
    if text == all_list[i]:
        count += 1
        if count == 2:
            print(i)
            break
else:
    print(-1)