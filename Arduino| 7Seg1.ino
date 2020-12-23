 
 void setup() {
  // put your setup code here, to run once:
pinMode(0,OUTPUT); //g
pinMode(1,OUTPUT); //f
pinMode(2,OUTPUT); //e
pinMode(3,OUTPUT); //d
pinMode(4,OUTPUT); //c
pinMode(5,OUTPUT); //b
pinMode(6,OUTPUT); //a
for(int i=0;i<7;i++)
pinMode(i,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
digitalWrite(0,LOW); // 0
digitalWrite(1,HIGH);
digitalWrite(2,HIGH);
digitalWrite(3,HIGH);
digitalWrite(4,HIGH);
digitalWrite(5,HIGH);
digitalWrite(6,HIGH);
delay(1000);
digitalWrite(0,LOW); // 1
digitalWrite(1,LOW);
digitalWrite(2,LOW);
digitalWrite(3,LOW);
digitalWrite(4,HIGH);
digitalWrite(5,HIGH);
digitalWrite(6,LOW);
delay(1000);
digitalWrite(0,HIGH); //2
digitalWrite(1,LOW);
digitalWrite(2,HIGH);
digitalWrite(3,HIGH);
digitalWrite(4,LOW);
digitalWrite(5,HIGH);
digitalWrite(6,HIGH);
delay(1000);
digitalWrite(0,HIGH); //3
digitalWrite(1,LOW);
digitalWrite(2,LOW);
digitalWrite(3,HIGH);
digitalWrite(4,HIGH);
digitalWrite(5,HIGH);
digitalWrite(6,HIGH);
delay(1000);
digitalWrite(0,HIGH); //4
digitalWrite(1,HIGH);
digitalWrite(2,LOW);
digitalWrite(3,LOW);
digitalWrite(4,HIGH);
digitalWrite(5,HIGH);
digitalWrite(6,LOW);
delay(1000);
digitalWrite(0,HIGH); //5
digitalWrite(1,HIGH);
digitalWrite(2,LOW);
digitalWrite(3,HIGH);
digitalWrite(4,HIGH);
digitalWrite(5,LOW);
digitalWrite(6,HIGH);
delay(1000);
digitalWrite(0,HIGH); //6
digitalWrite(1,HIGH);
digitalWrite(2,HIGH);
digitalWrite(3,HIGH);
digitalWrite(4,HIGH);
digitalWrite(5,LOW);
digitalWrite(6,HIGH);
delay(1000);
digitalWrite(0,LOW); //7
digitalWrite(1,LOW);
digitalWrite(2,LOW);
digitalWrite(3,LOW);
digitalWrite(4,HIGH);
digitalWrite(5,HIGH);
digitalWrite(6,HIGH);
delay(1000);
digitalWrite(0,HIGH); //8
digitalWrite(1,HIGH);
digitalWrite(2,HIGH);
digitalWrite(3,HIGH);
digitalWrite(4,HIGH);
digitalWrite(5,HIGH);
digitalWrite(6,HIGH);
delay(1000);
digitalWrite(0,HIGH); //9
digitalWrite(1,HIGH);
digitalWrite(2,LOW);
digitalWrite(3,LOW);
digitalWrite(4,HIGH);
digitalWrite(5,HIGH);
digitalWrite(6,HIGH);
delay(1000);

}
