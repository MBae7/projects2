void setup() {
  Serial.begin(9600); // Set baud rate
  Serial.println("Arduino is ready"); // Send initial message to Python
}

void loop() {
  if (Serial.available() > 0) {
    int data = Serial.read();
    Serial.println(data); // Echo back to Python
  }
}
