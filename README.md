# Python3.lab1
**Just some simple python work**

_Если кому-то интересно, PyCharm Community поддерживает редактирование Markdown_

### Roadmap

- Общая информация
- Установка зависимостей
- Кофигурация запуска для PyCharm
- Unit-тестирование
- Полезные ссылки

### Общая информация

> *без внятного ТЗ - результат хз*

Проект выполен в рамках лабораторной работы и представляет собой простую модель городской инфраструктуры. Поддерживает ввод/вывод в CLI, сохранение состояния в формате JSON-файлов. Работает на Python3.11

Unit-тесты работают с pytest и monkeypatch

*Я сделал как понял ТЗ-шку, потому что инфы по сути нет*

### Установка зависимостей

Необходимо установить Python3 актуальной версии. В зависимости от операционной системы можно воспользоваться пакетным менеджером, либо установить Python с официального сайта

Проект по сути требует только pytest
Установка может быть произведена при помощи pip (идет вместе с Python3, дополнительной установки не требует)

```pip install -r requirements.txt```

Либо

```pip install pytest```

Сторонних библиотек не требует

### Конфигурация запуска для PyCharm

Запускать необходимо classes.main.py
Для тестов используется модуль dev.tests

### Unit-тестирование

Для unit-тестирования используется pytest. Мануал по установке выше

Для запуска необходимо запустить dev.tests.supertest.py или отдельный тест из этого файла

### Полезные ссылки

- [PyTest (Habr)](https://habr.com/ru/articles/269759/)
- [Monkeypatch (Wikipedia)](https://ru.wikipedia.org/wiki/Monkey_patch)
- [Monkeypatch (Hexlet)](https://ru.hexlet.io/courses/python-advanced-testing/lessons/monkey-patching/theory_unit)
- [hasattr, setattr, etc.](https://proghunter.ru/articles/working-with-object-attributes-in-python-hasattr-delattr-setattr-getattr-functions)
- [JSON](https://habr.com/ru/articles/554274/)