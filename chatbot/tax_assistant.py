#pip install flask
from flask import Flask, request, render_template
import openai
import config
openai.api_key = config.API_KEY

app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    instructions = """This GPT must behave answering questions related to information found on revenue.ie website, 
    the text file contains javascript and some repeated sentences related to cookie policy, these should be 
    ignored when providing answers, answer this as Eamon De Valera, keep his inclusion to one sentence, make it warm and witty. 
    After answering these questions end it with, '<br /><br />Please be aware that while AI strives for accuracy, it can sometimes produce incorrect 
    or misleading information. Only use this as a guide and not as the sole basis for any decisions, as we cannot accept liability 
    for the outcomes of such decisions.' then add this below '<br /><br />If  you found this helpful then click the link to sign up for 
    a free account and never waste time paying taxes again! <br ><br ><a href="https://forms.gle/MV3E7DMKkhSTWNxh6" target="_blank">Sign Up</a>'"""

    file_path = "cleaned_irish_tax_revenue_info.txt"
    with open(file_path, "r") as file:
        knowledge = file.read()

    userText = request.args.get('msg')
    #used to send a request to the ChatGPT API to generate the completion of the user’s input prompt.
    response = openai.ChatCompletion.create(
        #model="gpt-4",
        model = "gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": instructions},
            #{"role": "user", "content": knowledge},
            {"role": "user", "content": userText},
        ]
    )
    answer = response["choices"][0]["message"]["content"]
    return str(answer)

if __name__ == "__main__":
    app.run()