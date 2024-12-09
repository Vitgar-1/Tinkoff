from funk import *
b = 1
while True:
    go = input(
        '\n\n\nВведите известные вам местоположения букв в формате *а**и\nили оставьте пустым в случае неизвестного местоположения букв (*****)\n')
    lines = Mest(lines, go)

    gid = input('\nвведите какие буквы исключаем - подряд (БезПробелаПожалуйста!)\n')
    lines = Iskluch(lines, gid)

    gid2 = input(
        '\nвведите какие буквы есть в слове но не известно на каком месте - с указанием где было формат (а0б4г1)\n отсчёт с 0 до 4\n')
    lines = Izvesn(lines, gid2)

    while True:
        a = input('продолжаем это слово?')

        if a != '' and a != 'да' and a != 'Да':
            lines = Zanovo(lines, lines2)
            print('Угадано за', b, 'попыток')
            b = 1
            break
        elif a == '' or a == 'да' or a == 'Да':
            b += 1
            print('начинаем', b, '-ую попытку')
            break
        else:
            print('не угадан ответ на последний вопрос')
