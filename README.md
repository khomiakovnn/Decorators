# Домашнее задание к лекции «Decorators»
- Файл main.py содержит ДЗ к предыдущей лекци (итераторы и генераторы)
- Файл decorator.py содержит декораторы для функций и методов файла main.py
- Передача аргументов в декоратор изначально была через аргументы декорируемой функции и самого внутреннеего декоратора. Оставил вариант с передачей аргументов конструктором декоратора, как в лекции. Так кажется более правильно для отладки.
- Не понял почему при импорте декоратора сохранился его функционал по работе с датами и временем, без прямого импорта модуля "datetime" в файл main.py