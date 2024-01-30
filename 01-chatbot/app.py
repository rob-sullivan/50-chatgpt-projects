from flask import Flask, request, render_template #pip install flask
import openai #pip install openai
import config
openai.api_key = config.API_KEY

app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    instructions = """You are a tax assistant, when the user first interacts ask the user to describe themself to understand what tax they should pay and what expenses they can claim for."""

    #file_path = "cleaned_text_dataset.txt"
    #with open(file_path, "r") as file:
    #    knowledge = file.read()

    userText = request.args.get('msg')
    #used to send a request to the ChatGPT API to generate the completion of the user’s input prompt.
    response = openai.ChatCompletion.create(
        model="gpt-4",
        #model = "gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": instructions},
            {"role": "assistant", "content": "all responses should be in html format inside a div"},
            #{"role": "user", "content": knowledge}, #this will be loaded in as context for each query expensive tokens!
            {"role": "user", "content": userText},
        ]
    )
    answer = response["choices"][0]["message"]["content"]
    return str(answer)

if __name__ == "__main__":
    app.run()