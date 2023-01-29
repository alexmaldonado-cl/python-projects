def add(a, b):
    answer = a + b
    print(f"{str(a)} + {str(b)} = {str(answer)}")


def sub(a, b):
    answer = a - b
    print(f"{str(a)} - {str(b)} = {str(answer)}")


def mul(a, b):
    answer = a * b
    print(f"{str(a)} * {str(b)} = {str(answer)}")

def div(a, b):
    answer = a / b
    print(f"{str(a)} / {str(b)} = {str(answer)}")


def userOptions():
    while True:
        print("A. Addition")
        print("B. Subtraction")
        print("C. Multiplication")
        print("D. Division")
        print("E. Exit")

        choice = input("Input your choice: ")

        if choice == 'a' or choice == 'A':
            a = int(input('Input first number: '))
            b = int(input('Input second number: '))
            add(a, b)
        elif choice == 'b' or choice == 'B':
            a = int(input('Input first number: '))
            b = int(input('Input second number: '))
            sub(a, b)
        elif choice == 'c' or choice == 'C':
            a = int(input('Input first number: '))
            b = int(input('Input second number: '))
            mul(a, b)
        elif choice == 'd' or choice == 'D':
            a = int(input('Input first number: '))
            b = int(input('Input second number: '))
            div(a, b)
        elif choice == 'e' or choice == 'E':
            print('Program ended')
            quit()
            

def run():
    userOptions()

#* Entry point
if __name__ == '__main__':
    run()