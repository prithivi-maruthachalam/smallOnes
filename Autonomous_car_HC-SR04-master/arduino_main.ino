
#include<Servo.h>

static int i =0;
String x,y;
int m = 0;
int dmax = 0;

int dmid = 0;
int dright = 0;
int dleft = 0;

Servo s;

int pos = 0;

const int trig = 12, echo = 3;

int distance = 0;
int time;

void setup()
{
  Serial.begin(9600);
  
  s.attach(9);
  
  pinMode(trig, OUTPUT);
  pinMode(echo, INPUT);
  
  digitalWrite(trig,LOW);
  delay(0.002);
  
  
  delay(5000);
  while(i==0)
  {
    Serial.println("hi");
    x = Serial.readString();
    if(x == "pihi")
    Serial.println(x);
    i = 2;
  }
}


int get_distance()
{

  digitalWrite(trig, HIGH);
  delay(0.01);
  digitalWrite(trig, LOW);
  
  time = pulseIn(echo,HIGH);
  distance = time * 0.017;
  return distance;
  
}




void loop()
{
  if(Serial.readString() == "give_d")
  {
    dmid = get_distance();

    
    s.write(0);
    delay(180);
    dright = get_distance();
    
    delay(15);
    s.write(90);
    delay(100);
    
    s.write(180);
    delay(180);
    dleft = get_distance();
    
    delay(15);
    s.write(90);
    
    
    dmax = max(dmid,dright);
    dmax = max(dmax,dleft);
    
    
    if(dmax == dmid)
    {Serial.println(1,DEC);}
    
    else if(dmax == dright)
    {Serial.println(2,DEC);}
    
    else if(dmax == dleft)
    {Serial.println(0,DEC);}
    
    else
    {Serial.println(8,DEC);}
  }
  
  else
    {Serial.println(12,DEC);}
  
  x = Serial.readString();
  
  while(x != "give_d")
  {
      x = Serial.readString();
      distance = get_distance();
      if(distance>0)
      Serial.println(abs(distance),DEC);
      delay(200);
  }
  
  
}
