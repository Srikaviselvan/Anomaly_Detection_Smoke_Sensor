import serial
import pandas as pd
import joblib
import discord

bot = discord.Client(intents = discord.Intents.all())




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
    
    


@bot.event
async def on_ready():

    channel_id = 1217350511553155113

    channel = bot.get_channel(channel_id)

    await channel.purge()

    alerted = False

    while True:
        try:
            anomaly_status = get_anomaly_status(serial_port = serial_port)
            print(anomaly_status)
            await channel.send(anomaly_status)
        except KeyboardInterrupt:
            print("Keyboard Interrupt detected. Exiting...")
            serial_port.close()
            await bot.close()
            break



bot.run("MTIxNzM1MDA3MzQwNzYzNTQ2Ng.GjTVX5.Hjm5YAkgh8Z7-jP-LQ2nBht4M37c1sI96TzYJ4")
