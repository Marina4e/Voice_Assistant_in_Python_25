import time
import random
import requests
from output import say, engine
import speech_recognition as sr
# import openai
# from key import key


def get_time(text: str):
    current_time = time.localtime()

    output_time = f'{current_time.tm_hour}:{current_time.tm_min}'

    return {"time": output_time}

def get_random_number(text: str):
    return {"number": random.randint(0, 100)}

def get_random_flip(text: str):
    variants = ["heads", "tails"]
    winner = random.choice(variants)
    if winner == "heads":
        return {"side_win": "heads", "side_loos": "tails"}
    else:
        return {"side_loos": "tails"}

def get_dollar_currency(text: str):
    result = requests.get("https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5")
    result = result.json()
    total = str(round(float(result[1]['sale']), 2))
    total = total.split('.')
    return {"paper": total[0], "coin": total[1]}

def game(text: str):
    recognizer = sr.Recognizer()
    say("Okay, let's play, I've guessed a number from 1 to 100, your task is to guess it, say the end if you want to end the game")
    correct_number = random.randint(0, 100)
    with sr.Microphone() as source:
        print('ready game')
        while True:
            engine.runAndWait()
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            try:
                text = recognizer.recognize_google(audio, language='en-US')
                print(f"You said: {text}")
                if text.isdigit():
                    number_user = int(text)
                    if number_user == correct_number:
                        say("You guessed correctly")
                        break
                    elif number_user < correct_number:
                        say(f"Try again, my number is higher than {number_user}")
                    elif number_user > correct_number:
                        say(f"Try again, my number is lower than {number_user}")
                elif "end" in text:
                    break
                else:
                    say("Say a number, nothing else")
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError:
                print("request error")
            except sr.WaitTimeoutError:
                print("wait timeout")
    return {}

# def ai(text: str):
#     prompt = f'''You have to generate answers for the voice assistant, without unnecessary text,
#     everything you generate I will immediately send to the user in the form of sound
#     let's give SHORT answers, no need to fully reveal the topic
#     Below I provide what the user asks
#
#     {text}
#     '''
#     response = openai.Completion.create(
#         model="gpt-4o-mini",
#         messages=[
#             {"role": "user", "content": prompt}
#         ]
#     )
#     return {"text": response["choices"][0]["message"]["content"].strip()}
