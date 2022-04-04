def compound()

investment = int(input('Enter a principal investment amount: '))
interestRate = (input('Enter an interest rate (0-100): '))
years = int(input('Enter duration of investment: '))

interestRate = (int(interestRate) / 100) + 1
investmentValue = investment * interestRate ** years

print(investmentValue)