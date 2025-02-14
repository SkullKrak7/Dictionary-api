from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

df = pd.read_csv("dictionary.csv", sep=",")

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/api/v1/<word>/")
def api(word):
    define = df.loc[df['word'] == word]['definition'].squeeze()
    return {"word": word, "definition": define}


app.run(debug=True, port=5001)