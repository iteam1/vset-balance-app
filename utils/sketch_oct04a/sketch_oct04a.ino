/*
Test serial communicate as a shimadzu balance
*/
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println("123.45678Tl4"); // Total 14 bytes
  delay(3000);
  Serial.println("  0.18288Tl4"); // Total 14 bytes
  delay(3000);
}
