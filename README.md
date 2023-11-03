# 50-chatgpt-projects
the code for 50 amazing ChatGPT projects for developers

## Environment Setup
1. Created a repo on [github](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) then in [vs code](https://code.visualstudio.com/download) I cloned it to my laptop
2. With [python 3.8.0](https://www.python.org/downloads/release/python-380/) installed I setup a python virtual environment with: 
    >```python -m venv venv_chatgpt```
3. Added venv_chatgpt to .gitignore and pushed changes to github

## Email Reply Generator
* Install Microsoft Outlook on your computer and setting up an email account.
* Install Libraries
>```pip install openai```

>```pip install pywin32```
* create a file called config.py and save the following into it:
> ```API_KEY = "<YOUR_CHATGPT_API_KEY>"```
* create a new file called app.py and place the following into it:
```python
import openai
import win32com.client
import tkinter as tk
import config

openai.api_key = config.API_KEY
```
* Launch Outlook and ensure you are signed in.