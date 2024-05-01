import serial
import msvcrt  # For Windows

# Configure the serial port
ser = serial.Serial('COM7', 9600)  # Change 'COM7' to the appropriate port and baudrate accordingly

# Open CSV file for writing
csv_file = open('serial_data.csv', 'a')

try:
    while True:
        # Read data from serial port
        data = ser.readline().decode('utf-8').strip()  # Assuming ASCII data, change decoding accordingly
        
        # Print the data
        print(data)
        
        # Check if a key is pressed
        if msvcrt.kbhit():  # For Windows
            key = msvcrt.getch().decode('utf-8')
            # Determine status based on user input
            if key == '1':
                status = 'normal'
            elif key == '2':
                status = 'broken'
            else:
                status = 'unknown'  # Default status for unrecognized input
            
            # Format the data with status and write to CSV file
            formatted_data = f"{data},{status}\n"
            csv_file.write(formatted_data)
            csv_file.flush()  # Flush buffer to ensure immediate writing
            
            print(f"Data saved with status: {status}")

except KeyboardInterrupt:
    print("Keyboard Interrupt detected. Exiting...")

finally:
    # Close serial port and CSV file
    ser.close()
    csv_file.close()
