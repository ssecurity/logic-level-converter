int i = 0;
void setup() {
  // put your setup code here, to run once:
  Serial3.begin(9600);
  
}

void loop() {
  // put your main code here, to run repeatedly:
  i++;
  i = i % 100;
  Serial3.print("HELLO, FROM ARDUINO (v.");
  Serial3.print(i);
  Serial3.println(")");
  delay(5000);
  
}
