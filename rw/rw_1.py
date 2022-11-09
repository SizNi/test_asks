# пример 1
input_file = open("input.txt", "r")  # открывается файл для чтения
output_file = open("output.txt", "w")  # создается файл для записи
for i, line in enumerate(input_file, 1):  # начинается алгоритм нумерации строк в файле для записи
    output_file.write(f"{i}) {line}")
input_file.close()  # файлы закрываются и не занимают память больше
output_file.close()

# прмер 2
with open("input.txt", "r") as input_file:  # конструкция, по выходу из которой закрываются все структуры, которые открыты в ней
    with open("output.txt", "w") as output_file:
        for i, line in enumerate(input_file, 1):
            output_file.write(
                f"{i}) {line}"
            )