from flask import Flask, request, render_template #pip install flask
import openai #pip install openai
import config
openai.api_key = config.API_KEY

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()