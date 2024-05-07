from flask import Flask, Response, jsonify

def main() -> None:
    app = Flask(__name__)

    @app.route("/")
    def hello_world() -> Response:
        return jsonify({"message":"hellow, world!"})

    app.run(port=8900)

if __name__ == "__main__":
    main()