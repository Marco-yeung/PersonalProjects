from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://free.currconv.com/"
API_KEY = "be280990bbe37c1a09c2"

printer = PrettyPrinter()

# ? is a query parameter, some data or parameter that are going to send to the URL

def get_currencies():
    endpoint = f"api/v7/currencies?apiKey={API_KEY}"
    url = BASE_URL + endpoint
    data = get(url).json()['results']
    # in order to let us sort the currency by aphabetical order, we need to convert dictionary into a list first
    # items() will give me a tuple that contains the key
    data = list(data.items())
    data.sort()

    return data

def print_currencies(currencies):
    for name, currency in currencies:
        name = currency['currencyName']
        _id = currency['id']
        # we are trying to get the currency symbol, if it does not return a symbol, it would return an empty string
        symbol = currency.get("currencySymbol", "")
        print(f"{name} - {_id} - {symbol}")

def exchange_rate(currency1, currency2):
    endpoint = f"api/v7/convert?q={currency1}_{currency2}&compact=ultra&apiKey={API_KEY}"
    url = BASE_URL + endpoint

    response = get(url)

    data = response.json()

    if len(data) == 0:
        print('Invalid currencies')
        return

    #return data would only give us the dictionary, data.values() would only give us the values but not the key from our DICT
    # return list(data.values())[0]
    # return data

    rate = list(data.values())[0]
    print(f"{currency1} -> {currency2} = {rate}")

    return rate

def convert(currency1, currency2, amount):
    rate = exchange_rate(currency1, currency2)
    if rate is None:
        return
    
    try:
        amount = float(amount)
    except:
        print("Invalid amount")
        return
    
    converted_amount = rate * amount
    print(f"{amount} {currency1} is equal to {converted_amount} {currency2}")


data = get_currencies()
print_currencies(data)
rate = exchange_rate('USD', 'HKD')
print(rate)

def main():
    currencies = get_currencies()

    print('Welcome to the currency converter')
    print('List - lists the differen currencies')
    print('Convert - convert from one currency to another')
    print("Rate - get the exchange rate of two currencies")

    while True:
        command = input("Enter a command (q to quit): ").lower()

        if command == 'q':
            break
        elif command == 'list':
            print_currencies(currencies)
        elif command == 'convert':
            currency1 = input("Enter the base currency: ").upper()
            amount = input(f"Enter an amount in {currency1}: ")

            currency2 = input("Enter a currency to convert to: ").upper()
            convert(currency1, currency2, amount)
        elif command == 'rate':
            currency1 = input("Enter a base currency: ").upper()
            currency2 = input("Enter a currency to convert to: ").upper()
            exchange_rate(currency1, currency2)

        else:
            print("Unrecognized command")
