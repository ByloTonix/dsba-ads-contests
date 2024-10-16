# Формат ввода

# В каждой строке сначала записан номер класса (число, равное 9, 10 или 11), затем (через пробел) – фамилия ученика. Общее число строк в файле не превосходит 100000. Длина каждой фамилии не превосходит 50 символов.
# Формат вывода

# Необходимо вывести список школьников по классам: сначала всех учеников 9 класса, затем – 10, затем – 11. Внутри одного класса порядок вывода фамилий должен быть таким же, как на входе.
class_9, class_10, class_11 = [], [], []
with open("input.txt") as file:
    for line in file:
        _class, surname = line.split()
        if _class == "9":
            class_9.append(line.strip())
        elif _class == "10":
            class_10.append(line.strip())
        elif _class == "11":
            class_11.append(line.strip())
        else:
            print("Unexpected case")
print("\n".join(class_9 + class_10 + class_11))
