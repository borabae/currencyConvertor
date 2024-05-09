from forex_python.convertor import CurrencyRates

def convertCurrency(amount, fromCurrency, toCurrency):
    c = CurrencyRates()
    convertedAmount = c.convert(fromCurrency, toCurrency, amount)
    return convertedAmount

