from flask import Flask, Response, abort, jsonify, request
from pathlib import Path
from rates_api.rates_data import load_rates
import math

def main() -> None:
    app = Flask(__name__)

    rates_file_path = Path("rates_api/rates.csv")
    rates = load_rates(rates_file_path)

    @app.route("/")
    def hello_world() -> Response:
        return jsonify({"message":"hellow, world!"})
    
    @app.route("/check")
    def health_check() -> str:
        return "READY"
    
    #sample request
    #http://127.0.0.1:8900/api/2021-04-09?base=INR&symbols=USD,EUR
    @app.route("/api/<rate_date>")
    def rates_by_date(rate_date: str) -> Response:
        #print(rate_date)
        for rate in rates:
            #print(rate)
            if rate["Date"] == rate_date:
                # get url option base, if not found then default to EUR
                base_country = request.args.get("base", "EUR")
                #print(base_country)

                if "symbols" in request.args:
                    country_symbols = request.args["symbols"].split(",")
                else:
                    country_symbols = [col for col in rate if col != "Date"]

                #print(rate.items())

                country_rates = {
                    country_code: country_rate / rate[base_country]
                    for (country_code, country_rate) in rate.items()
                    if country_code != "Date"
                    and country_code in country_symbols
                    and not math.isnan(country_rate)
                }

                return jsonify(
                    {
                        "date": rate["Date"],
                        "base": base_country,
                        "rates": country_rates
                    }
                )

        abort(404)
        
    app.run(port=8900)

if __name__ == "__main__":
    main()