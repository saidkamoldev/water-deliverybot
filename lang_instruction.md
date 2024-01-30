## Название - dating

### Запускаем первый раз

1. Вытаскиваем тексты из файлов (он сам находит)
   `pybabel extract . -o locales/tozasuv.pot`
   
2. Создаем папку для перевода на английский
   `pybabel init -i locales/tozasuv.pot -d locales -D tozasuv -l uz`
3. То же, на русский
   `pybabel init -i locales/tozasuv.pot -d locales -D tozasuv -l ru`
5. Переводим, а потом собираем переводы
   `pybabel compile -d locales -D tozasuv`

### Обновляем переводы

1. Вытаскиваем тексты из файлов, Добавляем текст в переведенные версии
   `pybabel extract . -o locales/dating.pot`
   `pybabel update -d locales -D dating -i locales/dating.pot`
2. Вручную делаем переводы, а потом Собираем
   `pybabel compile -d locales -D dating`