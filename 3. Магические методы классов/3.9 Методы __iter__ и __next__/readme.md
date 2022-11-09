## Методы \_\_iter__ и \_\_next__

Статьи на тему:

- <https://proproprogs.ru/python_oop/magicheskie-metody-iter-next>
- <https://habr.com/ru/company/domclick/blog/674194/>
- <https://www.programiz.com/python-programming/methods/built-in/iter>
- <https://stackoverflow.com/questions/64577138/implement-iter-and-next-in-different>
- <https://habr.com/ru/post/488112/>

task_0.py - примеры из видео-урока

---

**Подвиг 5.**

Объявите в программе класс Person, объекты которого создаются командой:

    p = Person(fio, job, old, salary, year_job)

где <u>fio</u> - ФИО сотрудника (строка);\
<u>job</u> - наименование должности (строка);\
<u>old</u> - возраст (целое число);\
<u>salary</u> - зарплата (число: целое или вещественное);\
<u>year_job</u> - непрерывный стаж на указанном месте работы (целое число).

В каждом объекте класса Person автоматически должны создаваться локальные атрибуты с такими же именами: fio, job, old, salary, year_job и соответствующими значениями.

Также с объектами класса Person должны поддерживаться следующие команды:
```python
data = p[indx] # получение данных по порядковому номеру (indx) атрибута (порядок: fio, job, old, salary, year_job и начинается с нуля)
p[indx] = value # запись в поле с указанным индексом (indx) нового значения value
for v in p: # перебор всех атрибутов объекта в порядке: fio, job, old, salary, year_job
    print(v)
```
При работе с индексами, проверить корректность значения indx. Оно должно быть целым числом в диапазоне [0; 4]. Иначе, генерировать исключение командой:

    raise IndexError('неверный индекс')

Пример использования класса (эти строчки в программе не писать):
```python
pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
pers[0] = 'Балакирев С.М.'
for v in pers:
    print(v)
pers[5] = 123 # IndexError
```
P.S. В программе нужно объявить только класс. Выводить на экран ничего не нужно.
