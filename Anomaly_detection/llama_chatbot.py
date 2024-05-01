import os
import replicate
import pandas as pd
import json
import discord

with open("credentials.json", "r") as json_file:
    credentials = json.load(json_file)

os.environ["REPLICATE_API_TOKEN"] = credentials["replicate_key"]



def get_training_data(training_file):
    
    data = pd.read_excel(training_file)

    dict_list = data.to_dict(orient='records')

    return dict_list

def update_training_data(training_file, old_data, new_data):

    old_data.extend(new_data)

    updated_data = pd.DataFrame(old_data)

    updated_data.to_excel(training_file, index=False)



def initialize_training_data(training_file, initial_data):

    data = pd.DataFrame(initial_data)
    data.to_excel(training_file, index = False)


def get_context(training_file):

    data = pd.read_excel(training_file)

    context = ""

    for index in range(data.shape[0]):

        role = str(data['role'][index])
        content = data['content'][index]

        if role != "nan":
            context += role + " : "
        
        context += content + "\n"
    
    return context



def get_response(context):

    output_generator = replicate.run('a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5', # LLM model
                            input={"prompt": context,
                            "temperature":0.1, "top_p":0.9,  "repetition_penalty":1})


    response_text = ""

    for output in output_generator:
        response_text += output
        

    return response_text


maintenance_assistant_client = discord.Client(intents = discord.Intents.all())

@maintenance_assistant_client.event
async def on_ready():
    
    global training_file

    training_file = "Speech Training.xlsx"


    data = {"role": [''], 'content': ["Please respond to the message without prefixing your role. You are an assistant tasked with providing assistance for malfunctioning equipment."

    ]}

    initialize_training_data(training_file = training_file, initial_data = data)

@maintenance_assistant_client.event
async def on_message(message : discord.message.Message):
        
    if not message.author.bot:
    
        prompt = message.content

        old_data = get_training_data(training_file = training_file)
        new_data = [{'role': 'User', 'content': prompt}]
        update_training_data(training_file = training_file, old_data = old_data, new_data = new_data)

        response = get_response(context = get_context(training_file = training_file))
        if 'Assistant : ' in response:
            response = response.split('Assistant : ')[1]
        
        await message.channel.send(response)
        
        new_data = [{'role': 'Assistant', 'content': response}]
        update_training_data(training_file = training_file, old_data = old_data, new_data = new_data)

maintenance_assistant_client.run(credentials['discord_maintenance_client_token'])

