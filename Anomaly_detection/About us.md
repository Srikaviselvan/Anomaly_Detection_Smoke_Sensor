Team: Visionaries

Problem Statement:
SHK24004 - Predictive Maintenance with Chatbot Integration


Proposed Solution:

The system detects malfunctioning sensors from the sampled_sensor.csv file.
If any of the sensors contain anomalous readings, those sensors are stored in a list.

A client (alerter) sends a text alert over a server to the maintenance employees.
At the same time, another client is started (maintenance assistant).

If any of the employees respond to the alerter, then maintenance is initiated, and the alerter 
takes no further steps, or can be configured to send a backup alert if the sensors do not get fixed.
If no response is received within a fixed amount of time, the alert sends a phone call alert to the employees.

The maintenance assistant leverages artificial intelligence to provide maintenance support to 
the employees by responding to their queries. Each dialogue exchange is recorded and is used to train 
the chatbot so it gets smarter with each response.
