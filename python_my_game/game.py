import random

words_list = ('программист', 'компьютер', 'код', 'мышь',
              'клавиатура', 'ноутбук', 'программа', 'сайт')

secret_word = random.choice(words_list)


gamer_word = ['*'] * len(secret_word)
print(''.join(gamer_word))

errors_counter = 0
while True:
    letter = input('Введите одну русскую букву: ').lower()

    if letter in secret_word:
        for idx, symbol in enumerate(secret_word):
            if symbol == letter:
                gamer_word[idx] = letter
        if '*' not in gamer_word:
            print('Вы выиграли!!!')
            print(f'Было загадано слово: {secret_word.upper()}')
            print('Сыграйте еще разок!')
            break
    else:
        errors_counter += 1
        print('Ошибок допущено:', errors_counter)
        if errors_counter == 8:
            print('Вы проиграли :(')
            print('Попробуйте снова.')
            break
    print(''.join(gamer_word))