int analogPin0 = A0; //voltage input
int val_low = 0;
int count_low = 0;
int Vout_low = 13;
#define VMAX 970 // threshold value to have water
#define Hour 3600000
void setup() {
  // put your setup code here, to run once:
  pinMode(Vout_low,OUTPUT);
  digitalWrite(Vout_low,HIGH);
  Serial.begin(9600); 

}

void loop() {
  val_low = analogRead(analogPin0);  // read the incoming voltage
  //an open circiut will out a voltage of 5v, unless there's water...
  if(val_low<VMAX)
    count_low++;
    //failsafe for fake alerts
   else if(count_low < 5)
     count_low = 0;

     //Serial.println(val_low);
         
    if(count_low == 8){
      Serial.println("w");
      digitalWrite(Vout_low,LOW);
      delay(Hour*12);
      count_low = 0;
      digitalWrite(Vout_low,HIGH);
    }
    delay(5000);
}