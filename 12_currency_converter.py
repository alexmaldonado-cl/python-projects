
converter_to_pounds = lambda dollars: format(dollars * 0.82, '.2f')

def main():
    print("="*50)
    print("CONVERTER US DOLLARS TO POUNDS STERLING")
    print("="*50)
    print(" ")

    dollars = eval(input("Enter amount in dollars: "))
    
    pounds = converter_to_pounds(dollars)

    print(f"That is {pounds} pounds")

if __name__ == '__main__':
    main()