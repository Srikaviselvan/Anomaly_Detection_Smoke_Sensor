from openai import OpenAI
import pandas as pd
import discord
import pandas as pd
import json

with open("credentials.json", "r") as json_file:
    credentials = json.load(json_file)

def get_response(client, training_data):
    response = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages = training_data,
    temperature=1,
    top_p=1,
    frequency_penalty=0.6,
    presence_penalty=0
    )

    return response

def get_training_data(training_file):
    
    data = pd.read_excel(training_file)

    dict_list = data.to_dict(orient='records')

    return dict_list

def update_training_data(old_data, new_data):

    old_data.extend(new_data)

    updated_data = pd.DataFrame(old_data)

    updated_data.to_excel("Speech Training.xlsx", index=False)



def initialize_training_file(initial_data):

    data = pd.DataFrame(initial_data)
    data.to_excel("Speech Training.xlsx", index = False)

    
ai_client = OpenAI(api_key = credentials['openai_key'])

data = {'role': ['system'], 'content': ['You are an assistant who helps with malfunctioning equipment.']}

initialize_training_file(initial_data = data)



maintenance_assistant_client = discord.Client(intents = discord.Intents.all())

@maintenance_assistant_client.event
async def on_ready():
    
    channel = maintenance_assistant_client.get_channel(1217350511553155113)


@maintenance_assistant_client.event
async def on_message(message):
        
    if not message.author.bot:
    
        training_data = get_training_data(training_file = "Speech Training.xlsx")

        chat_prompt = message.content

        new_data = [{'role': 'user', 'content': chat_prompt}]

        update_training_data(old_data = training_data, new_data = new_data)

        training_data = get_training_data(training_file = "Speech Training.xlsx")

        response = get_response(client = ai_client, training_data = training_data).choices[0].message.content

        new_data = [{'role': 'assistant', 'content': response}]

        update_training_data(old_data = training_data, new_data = new_data)

        await message.channel.send(response)

maintenance_assistant_client.run(credentials['discord_maintenance_client_token'])


