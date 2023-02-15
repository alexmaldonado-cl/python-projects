#Ask user if they want to generate a password or not
#If yes, aks for password length
#Generate password
#Print password
#If initial response is not, exit program
import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_password():
    password_length = int(input("How long would you like your password to be? : "))
    random.shuffle(characters)

    password = []

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)

    print(password)


def run():
    option = input("Do you want to generate a password? (Yes/No): ")

    if(option.lower() == 'yes'):
        generate_password()
    elif option.lower() == 'no':
        print("Program ended")
        quit()
    else:
        print("Invalid input, please input Yes or Not")
        quit()



if __name__ == '__main__':
    run()