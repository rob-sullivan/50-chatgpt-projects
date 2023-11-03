import openai
import win32com.client
import tkinter as tk
import config

openai.api_key = config.API_KEY

def last_five_emails():
    """Gets the last 5 email subjects from your Outlook and displays them."""
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    inbox = outlook.GetDefaultFolder(6)
    messages = inbox.Items
    emails = [messages.GetLast().Subject]
    email_number = 5
    for i in range(email_number):
        emails.append(messages.GetPrevious().Subject)
    return emails


# UI for email reply generator
root = tk.Tk()
root.title("Outlook Emails")
root.geometry("300x300")

email_subjects = last_five_emails()
selected_subject = tk.StringVar()

dropdown = tk.OptionMenu(root, selected_subject, *email_subjects)
dropdown.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()