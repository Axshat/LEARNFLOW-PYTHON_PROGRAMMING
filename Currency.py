import requests

def get_exchange_rate(from_currency, to_currency):
    api_key = '9fa9ca6978b3900cbb869b35'  
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}"
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Failed to get exchange rates")
        return None
        
    data = response.json()
    if 'conversion_rates' not in data:
        print("Invalid response from the API")
        return None
    
    rates = data['conversion_rates']
    if to_currency not in rates:
        print(f"Exchange rate for {to_currency} not found")
        return None
    
    return rates[to_currency]

def convert_currency(amount, from_currency, to_currency):
    rate = get_exchange_rate(from_currency, to_currency)
    if rate is None:
        print("Conversion failed")
        return None
    return amount * rate

def currency_converter():
    print("Welcome to the Currency Converter")
    
    amount = float(input("Enter the amount to convert: "))
    from_currency = input("Enter the currency to convert from (e.g., USD): ").upper()
    to_currency = input("Enter the currency to convert to (e.g., EUR): ").upper()
    
    converted_amount = convert_currency(amount, from_currency, to_currency)
    if converted_amount is not None:
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")

if __name__ == "__main__":
    currency_converter()
