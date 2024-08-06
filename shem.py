def remove_dot_after_second_column(input_file, output_file, delimiter=' '):
    """
    Удаляет точку в конце значений второго столбца из текстового файла.

    :param input_file: Входной файл.
    :param output_file: Выходной файл.
    :param delimiter: Разделитель между столбцами (по умолчанию пробел).
    """
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            # Разделяем строку на столбцы
            columns = line.strip().split(delimiter)
            
            # Проверяем, что строка содержит хотя бы два столбца
            if len(columns) < 2:
                outfile.write(line)  # Если столбцов меньше двух, пишем строку без изменений
                continue

            # Убираем точку из второго столбца, если она есть
            if columns[1].endswith('.'):
                columns[1] = columns[1][:-1]

            # Собираем строку обратно
            new_line = delimiter.join(columns) + '\n'
            outfile.write(new_line)


# Пример использования
input_file = "output_2.txt"
output_file = "output_3.txt"
remove_dot_after_second_column(input_file, output_file, delimiter=' ')
print(f"Файл {input_file} обработан. Результат сохранен в {output_file}.")
