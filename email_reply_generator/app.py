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

# UI for email reply generator
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