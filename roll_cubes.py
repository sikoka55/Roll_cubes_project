import random


def prnt_answer(answer: int):
    print('Ось твій результат:')
    print('♥' * 9)
    print(' '*3, random.randint(1, answer))
    print('♥' * 9)


print('Привіт,мандрівник!')
print('Я бачу, у тебе є потреба у роллі кубика')
print()
print('Який кубик тобі потрібно кинути?')
print()
print('к4,к6,к8,к10,к12,к20,к100 - обери свій и введи назву ')
print()


while True:
    answer = input()
    if answer not in ['к4', 'к6', 'к8', 'к10', 'к12', 'к20', 'к100']:
        print('Обери кубик! Годі колупатися у носі!')

    else:
        print('Оце так! Ти вибрав', answer)
        answer = int(answer[1:])
        prnt_answer(answer)

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