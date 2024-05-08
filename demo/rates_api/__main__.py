from rates_api.api_server import api_server
from rates_api.rates_app import start_rates_api
import requests

def main() -> None:
    health_check_url = "http://127.0.0.1:8900/check"

    with api_server(health_check_url, start_rates_api):
        resp = requests.get("http://127.0.0.1:8900/api/2021-02-01?base=USD&symbols=EUR")
        print(resp.json())
        

if __name__ == "__main__":
    main()
