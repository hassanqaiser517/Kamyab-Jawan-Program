int light1 = 11;
int light2 = 12;
int light3 = 13;

void setup()
{
  pinMode(light1, OUTPUT);
  pinMode(light2, OUTPUT);
  pinMode(light3, OUTPUT);
}

void loop()
{
digitalWrite(light1, HIGH);
delay(3000);
digitalWrite(light1, LOW);

digitalWrite(light2, HIGH);
delay(600);
digitalWrite(light2, LOW);

digitalWrite(light3, HIGH);
delay(3000);
digitalWrite(light3, LOW);

digitalWrite(light2, HIGH);
delay(600);
digitalWrite(light2, LOW);
}
