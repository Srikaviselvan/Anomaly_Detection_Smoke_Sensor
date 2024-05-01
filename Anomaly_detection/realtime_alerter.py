import discord
import asyncio
from threading import Thread
from time import sleep
from twilio.rest import Client
import json
import serial
import pandas as pd
import joblib


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
        print("Calling...")
        alert_via_call(phone_number = phone_number)


def alert_via_call(phone_number):
    client = Client(credentials['twilio_account_sid'], credentials['twilio_auth_token'])

    call = client.calls.create(
    url="http://demo.twilio.com/docs/voice.xml",
    to=str(phone_number),
    from_="+12097574309"
    )
    



# Load the trained model
model = joblib.load('anomaly_detection_model.pkl')

# Configure the serial port
serial_port = serial.Serial('COM7', 9600)  # Change 'COM7' to the appropriate port and baudrate accordingly

def get_anomaly_status(serial_port):
    # Read data from serial port
    data = serial_port.readline().decode('utf-8').strip()
    try:
        sensor_value = float(data)

        # Create a DataFrame with the sensor value
        df = pd.DataFrame({'value': [sensor_value]})
        
        # Predict the status using the trained model
        status = model.predict(df)[0]
        
        # Print the status
        return status
    
    except:
        pass


async def check_for_anomalies_loop(channel):
    reply_time = 10
    global responded
    responded = False
    timer_started = False
    alerted = False
    
    while True:

        anomaly_status = get_anomaly_status(serial_port = serial_port)

        if anomaly_status == 'anomaly' and not alerted:

            print("Alerting...")
            await channel.send("Anomaly Detected")
            alerted = True

            if not timer_started:

                timer_thread = Thread(target = start_timer, args = [reply_time])
                timer_thread.start()
                timer_started = True

            break




async def main():
    
    bot = discord.Client(intents=discord.Intents.all())

    @bot.event
    async def on_ready():

        channel_id = 1217350511553155113
        channel = bot.get_channel(channel_id)

        await channel.purge()

        await check_for_anomalies_loop(channel = channel)



    @bot.event
    async def on_message(message: discord.message.Message):

        global responded

        if not message.author.bot:

            if message.content == '👍':
                print("Responded")
                responded = True
            

    await bot.start(credentials['discord_alerter_client_token'])

asyncio.run(main())