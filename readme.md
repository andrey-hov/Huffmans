# Сжатие данных методом Хаффмана


## Установка

Для работы программы необходим Python версии 3 и выше.
Скачайте программу из репозитория.

## Использование

# Для кодирования файла:
- Ввести в консоли `python main.py encode file_path file`, 
где `file_path` - путь до кодируемого файла (примеры файлов: `text1.txt`, `text2.txt`)
Например: `python main.py encode text1.txt file`

# Для декодирования файла:
Замечание: Чтобы декодировать файл, надо сначала его закодировать и получить кодировку (с помощью метода выше)
- Ввести в консоли `python main.py decode file_path file_path_codes`, 
где `file_path` - путь до декодируемого файла (примеры файлов: `text1.txt`, `text2.txt`),
где `file_path_codes` - путь до кодируемого файла (примеры файлов: `text1_codes.txt`, `text2_codes.txt`)
Например: `python main.py decode text1_encode.txt text1_codes.txt`