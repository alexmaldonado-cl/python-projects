def replace_word(str):
    print("="* 30, 'CURRENT TEXT', "="* 30)
    print(str)
    print("="* 74,)
    word_to_replace = input('Enter the word to replace: ')
    word_replacement = input('Enter the word replacement: ')
    print("="* 31, 'FINAL TEXT', "="* 31)
    print(str.replace(word_to_replace, word_replacement))


def run():
    replace_word('Hi guys, i am Alex, and hi hi hi hi hi')

if __name__ == '__main__':
    run()