import discord
import asyncio
from threading import Thread
from time import sleep
from twilio.rest import Client
import json

with open("credentials.json", "r") as json_file:
    credentials = json.load(json_file)


global responded
responded = False


phone_number = "+91" + credentials['phone_number']

def start_timer(time):
    
    while time > 0:
        time -= 1
        sleep(1)
    if not responded:
        alert_via_call(phone_number = phone_number)


def alert_via_call(phone_number):
    client = Client(credentials['twilio_account_sid'], credentials['twilio_auth_token'])

    call = client.calls.create(
    url="http://demo.twilio.com/docs/voice.xml",
    to=str(phone_number),
    from_="+12097574309"
    )
    




    
def get_anomaly_status(sensor_name):
    
    return anomaly_history[sensor_name][0]


def get_notified_status(sensor_name):
    
    return anomaly_history[sensor_name][1]


async def notify_anomaly(channel, sensor_name):

    alert_message = await channel.send("Sensor " + str(sensor_name) + ' - Anomaly Detected')

    anomaly_history[sensor_name].append(alert_message)

    anomaly_history[sensor_name][1] = True





    

global anomaly_history
anomaly_history = {}

for i in range(1, 11):
    if i % 2 == 0:
        anomaly_history[i] = [True, False]
    else:
        anomaly_history[i] = [False, False]







async def main():
    
    bot = discord.Client(intents=discord.Intents.all())

    @bot.event
    async def on_ready():

        channel_id = 1217350511553155113
        channel = bot.get_channel(channel_id)

        await channel.purge()

        reply_time = 10
        responded = False
        timer_started = False
   
        for sensor in anomaly_history:
            if get_anomaly_status(sensor_name = sensor) and not get_notified_status(sensor_name = sensor):
                if not timer_started:
                    timer_thread = Thread(target = start_timer, args = [reply_time])
                    timer_thread.start()
                    timer_started = True
                await notify_anomaly(channel = channel, sensor_name = sensor)
    
    
    @bot.event
    async def on_raw_reaction_add(payload):
        
        if payload.emoji.name == '👍':
            channel = bot.get_channel(payload.channel_id)
            message = await channel.fetch_message(payload.message_id)
            await message.delete()
            

            for sensor in anomaly_history:
                if len(anomaly_history[sensor]) == 3:
                    if anomaly_history[sensor][2] == message:
                        anomaly_history[sensor].pop()
                        confirmation_message = await channel.send("Sensor " + str(sensor) + " has been fixed")
                        await confirmation_message.delete(delay = 3)


    @bot.event
    async def on_message(message: discord.message.Message):

        global responded

        if not message.author.bot:

            if message.content == '👍':
                responded = True
            

    await bot.start(credentials['discord_alerter_client_token'])

asyncio.run(main())

