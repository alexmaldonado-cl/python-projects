
def main():
    print("This is a monthly payment loan calculator")
    print(" ")

    principal = float(input("Input the loan amount: "))
    apr = float(input("Input the anuual interest rate: "))
    years = int(input("Input amount of years: "))

    monthly_interest_rate = apr / 1200
    amount_of_months = years * 12
    monthly_payment = principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-amount_of_months))

    monthly_payment = format(monthly_payment, '.2f')

    print(f"The monthly payment for this loan is: {monthly_payment}")

if __name__ == '__main__':
    main()