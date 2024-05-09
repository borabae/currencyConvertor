# imported python currency conversion library
from forex_python.converter import CurrencyRates

# function to perform currency conversion
def convertCurrency(amount, fromCurrency, toCurrency):
    c = CurrencyRates()
    convertedAmount = c.convert(fromCurrency, toCurrency, amount)
    return convertedAmount

# function testing
convertedAmount = convertCurrency(100, 'USD', 'EUR')
print(convertedAmount)

# user interaction
def main():
    amount = float(input("Enter amount: "))
    fromCurrency = input("From currency: ").upper()
    toCurrency = input("To currency: ").upper()

    convertedAmount = convertCurrency(amount, fromCurrency, toCurrency)
    print(f"{amount} {fromCurrency} is equal to {convertedAmount: .2f} {toCurrency}")

if __name__ == "__main__":
    main()