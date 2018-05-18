# 2nd-year-thesis
<b>Приложения 1</b> и <b>2</b> - результаты корпусного исследования, выполненного в рамках курсовой работы.

<b>Источники данных:</b>

http://realec.org

http://www.learnercorpusassociation.org/resources/tools/locness-corpus/

Базы данных с частотами биграмм и словоформ в подкорпусах можно загрузить по адресу:

https://yadi.sk/d/m9RhasYR3W9T2c (Объём несжатой папки - 826 МБ)

realec_helper.py - скрипт для загрузки копии корпуса REALEC в указанную папку (может использоваться только через import)

Взаимодействие с сайтом realec.org происходит через класс realecHelper, имеющий следующие методы:

download_folder(path_to_folder = путь к папке в корпусе, path_to_saved_folder = путь к папке на компьютере) - сохраняет папку корпуса в указанную папку на компьютере, если указать
первым аргументом (при вводе '/' в качестве пути к папке будет скачан весь корпус).

download_document(путь к документу в корпусе,path_to_saved_document = путь к файлу на компьютере) - скачивает текст эссе и сохраняет по указанному адресу на компьютере 
