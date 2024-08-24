import random

# список учеников
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
# отсортируем список учеников
students.sort()
# список предметов
classes = ['Математика', 'Русский язык', 'Информатика']
# пустой словарь с оценками по каждому ученику и предмету
students_marks = {}
# сгенерируем данные по оценкам:
# цикл по ученикам
for student in students:  # 1 итерация: student = 'Александра'
    students_marks[student] = {}  # 1 итерация: students_marks['Александра'] = {}
    # цикл по предметам
    for class_ in classes:  # 1 итерация: class_ = 'Математика'
        marks = [random.randint(1, 5) for i in range(3)]  # генерируем список из 3х случайных оценок
        students_marks[student][class_] = marks  # students_marks['Александра']['Математика'] = [5, 5, 5]
# выводим получившийся словарь с оценками:
for student in students:
    print(f'''{student}
            {students_marks[student]}''')

print('''
        Список команд:
        1. Добавить оценки ученика по предмету
        2. Вывести средний балл по всем предметам по каждому ученику
        3. Вывести все оценки по всем ученикам
        4. Добавление предмета в список
        5. Вывод информации по всем оценкам по определенному ученику
        6. Удаление предмета
        7. Удаление ученика с его оценками
        8. Изменение предмета
        9. Добавление ученика в список
        10. Удалить оценку ученика по предмету
        11. Изменить оценку ученика по предмету
        12. Изменение имени ученика в списке
        13. Выход из программы
        ''')

while True:
    command = int(input('Введите команду: '))
    if command == 1:
        print('1. Добавить оценку ученика по предмету')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # считываем название предмета
        class_ = input('Введите предмет: ')
        # считываем оценку
        mark = int(input('Введите оценку: '))
        # если данные введены верно
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            # добавляем новую оценку для ученика по предмету
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        # неверно введены название предмета или имя ученика
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')

    elif command == 2:
        print('2. Вывести средний балл по всем предметам по каждому ученику')
        # цикл по ученикам
        for student_d in students:
            print(student_d)
            # цикл по предметам
            for class_d in classes:
                # находим сумму оценок по предмету
                marks_sum = sum(students_marks[student_d][class_d])
                # находим количество оценок по предмету
                marks_count = len(students_marks[student_d][class_d])
                # выводим средний балл по предмету
                print(f'{class_d} - {marks_sum // marks_count}')
            print()

    elif command == 3:
        print('3. Вывести все оценки по всем ученикам')
        # выводим словарь с оценками:
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_a in classes:
                print(f'\t{class_a} - {students_marks[student][class_a]}')
            print()

    elif command == 4:
            print('4. Добавление предмета в список')
            class_new = str(input('Введите название нового предмета: '))
            if class_new in classes:
                print('Указанный предмет уже есть в списке')
            else:
                classes.append(str(class_new))
                #Вывод списка предметов
                print(f' {classes}')
                for student in students:  # 1 итерация: student = 'Александра'
                   # если данные имеются в таблице
                    if student in students_marks.keys() and class_new in classes:
                        # добавляем новую оценку для ученика по предмету
                        mark = [random.randint(1, 5) for i in range(3)]  # генерируем список из 3х случайных оценок
                        students_marks[student][class_new] = mark
                        print(f'Для {student} по предмету {class_new} добавлена оценка {mark}')
                    else:
                        print('Указанные оценки не добавлены')

    elif command == 5:
            print('5. Вывод информации по всем оценкам по определенному ученику')
            student = input('Введите имя ученика: ')
            if student in students_marks.keys():
                for classes_s, marks_s in students_marks[student].items():
                    print(f'{classes_s} - {marks_s}')  #students_marks[student][classes_s]
                    print()
            else:
                print('Данного ученика нет в списке')

    elif command == 6:
        print('6. Удаление предмета')
        class_del = input('Введите предмет, который хотите удалить: ')
        if class_del in classes:
            inde = classes.index(class_del)
            classes.pop(inde)
            for student in students:
                del students_marks[student][class_del]
            print(f'Предмет {class_del} удален из списка')
        else:
            print('Данного предмета нет в списке')

    elif command == 7:
        print('7. Удаление ученика с его оценками')
        student = input('Введите ученика, которого хотите удалить: ')
        if student in students_marks:
            del students_marks[student]
            students.remove(student)
            print(f'Ученик {student} удален из списка')
        else:
            print('Указанного ученика нет в списке')

    elif command == 8:
        print('8. Изменение предмета')
        class_i = str(input('Введите предмет, который хотите изменить: '))
        class_new = str(input('Введите новое название предмета: '))
        index = classes.index(class_i)
       # students_marks_time = {}
        for student_f in students_marks:
            #Заносим старые данные в измененый предмет
            students_marks[student_f][class_new] = students_marks[student_f][class_i]
            del students_marks[student_f][class_i]
        classes.remove(class_i)
        classes.insert(index, class_new)
        print(f'Предмет {class_i} изменен на {class_new}')

    elif command == 9:
            print('9. Добавление ученика в список')
            new_student = input('Введите имя нового ученика: ')
            if new_student in students:
                print('Указанный ученик уже есть в списке')
            else:
                students.append(new_student)
                students_marks[new_student] = {}
               # students_marks[]
                for class_ in classes:  # 1 итерация: student = 'Александра'
                   # если данные имеются в таблице
                    if new_student in students and class_ in classes:
                        # добавляем новую оценку для ученика по предмету
                        mark = [random.randint(1, 5) for i in range(3)]  # генерируем список из 3х случайных оценок
                        students_marks[new_student][class_] = mark
                        print(f'Для {new_student} по предмету {class_} добавлена оценка {mark}')
                    else:
                        print('Указанные оценки не добавлены')

    elif command == 10:
            print('10. Удалить оценку ученика по предмету')
            # считываем имя ученика
            student = input('Введите имя ученика: ')
            # считываем название предмета
            class_ = input('Введите предмет: ')
            # считываем оценку
            print(f'У {student} по предмету {class_} выставлены оценки  {students_marks[student][class_]}')
            mark_del = int(input('Введите оценку которую необходимо удалить: '))
            # если данные введены верно
            if student in students_marks.keys() and class_ in students_marks[student].keys():
                 # разделяем оценки через переменную
                 points = students_marks[student][class_]
                 # удаляем оценку для ученика по предмету
                 points.remove(mark_del)
                 print(f''' Для {student} по предмету {class_} удалена оценка {mark_del}
                 Оставшиеся оценки у {student} = {students_marks[student][class_]} ''')
            # неверно введены название предмета или имя ученика
            else:
                print('ОШИБКА: неверное имя ученика или название предмета')

    elif command == 11:
        print('11. Изменить оценку ученика по предмету')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # считываем название предмета
        class_ = input('Введите предмет: ')
        # считываем оценку
        print(f'У {student} по предмету {class_} выставлены оценки  {students_marks[student][class_]}')
        #Считываем параметры для изменения оценки
        mark_del = int(input('Введите оценку которую необходимо изменить: '))
        mark_new = int(input('Введите оценку которую необходимо внести в журнал: '))
        # если данные введены верно
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            # разделяем оценки через переменную
            points = students_marks[student][class_]
            index_mark = points.index(mark_del)
            # изменяем оценку для ученика по предмету
            points.remove(mark_del)
            points.insert(index_mark, mark_new)
            print(f''' Для {student} по предмету {class_} изменена оценка {mark_del}
                    Оставшиеся оценки у {student} = {students_marks[student][class_]} ''')
            del points
        # неверно введены название предмета или имя ученика
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')

    elif command == 12:
            print('12. Изменение имени ученика в списке')
            rename_student = input('Введите имя ученика, которое необходимо изменить: ')
            i_student = input('Введите новое имя ученика: ')
            if i_student in students:
                print('Указанный ученик уже есть в списке')
            else:
                students.append(i_student)
                students_marks[i_student] = students_marks[rename_student]
                if rename_student in students_marks:
                    del students_marks[rename_student]
                    students.remove(rename_student)
            print(f'Для студента "{rename_student}" изменено имя на "{i_student}"')

    elif command == 13:
        print('13. Выход из программы')
        break