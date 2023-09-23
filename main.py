import first_task as letters
import second_task as insert

task_number = int(input('Enter task number: '))

while task_number < 1 or task_number > 2:
    print('Enter 1 or 2 pls >:')
    task_number = int(input('Enter task number: '))

if task_number == 1:
    letters.Letters(
        str(input('Enter something there: '))
    ).find_result_with_for()
elif task_number == 2:
    insert.Insert(
        str(input('Enter something there: ')),
        str(input('Enter combination after which we will insert: ')),
        str(input('Enter combination which we gonna insert: '))
    ).insert_string()
