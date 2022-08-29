import random


def roll (answer):
    if answer == 'd4':
        print('Ось твій результат:')
        print('*' * 9)
        print(random.randint(1, 5), sep='')
        print('*' * 9)

    elif answer == 'd6':
        print('Ось твій результат:')
        print('*' * 9)
        print(random.randint(1, 7), sep='')
        print('*' * 9)

    elif answer == 'd8':
        print('Ось твій результат:')
        print('*' * 9)
        print(random.randint(1, 9), sep='')
        print('*' * 9)

    elif answer == 'd10':
        print('Ось твій результат:')
        print('*' * 9)
        print(random.randint(1, 11), sep='')
        print('*' * 9)

    elif answer == 'd12':
        print('Ось твій результат:')
        print('*' * 9)
        print(random.randint(1, 13), sep='')
        print('*' * 9)

    elif answer == 'd20':
        print('Ось твій результат:')
        print('*' * 9)
        print(random.randint(1, 21), sep='')
        print('*' * 9)

    elif answer == 'd100':
        print('Ось твій результат:')
        print('*' * 9)
        print(random.randint(1, 101), sep='')
        print('*' * 9)


print('Привіт,мандрівник!')
print('Я бачу, у тебе є потреба у роллі кубика')
print('Який кубик тобі потрібно кинути?')
print()
print('d4,d6,d8,d10,d12,d20,d100 - обери свій и введи назву')
print()


while True:
    answer = input()
    if answer not in ['d4', 'd6', 'd8', 'd10', 'd12', 'd20', 'd100']:
        print('Обери кубик! Годі колупатися у носі!')

    else:
        print('Оце так! Ти вибрав', answer)
        roll(answer)

        print()
        print('Хочеш зробити ще один бросок? Напиши "так" або "ні"')
        answr_again = input()
        if answr_again.lower() == 'так':
            print('Який кубик будеш кидати?')
            continue
        else:
            print('Заходь, якщо що!')
            exit_user = input()
            break