void setup() {
  Serial.begin(9600); // Set baud rate
  Serial.println("Arduino is ready"); // Send initial message to Python
}

void loop() {
  if (Serial.available() > 0) {
    String data = String(Serial.read());
    Serial.println(data+1); // Echo back to Python
  }
}
