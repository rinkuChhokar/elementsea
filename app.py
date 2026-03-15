from flask import Flask, render_template, abort
import json
import os

app = Flask(__name__, template_folder='templates')
app.secret_key = 'elementdekho'

# Load elements data once
with open(os.path.join(os.path.dirname(__file__), 'static', 'elements_data.json'), 'r') as f:
    ELEMENTS = json.load(f)

# Build lookup maps
SYMBOL_MAP = {el['symbol'].lower(): el for el in ELEMENTS}
NUMBER_MAP = {el['number']: el for el in ELEMENTS}

@app.route("/")
def homepage():
    return render_template("home.html", elements=ELEMENTS)

@app.route("/element/<symbol>")
def element_detail(symbol):
    el = SYMBOL_MAP.get(symbol.lower())
    if not el:
        abort(404)
    prev_el = NUMBER_MAP.get(el['number'] - 1)
    next_el = NUMBER_MAP.get(el['number'] + 1)
    return render_template("element_detail.html", el=el, prev_el=prev_el, next_el=next_el)

@app.errorhandler(404)
def not_found(e):
    return render_template("home.html", elements=ELEMENTS), 404

if __name__ == "__main__":
    app.run(debug=True)
