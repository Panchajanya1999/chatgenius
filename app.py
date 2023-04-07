######################################
##
##  ChatBot using OpenAI
##
######################################

import os
import openai as opai
import gradio as gr

opai.api_key = os.getenv("OPENAI_API_KEY")

# make prompt accept command line argument
# prompt = input("Enter prompt: ")
# setup a function that accepts propmpt and returns a response using "gpt-3.5-turbo" model

def chatbot(prompt, temperature = 0.2):
    response = opai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        max_tokens = 512,
        temperature = temperature,
        frequency_penalty = 0,
        presence_penalty = 0.6,
        messages = [
            {"role": "user", "content": prompt}
]
    )
    return response['choices'][0]['message']['content']

# test the function
demo = gr.Interface(
    fn = chatbot, 
    inputs = [gr.Textbox(lines=5, label="Prompt", placeholder="Enter prompt here", info = "Enter a prompt and the chatbot will generate a response."), gr.Slider(0, 1, 0.2, step = 0.1, label="Temperature", info = "The higher the temperature, the more creative the response will be.")],
    outputs = gr.Textbox(label="Response", lines=10), 
    title = "ChatGenius - An OpenAI self-tuned chatbot based on GPT-3.5 Turbo", 
    description = "Enter a prompt and the chatbot will generate a response.",
    theme=gr.themes.Monochrome()
)
demo.launch(share=False)
