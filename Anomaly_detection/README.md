ASSIGN YOUR CREDENTIALS IN THE credentials.json FILE APPROPRIATELY

Getting your Discord Client Token:

Go to the Discord Developer Portal : https://discord.com/developers/applications
Click on the "New Application" button.
Enter a name for your application and click "Create".
In your application settings, go to the "Bot" tab.
Click on the "Add Bot" button to convert your application into a bot.
After adding the bot, you can grant it administrator privileges by toggling the "Administrator" 
permission under the "Privileged Gateway Intents" section.
After setting up your bot, go to the "OAuth2" tab in your application settings.
Under "OAuth2 URL Generator", select "bot" as the scope
Copy the generated URL and open it in your browser. 
From there, you can choose a server to invite the bot to.'
In the "Bot" tab of your application settings, you'll find the bot token under the "Token" section.

Link to my Server : https://discord.gg/K646AGpE (Link expires on March 29 2024)

<hr>
Getting your OpenAI API Key:

Go to the OpenAI platform : https://platform.openai.com/api-keys
Once signed in, you should be on the API Keys page. If not, navigate there by clicking on your user icon 
at the top right corner and selecting "API Keys" from the dropdown menu.
If you haven't created an API key yet, you'll see an option to "Create API Key". Click on it.
Click on the "Generate API Key" button.

<hr>
Getting your Twilio Credentials:

Go to the Twilio website : https://www.twilio.com/
Once logged in, navigate to the Twilio Console.
In the sidebar menu, look for the "Settings" option. Click on it to expand the submenu.
Under "Settings", select "API Keys" or "API Keys & Tokens", depending on the Twilio dashboard layout at 
the time of your access.
Look for an option to create a new API key. This might be labeled as "Create API Key" or something 
similar.
After providing a name, proceed to generate the API key. Twilio will generate both an API Key (SID) and 
an API Secret (Token) for you.

<hr>
Getting your Replicate API Key:

Visit the following website : https://replicate.com/account/api-tokens
Sign in with Github.
A default API Key will be provided for you.
You can also generate a new API Key by clicking 'Create token'.
<hr>

If you want to access the credentials:
https://drive.google.com/file/d/1-4ZgNUQP-YUb1m0n67eItd2rwV5c1eF4/view?usp=sharing

**The above steps have to be completed before running the python files.**
<hr>

UI/UX link(Figma) : https://www.figma.com/proto/35sOySU7eC6A9sbxhrq8a0/Untitled?type=design&node-id=7-276&t=ZGlV7Q28YanXkkKA-1&scaling=min-zoom&page-id=0%3A1&starting-point-node-id=7%3A276&mode=design

<hr>
<h2>Steps To Execute</h2>

1. Sensor:<br>
   Get a smoke sensor and connect it as per the diagram with Arduino uno or Arduino Nano
   ![image](https://github.com/hr-shloklabs/SHK24-Karunya-visionaries/assets/110014983/5dcec124-ca58-4798-a29e-5eb788be3cc0)
<hr>
2. Arduino IDE:<br>
   Download and install Arduino IDE and run the file "smoke_sensor.ino"
<hr>
3. Pyserial: <br>
   Before running the "dataextractor.py" make sure that you have installed pyserial module.
   Run the "dataextractor.py" file to collect the data. Press "1" to label it as Normal data and Press "2" to label it as Broken data.
<hr>
4. CSV: <br>
   The collected data is shown at serial_data.csv 
<hr>
5. Machine Learning: <br>
   Run the "machine_learning_anomaly_detection" file to run the RandomForestClassifier algorithm and the model will be saved "anomaly_detection_model.pkl"
<hr>
6. Realtime prediction : <br>
   Run the "predict.py" file to predict the status of the machine in realtime.
   Now you can run the "realtime_detection.py" file to connect with the discord server and it will show the anomaly status in the server.
<hr>
7. Realtime alerter: <br>
   Now run the "realtime_alerter.py" file to get the anomaly status with phone call alerter integration.
<hr>
8. Simulating Employee response: <br>
   A text alert will be sent to the server.
   Respond with a 👍 emoji to acknowledge the alert message.
   If no one responds within 10 seconds, a phone call will be sent.
   React with a 👍 emoji to the alert messages of the respective sensors to confirm they have been fixed.
<hr>
