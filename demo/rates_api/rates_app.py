from flask import Flask, Response, jsonify
from pathlib import Path
from rates_api.rates_app import load_rates

def main() -> None:
    app = Flask(__name__)

    rates_file_path = Path("../rates.csv")
    rates = load_rates(rates_file_path)

    @app.route("/")
    def hello_world() -> Response:
        return jsonify({"message":"hellow, world!"})
    
    @app.route("/check")
    def health_check() -> str:
        return "READY"
    
    @app.route("/api/<rate_date>")
    def rates_by_date(rate_date: str) -> Response:
        return jsonify({})

    app.run(port=8900)

if __name__ == "__main__":
    main()