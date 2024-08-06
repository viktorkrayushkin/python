import os
import re
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter

# Укажите путь к Tesseract, если требуется
pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/Cellar/tesseract/5.5.0/bin/tesseract'

def preprocess_image(image_path):
    """
    Подготовка изображения для улучшения распознавания текста.
    """
    image = Image.open(image_path)
    # Преобразование в градации серого
    image = image.convert('L')
    # Увеличение контраста
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2.0)
    # Применение фильтра для сглаживания шумов
    image = image.filter(ImageFilter.MedianFilter(size=3))
    return image

def extract_numbers_from_image(image_path):
    """
    Извлекает числа из изображения.
    """
    image = preprocess_image(image_path)
    # Настройка Tesseract для исключения букв
    custom_config = r'--oem 3 --psm 6 -c tessedit_char_blacklist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    text = pytesseract.image_to_string(image, config=custom_config)
    # Извлечение чисел с помощью регулярного выражения
    numbers = re.findall(r'\d+', text)
    return numbers

def main():
    # Директория с изображениями
    image_directory = 'frames_folder'
    # Выходной файл
    output_file = 'recognized_numbers.txt'

    # Распознаваемые расширения
    supported_extensions = ('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')
    image_files = [f for f in os.listdir(image_directory) if f.lower().endswith(supported_extensions)]

    with open(output_file, 'w') as f_out:
        for image_file in image_files:
            image_path = os.path.join(image_directory, image_file)
            numbers = extract_numbers_from_image(image_path)
            if numbers:
                numbers_line = ' '.join(numbers)
                f_out.write(f"{image_file}: {numbers_line}\n")
                print(f"Извлечено из {image_file}: {numbers_line}")

if __name__ == '__main__':
    main()
