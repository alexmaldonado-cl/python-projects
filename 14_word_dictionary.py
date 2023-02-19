def main():
    word_dictionary = {
        'hi': 'a way of gretting',
        'eyes': 'an organ for seeing',
        'earth': 'a planet in space',
    }

    while True:

        word = input("Enter a word: ").lower()

        if word == "":
            break

        if word in word_dictionary:
            print(word, ":", word_dictionary[word])


if __name__ == "__main__":
    main()