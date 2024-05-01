import discord
import asyncio
import json

with open("credentials.json", "r") as json_file:
    credentials = json.load(json_file)

async def testing_thread_function():

    for sensor in anomaly_history:
        await fix_anomaly(sensor_name = sensor)

def start_testing_thread_function():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(testing_thread_function())


def create_anomaly(sensor_name):

    anomaly_history[sensor_name][0] = True


async def fix_anomaly(sensor_name):

    anomaly_history[sensor_name][0] = False

    if get_notified_status(sensor_name = sensor_name):
        await delete_alert(sensor_name = sensor_name)
        anomaly_history[sensor_name][1] = False


    
def get_anomaly_status(sensor_name):
    
    return anomaly_history[sensor_name][0]


def get_notified_status(sensor_name):
    
    return anomaly_history[sensor_name][1]


async def notify_anomaly(channel, sensor_name):

    alert_message = await channel.send("Sensor " + str(sensor_name) + ' - Anomaly Detected')

    anomaly_history[sensor_name].append(alert_message)

    anomaly_history[sensor_name][1] = True


async def delete_alert(sensor_name):

    await anomaly_history[sensor_name][2].delete()

    anomaly_history[sensor_name].pop()
    

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

        while True:
            for sensor in anomaly_history:
                if get_anomaly_status(sensor_name = sensor) and not get_notified_status(sensor_name = sensor):
                    await notify_anomaly(channel = channel, sensor_name = sensor)
            
            # Testing here
                    
            await fix_anomaly(6)

            await fix_anomaly(10)

            create_anomaly(3)

            create_anomaly(7)
    
    

            

    await bot.start(credentials['discord_alerter_client_token'])

asyncio.run(main())

