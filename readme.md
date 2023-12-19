# Сжатие данных методом Хаффмана


## Установка

Для работы программы необходим Python версии 3 и выше.
Скачайте программу из репозитория.

## Использование

# Для кодирования файла:
- Ввести в консоли `python main.py encode file_path`, 
где `file_path` - путь до кодируемого файла (примеры файлов: `text1.txt`, `text2.txt`)
Например: `python main.py --code encode --file_path test.txt`

# Для кодирования папки:
- Ввести в консоли `python main.py encode folder_name`, 
где `file_name` - имя папки (примеры папок: `texts`)
Например: `python main.py --code encode --file_path texts`

# Для декодирования файла:
Замечание: Чтобы декодировать файл, надо сначала его закодировать и получить кодировку (с помощью метода выше)
- Ввести в консоли `python main.py --code decode file_path file_path_codes`, 
где `file_path` - путь до декодируемого файла (примеры файлов: `text1.txt`, `text2.txt`),
где `file_path_codes` - путь до кодируемого файла (примеры файлов: `text1_codes.txt`, `text2_codes.txt`)
Например: `python main.py --code decode --file_path test_encode.txt`

# Для декодирования папки:
- Ввести в консоли `python main.py decode folder_name`, 
где `file_name` - имя папки (примеры папок: `texts`)
Например: `python main.py --code decode --file_path texts`