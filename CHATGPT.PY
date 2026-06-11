from openai import OpenAI


import os
client= OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

prompt = ""

while True:
    prompt = input("You:")

    chat_completion= client.chat.completions.create(

        messages=[
            
            {
                "role" : "user",
                "content" : prompt
                
            }
        ],

        model= "gpt-4o-mini"
    )
    
    response_message = chat_completion.choices[0].message.content

    print("AI :",response_message)


