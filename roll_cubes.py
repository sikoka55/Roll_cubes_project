import random


def prnt_answer(cube: int):
    print('Ось твій результат:')
    print('*' * 9)
    print(random.randint(1, cube))
    print('*' * 9)



def roll(answer):
    if answer == 'd4':
        prnt_answer(4)

    elif answer == 'd6':
        prnt_answer(6)

    elif answer == 'd8':
        prnt_answer(8)

    elif answer == 'd10':
        prnt_answer(10)

    elif answer == 'd12':
        prnt_answer(12)

    elif answer == 'd20':
        prnt_answer(20)

    elif answer == 'd100':
        prnt_answer(100)


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