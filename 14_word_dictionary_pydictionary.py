from PyDictionary import PyDictionary

dictionary = PyDictionary()



def main():

    while True:

        word = input("Enter a word: ").lower()

        if word == "":
            break

        print(dictionary.meaning(word))


if __name__ == "__main__":
    main()