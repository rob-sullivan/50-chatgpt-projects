import collections.abc
import config
assert collections
import tkinter as tk
from pptx import Presentation
from pptx.util import Inches, Pt
import openai
from io import BytesIO
import requests
# API Token
openai.api_key = config.API_KEY

def get_slides():
    text = text_field.get("1.0", "end-1c")
    paragraphs = text.split("\n\n")
    prs = Presentation()
    width = Pt(1920)
    height = Pt(1080)
    prs.slide_width = width
    prs.slide_height = height
    for paragraph in paragraphs:
        slide_generator(paragraph, prs)
    prs.save("my_presentation.pptx")

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