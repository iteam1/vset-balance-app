/*
Test serial communicate as a shimadzu balance
*/
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println(" -123.4568T "); // Total 14 bytes
  delay(3000);
}
