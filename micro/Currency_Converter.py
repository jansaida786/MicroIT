
from forex_python.converter import CurrencyRates

def currency_converter():
    c = CurrencyRates()
    
    print("Currency Converter")
    print("------------------")
    
    from_currency = input("Enter the currency to convert from (e.g. USD, EUR, JPY): ").upper()
    to_currency = input("Enter the currency to convert to (e.g. USD, EUR, JPY): ").upper()
    amount = float(input("Enter the amount to convert: "))
    
    try:
        result = c.convert(from_currency, to_currency, amount)
        print(f"{amount} {from_currency} = {result} {to_currency}")
    except Exception as e:
        print(f"An error occurred: {e}")

currency_converter()
