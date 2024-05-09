# imported python currency conversion library
from forex_python.convertor import CurrencyRates

# function to perform currency conversion
def convertCurrency(amount, fromCurrency, toCurrency):
    c = CurrencyRates()
    convertedAmount = c.convert(fromCurrency, toCurrency, amount)
    return convertedAmount

# function testing
convertedAmount = convertCurrency(100, 'USD', 'EUR')
print(convertedAmount)

