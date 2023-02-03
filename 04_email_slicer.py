# 1 - collect email from user
# 2 - split the email usgin @, the first part as the user name, the seconf part is gonna be saved as domain
# 3 - split domain using .,

def printHeader():
    print(" " * 20)
    print("#" * 5, "WELCOME TO THE EMAIL SLICER", "#" * 5)
    print(" " * 20)


def main():
    printHeader()

    email_input = input('Input your email address: ')

    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")

    print("Username: ", username)
    print("Domain: ", domain)
    print("Extension: ", extension)

if __name__ == '__main__':
    main()