import serial
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('anomaly_detection_model.pkl')

# Configure the serial port
ser = serial.Serial('COM7', 9600)  # Change 'COM7' to the appropriate port and baudrate accordingly

try:
    while True:
        # Read data from serial port
        data = ser.readline().decode('utf-8').strip()
        try:
            sensor_value = float(data)
        except:
            sensor_value = data
        
        # Create a DataFrame with the sensor value
        df = pd.DataFrame({'value': [sensor_value]})
        
        # Predict the status using the trained model
        status = model.predict(df)[0]
        
        # Print the status
        print("Sensor Status:", status)

except KeyboardInterrupt:
    print("Keyboard Interrupt detected. Exiting...")

finally:
    # Close the serial port
    ser.close()
