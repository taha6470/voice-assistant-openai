import speech_recognition as sr 
import pyttsx3
import openai

openai.api_key = "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"

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voices",voices[0].id)
r = sr.Recognizer()
mic = sr.Microphone(device_index=1)

conversation = ""
user_name = "Taha"
bot_name = "Hamza the noob"

while True: 
    with mic as source:
        print("\n listening....")
        r.adjust_for_ambient_noise(source,duration=0.2)
        audio = r.listen(source)
    print("\n No longer listening.")

    try:
        user_input = r.recognize_google(audio)
    except:
        continue
    
    prompt = user_name+":"+user_input+"\n"+bot_name+":"
    conversation+=prompt

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=conversation,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    response_str = response["choices"][0]["text"].replace("\n","")
    response = response_str.split(
        user_name + ":" ,1)[0].split(bot_name+":",1)[0]

    conversation += response_str + "\n"
    print(response_str)
    engine.say(response_str)
    engine.runAndWait()
