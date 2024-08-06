def process_file(input_file, output_file, delimiter=' '):
    """
    Обрабатывает текстовый файл:
    1. Удаляет первый столбец.
    2. Во втором столбце добавляет точку в конце значения.
    3. Объединяет второй и третий столбцы.
    4. В объединенном третьем столбце добавляет 'e' в конце значения.
    Точка остается только после второго столбца.

    :param input_file: Путь к входному текстовому файлу.
    :param output_file: Путь к выходному текстовому файлу.
    :param delimiter: Разделитель между столбцами (по умолчанию пробел).
    """
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            # Разделяем строку на столбцы
            columns = line.strip().split(delimiter)
            
            # Проверяем, что строка содержит хотя бы три столбца
            if len(columns) < 4:
                continue  # Пропустить строку, если столбцов меньше 3

            # Удаляем первый столбец
            firs_col, second_col, third_col, forth_col = columns[0:4]

            # Добавляем точку во втором столбце
            second_col_with_dot = f"{second_col}."

            # Объединяем второй и третий столбцы, но без точки во втором
            combined_col = f"{third_col}*10^-{forth_col}"

            # Добавляем 'e' к объединенному столбцу
            combined_col_with_e = f"{combined_col}"

            # Формируем новую строку
            new_line = f"{firs_col}={second_col_with_dot}{combined_col_with_e}\n"

            # Записываем строку в выходной файл
            outfile.write(new_line)


# Пример использования
input_file = "recognized_numbers.txt"
output_file = "output_5.txt"
process_file(input_file, output_file, delimiter=' ')
print(f"Файл {input_file} обработан. Результат сохранен в {output_file}.")
