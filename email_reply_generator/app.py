import openai
import win32com.client
import tkinter as tk
import config

openai.api_key = config.API_KEY

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

def reply():
    email = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI").GetDefaultFolder(6).Items.Item(selected_subject.get())
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        max_tokens=1024,
        n=1,
        messages=[
            {"role": "user", "content": "You are a professional email writer"},
            {"role": "assistant", "content": "Ok"},
            {"role": "user", "content": f"Create a reply to this email:\n {email.Body}"}
        ]
    )
    """
    reply = email.Reply()
    reply.Body = "hellow world" # response["choices"][0]["message"]["content"]
    reply.Display()
    return

# UI for email reply generator
#I access tkiniter's libary to create a base UI window
root = tk.Tk()
# I set the title and size of that window
root.title("Email Reply Generator")
root.geometry("300x300")

# called the method we created earlier to get the most recent 5 emails 
# and save the subject lines
email_subjects = last_five_emails()
selected_subject = tk.StringVar()

# Added the subject lines into a dropdown menu button
dropdown = tk.OptionMenu(root, selected_subject, *email_subjects)
dropdown.pack()

# labelled the button
label = tk.Label(root, text="Previous emails")
label.pack()

# Added button to call GPT and create a reply
button = tk.Button(root, text="Generate Reply", command=reply)
button.pack()

# I call the main tkinter UI to display it for the user
root.mainloop()