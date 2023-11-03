# 50-chatgpt-projects
the code for 50 amazing ChatGPT projects for developers

## Environment Setup
1. Created a repo on [github](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) then in [vs code](https://code.visualstudio.com/download) I cloned it to my laptop
2. With [python 3.8.0](https://www.python.org/downloads/release/python-380/) installed I setup a python virtual environment with: 
    >```python -m venv venv_chatgpt```
3. Added venv_chatgpt to .gitignore and pushed changes to github
4. Activated python [virtual environment](https://docs.python.org/3/library/venv.html):
    >```.\venv_chatgpt\Scripts\activate```

## Email Reply Generator
In this project I automatically generate original replies to specific emails by integrating GPT-4 with Outlook API. We use Python 3.7, OpenAI API key, windows and Microsoft Office 365 Outlook for this project.

* Installed Microsoft Outlook on my computer and setup an email account.
* Installed the following libraries in a vs code terminal (ensuring my venv is active!)
>```pip install openai```

>```pip install pywin32```
* Created a file called config.py and save the following into it:
> ```API_KEY = "<YOUR_CHATGPT_API_KEY>"```
* Created a new file called app.py and place the following into it:
```python
import openai
import win32com.client
import tkinter as tk
import config

openai.api_key = config.API_KEY
```
* Launched Outlook and ensured I was signed in, if I saw the outlook window which contained emails, etc, then I should be able to make API calls. I had issues where I was logged in under an old account. I kept getting error messages. Had to ensure I was completely signed out first then signed in with a student email. You can even create a new one to test with.
* Added the following to app.py:
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
* Now that I can access the previous 5 emails I then build the UI for the email reply generator. I make use of builtin python UI libary called Tkinter and add the following to app.py:
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