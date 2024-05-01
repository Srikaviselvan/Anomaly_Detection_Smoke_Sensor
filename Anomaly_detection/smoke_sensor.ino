// Initialize the sensor variable
float sensorValue1;
// Initialize the analog pin
int smokeA0 = A0;

void setup() {
  Serial.begin(9600); 
  pinMode(smokeA0, INPUT);
 
  // Wait for 20 seconds to let the sensor warm up for accurate readings
  delay(20000); 
}

void loop() {
  sensorValue1 = analogRead(smokeA0);
  // print the sensor value
  Serial.println(sensorValue1);
  delay(1000);
  
}
