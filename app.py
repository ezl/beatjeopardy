from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    output = "Hello World"
    json = request.get_json()
    json = str(json)
    return output + json

if __name__ == "__main__":
    app.run()
