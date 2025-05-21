import os
from dotenv import load_dotenv
import google.generativeai as genai
import pyttsx3

load_dotenv()
api_key = os.getenv('API_KEY')

genai.configure(api_key=api_key)

model = genai.GenerativeModel(model_name='gemini-1.5-flash')
chat = model.start_chat()

chat.send_message("From now on, act as Jarvis: a witty, intelligent, and humorous AI assistant inspired by Iron Man's Jarvis. You help users clearly, with a bit of humor. Understand?")

engine = pyttsx3.init()

print('Welcome! I am Jarvis, your virtual assistant. Type "q" to quit.')

while True:
    user_input = input("\nYou: ")
    if user_input.lower().strip() == 'q':
        print('Jarvis exiting.....Goodbye!')
        engine.say("Jarvis exiting... Goodbye!")
        engine.runAndWait()
        break

    response = chat.send_message(user_input)
    print(f"\nJarvis: {response.text}")
    engine.say(response.text)
    engine.runAndWait()
