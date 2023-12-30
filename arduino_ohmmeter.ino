const int sensorPin = A0;  // Analog input pin that senses Vout
int sensorValue = 0;       // sensorPin default value
float Vin = 5;             // Input voltage
float Vout = 0;            // Vout default value
float Rref = 99;          // Reference resistor's value in ohms (you can give this value in kiloohms or megaohms - the resistance of the tested resistor will be given in the same units)
float R = 0;               // Tested resistors default value
float ohms[10];
int i = 0;
float sumR = 0;
String x = "";

void setup ()
{
  Serial.begin(9600);      // Initialize serial communications at 9600 bps
  Serial.setTimeout(1);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop ()
{
  sensorValue = analogRead(sensorPin);  // Read Vout on analog input pin A0 (Arduino can sense from 0-1023, 1023 is 5V)
  Vout = (Vin * sensorValue) / 1023;    // Convert Vout to volts
  R = Rref * (1 / ((Vin / Vout) - 1));  // Formula to calculate tested resistor's value

  sumR = sumR - ohms[i] + R;

  ohms[i] = R;

  //if (Serial.available())
  //{
  //  x = Serial.readString();
  //  if (x.charAt(0) == 'r')
      Serial.println(sumR/10);                    // Give calculated resistance in Serial Monitor
    
    //digitalWrite(LED_BUILTIN, HIGH);  // turn the LED on (HIGH is the voltage level)
    //delay(1000);                      // wait for a second
    //digitalWrite(LED_BUILTIN, LOW);   // turn the LED off by making the voltage LOW
    //delay(1000);                      // wait for a second
  //}
  i++;
  if(i == 10)
  {
    i = 0;
  }
  //Serial.print("R: ");                  
  //Serial.print(R);                    // Give calculated resistance in Serial Monitor
  //Serial.println(" k-Ohm");     
  delay(10);                          // Delay in milliseconds between reeds
}
