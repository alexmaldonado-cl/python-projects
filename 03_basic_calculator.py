def get_options():
    return {
        'A': {
            'name'     : "Addition",
            'operation': add
        },
        'B': {
            'name': "Subtraction",
            'operation': sub
        },
        'C': {
            'name': "Multiplication",
            'operation': mul
        },
        'D': {
            'name': "Division",
            'operation': div
        },
        'E': {
            'name': "Exit",
            'operation': False
        }
    }

def add(a, b):
    answer = a + b
    print(" " * 20)
    print("#" * 5, "RESULT", "#" * 5)
    print(f"{str(a)} + {str(b)} = {str(answer)}")


def sub(a, b):
    answer = a - b
    print(" " * 20)
    print("#" * 5, "RESULT", "#" * 5)
    print(f"{str(a)} - {str(b)} = {str(answer)}")


def mul(a, b):
    answer = a * b
    print(" " * 20)
    print("#" * 5, "RESULT", "#" * 5)
    print(f"{str(a)} * {str(b)} = {str(answer)}")

def div(a, b):
    answer = a / b
    print(" " * 20)
    print("#" * 5, "RESULT", "#" * 5)
    print(f"{str(a)} / {str(b)} = {str(answer)}")

def exits_user_choice(choice, options):
    return True if (choice in options) else False

def printHeader():
    print(" " * 20)
    print("#" * 5, "BASIC CALCULATOR", "#" * 5)
    print(" " * 20)

def userOptions():
    while True:
        printHeader()
        options = get_options()
        for index, option in options.items():
            print(f"{index}. {option['name']}")


        choice = input("Input your choice: ")
        choice = choice.upper();

        if(exits_user_choice(choice, options)):
            operation = options[choice]['operation']

            if(operation == False):
                print(" " * 20)
                print("*" * 15, "PROGRAM ENDED", "*" * 15,)
                print(" " * 20)
                quit()

            try:
                a = int(input('Input first number: '))
                b = int(input('Input second number: '))
                operation(a, b)
            except Exception as e:
                print(e)
                print(" " * 20)
                print("!" * 5, "Error. Try again.", "!" * 5,)

        else:
            print(" " * 20)
            print("!" * 5, "Incorrect Option. Try again.", "!" * 5,)

def run():
    userOptions()

#* Entry point
if __name__ == '__main__':
    run()