import requests
import sys 

try:
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    r = requests.get(url)
    data = r.json()
    usd_data = data['bpi']['USD']
    if len(sys.argv) <= 1:
        sys.exit("Missing command-line argument")
    # raise Exception("This line is never reached")
    output: float = float(usd_data['rate_float']) * float(sys.argv[1])
    print(f"amount: ${output:,.4f}")
except requests.RequestException:
    pass
except ValueError:
    sys.exit("Command-line argument is not a number")

