from flask import Flask, jsonify

app = Flask(__name__, static_folder="static")


@app.route('/')
def index():
    index = open("static/population.html", "r")
    page = index.read()
    index.close()
    return page


app.run(debug=True, host='ithub-ai.ru', port=1199)