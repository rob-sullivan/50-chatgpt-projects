# 50-chatgpt-projects

Code for 50 ChatGPT projects. [Get an email when finished](https://forms.gle/2963AjKGoU93Kc1t9).

## Getting Started with Python

Python is a versatile programming language that's great for beginners. This chapter will guide you through setting up Python and introduce you to its basic usage, including setting up a development environment with GitHub and virtual environments.

### 1. Installing Python

1. Download Python:
   - Go to the official Python website: [python.org](https://www.python.org/) and download the latest version for your operating system (Windows, macOS, or Linux).
2. Install Python
   - Open the downloaded installer.
   - Windows
     - Make sure to check the box that says "Add Python to PATH."
     - Click "Install Now."
   - Mac
     - Open the .pkg file and follow the instructions.
   - Linux
     - Use your package manager. For example, on Ubuntu, run
     ```
     sudo apt update
     sudo apt install python3
     ```

### 2. Setting Up a Code Editor

A code editor helps you write and manage your Python code efficiently. One of the most popular editors is Visual Studio Code (VS Code).

1. Download and Install VS Code:

   - Visit code.visualstudio.com and download the installer for your operating system.
   - Install the editor following the instructions on the website.

2. Install Python Extension for VS Code:
   - Open VS Code.
   - Go to the Extensions view by clicking the square icon on the sidebar or pressing **Ctrl+Shift+X**.
   - Search for "Python" and install the extension provided by Microsoft.

### 3. Setting Up a Python Development Environment

## Environment Setup

1. Created a repo on [github](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) then in [vs code](https://code.visualstudio.com/download) I cloned it to my laptop
2. With [python 3.8.0](https://www.python.org/downloads/release/python-380/) installed I setup a python virtual environment with:
   > `python -m venv venv_chatgpt`
3. Added venv_chatgpt to .gitignore and pushed changes to github
4. Activated python [virtual environment](https://docs.python.org/3/library/venv.html):
   > `.\venv_chatgpt\Scripts\activate`

## 1. Chatbot

In this project I create a clone of chatgpt using flask.

- Installed the following libraries in a vs code terminal (ensuring my venv is active!)
  > `pip install openai`

> `pip install flask`

- Created a file called config.py and save the following into it:
  > `API_KEY = "<YOUR_CHATGPT_API_KEY>"`

```python
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
    instructions = """This GPT must behave answering questions related to information found on revenue.ie website"""

    file_path = "cleaned_text_dataset.txt"
    with open(file_path, "r") as file:
        knowledge = file.read()

    userText = request.args.get('msg')
    #used to send a request to the ChatGPT API to generate the completion of the user’s input prompt.
    response = openai.ChatCompletion.create(
        model="gpt-4",
        #model = "gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": instructions},
            #{"role": "user", "content": knowledge}, #this will be loaded in as context for each query expensive tokens!
            {"role": "user", "content": userText},
        ]
    )
    answer = response["choices"][0]["message"]["content"]
    return str(answer)

if __name__ == "__main__":
    app.run()
```

## 2. Code Bug Fixer

## 3. Quiz Generator

## 4. Email Reply Generator

In this project ([demo](https://www.linkedin.com/posts/robssully_a-simple-chatgpt-email-reply-generator-activity-7127299322794135553-5GJI)) I automatically generate original replies to specific emails by integrating GPT-4 with Outlook API. We use Python 3.7, OpenAI API key, windows and Microsoft Office 365 Outlook for this project.

- Installed Microsoft Outlook on my computer and setup an email account.
- Installed the following libraries in a vs code terminal (ensuring my venv is active!)
  > `pip install openai`

> `pip install pywin32`

- Created a file called config.py and save the following into it:
  > `API_KEY = "<YOUR_CHATGPT_API_KEY>"`
- Created a new file called app.py and place the following into it:

```python
import openai
import win32com.client
import tkinter as tk
import config

openai.api_key = config.API_KEY
```

- Launched Outlook and ensured I was signed in, if I saw the outlook window which contained emails, etc, then I should be able to make API calls. I had issues where I was logged in under an old account. I kept getting error messages. Had to ensure I was completely signed out first then signed in with a student email. You can even create a new one to test with.
- Added the following to app.py:

```python
def last_five_emails():
    """Gets the last 5 email subjects from your Outlook and displays them."""

    # I create an object that gives us access to outlook
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    #I access emails in the inbox by getting the folder at index 6
    inbox = outlook.GetDefaultFolder(6)
    # Emails are items so I store them in messages
    messages = inbox.Items
    # I get the last subject line (aka the most recent) for each email chain
    emails = [messages.GetLast().Subject]
    # I set to 5 to get the last 5 emails
    email_number = 5
    for i in range(email_number):
        # There are other methods in win32com.
        # I chose GetPrevious to get the email that came before the most recent email in the chain
        emails.append(messages.GetPrevious().Subject)
    return emails #I return email subjects from this method
```

- Now that I can access the previous 5 emails I then build the UI for the email reply generator. I make use of builtin python UI libary called Tkinter and add the following to app.py:

```python
#I access tkiniter's libary to create a base UI window
root = tk.Tk()
# I set the title and size of that window
root.title("Email Reply Generator")
root.geometry("300x300")

# I call the method we created earlier to get the most recent 5 emails
# and save the subject lines
email_subjects = last_five_emails()
selected_subject = tk.StringVar()

# I add the subject lines into a dropdown menu button
dropdown = tk.OptionMenu(root, selected_subject, *email_subjects)
dropdown.pack()

# I label the button
label = tk.Label(root, text="Previous emails")
label.pack()

# I call the main tkinter UI to display it for the user
root.mainloop()

```

## 5. Presentation Generator

In this project ([demo](https://www.linkedin.com/posts/robssully_chatgpt-dalle-hackathon-activity-7130534652640923648-rgl5)) I automate PowerPoint presentation development by combining DALL-E art with ChatGPT’s human-like text to create presentation slides.

- Installed Microsoft Powerpoint on my computer and setup an email account.
- Installed the following libraries in a vs code terminal (ensuring my venv is active!)
  > `pip install python-pptx`

> `pip install openai`

> `pip install requests`

- Created a file called config.py and save the following into it:
  > `API_KEY = "<YOUR_CHATGPT_API_KEY>"`
- Created a new file called app.py and place the following into it:

```python
import collections.abc
import config
assert collections
import tkinter as tk
from pptx import Presentation
from pptx.util import Inches, Pt
import openai
from io import BytesIO
import requests

openai.api_key = config.API_KEY
```

- Added the following to app.py to create the GUI to allow users to generate powerpoint slides.

```python
#I first create the gui window for the user
app = tk.Tk()
app.title("Crate PPT Slides")
app.geometry("800x600")

# Create text field
text_field = tk.Text(app)
text_field.pack(fill="both", expand=True)
text_field.configure(wrap="word", font=("Arial", 12))
text_field.focus_set()

# Create the button to create slides
create_button = tk.Button(app, text="Create Slides", command=get_slides)
create_button.pack()
app.mainloop()
```

- Added the following to app.py above where I defined the Tkinter GUI. This allowed me to build functionality for creating the presentation and slides.

```python
def get_slides():
    # I get content from the text field starting from the first character to the last character, except the new line character.
    text = text_field.get("1.0", "end-1c")

    # I split text into paragraphs
    paragraphs = text.split("\n\n")

    # I initalise an empty powerpoint presentation
    prs = Presentation()
    width = Pt(1920)
    height = Pt(1080)
    prs.slide_width = width
    prs.slide_height = height
    # I loop through each text field paragraph and add them to the slides
    for paragraph in paragraphs:
        slide_generator(paragraph, prs)
    # Save with file name
    prs.save("chatgpt_presentation.pptx")
```

- Added the following to app.py above where I defined the get_slides(). This allowed me to build functionality for passing ChatGPT output to Dalle prompts.

```python
def slide_generator(text, prs):
    prompt = f"Summarize the following text to a DALL-E image generation prompt: \n {text}"

    model_engine = "gpt-4"
    dlp = openai.ChatCompletion.create(
        model=model_engine,
        messages=[
            {"role": "user", "content": "I will ask you a question"},
            {"role": "assistant", "content": "Ok"},
            {"role": "user", "content": f"{prompt}"}
        ],
        max_tokens=250,
        n=1,
        stop=None,
        temperature=0.8
    )

    dalle_prompt = dlp["choices"][0]["message"]["content"]
    dalle_prompt = dlp.choices[0].text
    response = openai.Image.create(
        prompt=dalle_prompt + " Style: digital art",
        n=1,
        size="1024x1024")
    image_url = response['data'][0]['url']
```

- Now I create slide headers and bullet points using Dall-E generated images and ChatGPT generated text.

```python

```

## 6. Document Translator

## 7. Essay Topic Generator

## 8. Voice Dictation (Speech-To-Text)

In this project I get chatgpt to transcribe my voice

## 9. Email Scraper

In this project I scape emails from linkedin by asking chatgpt to get me a list of [People] who work in [Industry]

## 10. Sports Reporter

In this project chatgpt will scrape sports websites to provide me a summary and scores on my favourite teams

## 11. Lyrics Explainer

In this project chatgpt will explain the meaning behind the lyrics to my favourite songs

## 12. Merge CSV or PDF files

In this project chatgpt will merge csv or pdf files for me

## 13. Spam Detector

## 14. Movie Explainer

In this project chatgpt will provide information about my favourite movies

## 15. Music Player

In this project I ask chatgpt to play my favourite music

## 16. News Reporter

In this project chatgpt will scrape and summerise the news for me.

## 17. Background Noise Filter

In this project I give chatgpt audio files and ask it to reduce the background noise.

## 18. Financial Stock Analyst

In this project chatgpt will provide me basic information on stocks I'm interested in.

## 19. Guess Numbers Game

In this project I have to guess chatgpt's chosen numbers.

## 20. Password Generator

In this project chatgpt creates secure passwords for me.

## 21. Document/Image to Text Reader (Text-To-Speech)

In this project chatgpt gets text from images or documents and reads them back to me.

- First I install gTTS
  > `pip install gTTS`
- Then to play speech we generate I use playsound
  > `pip install playsound`
- I test that the text to speech is working

```python
from gtts import gTTS
import playsound

text_to_speech = "Hello, this is an example of using gTTS in Python."
tts = gTTS(text=text_to_speech, lang='en')
tts.save("example.mp3")

# Play the generated audio using playsound
playsound.playsound("example.mp3")
```
