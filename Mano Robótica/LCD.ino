#include <Servo.h>
#include <LiquidCrystal.h>
const int rs = 12, en = 11, d4 = 2, d5 = 3, d6 = 4, d7 = 5;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

Servo pulgar;
Servo indice;
Servo medio;
Servo anular;
Servo menique;

int pul = 5;
int ind = 6;
int med = 9;
int anu = 10;
int men = 11;
int D1 = 0, D2 = 0, D3 = 0, D4 = 0, D5 = 0;
int UD1 = 0, UD2 = 0, UD3 = 0, UD4 = 0, UD5 = 0;
int servoPulgar [] = {50, 60}; // [valorBajo,valorAlto]
int servoIndice [] = {50, 60};
int servoMedio [] = {50, 60};
int servoAnular [] = {50, 60};
int servoMenhique [] = {50, 60};
String bufferLCD = "";
char dedo = "";
bool cambio = 0, ucambio = 0;

void setup() 
{
  Serial.begin(9600);
  lcd.begin(16, 2);
  lcd.clear ();
  lcd.print("Bienvenido");
  lcd.setCursor (0, 1);
  lcd.print ("Esperando");
  Serial.begin(9600);
  pulgar.attach(pul);
  indice.attach(ind);
  medio.attach(med);
  anular.attach(anu);
  menique.attach(men);
  //pinMode(LED,OUTPUT);
}

void loop() 
{
  if (Serial.available() != 0) 
  {
    for (int i = 0; i <= 5; i++)
    {
      dedo = Serial.read();
      bufferLCD += dedo;
      if (dedo == 'A')
      { //pulgar
        D1 = Serial.parseInt();
        bufferLCD += (String) D1;
      }
      if (dedo == 'B'){ //indice
        D2 = Serial.parseInt();
        bufferLCD += (String) D2;
      }
      if (dedo == 'C')
      { //medio
        D3 = Serial.parseInt();
        bufferLCD += (String) D3;
      }
      if (dedo == 'D')
      { //anular
        D4 = Serial.parseInt();
        bufferLCD += (String) D4;
      }
      if (dedo == 'E')
      { //meñique
        D5 = Serial.parseInt();
        bufferLCD += (String) D5;
      }
    }

    if (D1 != UD1 || D2 != UD2 || D3 != UD3 || D4 != UD4 || D5 != UD5) {
      //Serial.println("cambio");
      cambio = 1;
      UD1 = D1;
      UD2 = D2;
      UD3 = D3;
      UD4 = D4;
      UD5 = D5;
    }
    else {
      //Serial.println("no cambio");
      cambio = 0;
      UD1 = UD1;
      UD2 = UD2;
      UD3 = UD3;
      UD4 = UD4;
      UD5 = UD5;
    }
  }

  delay(50);

  if (cambio != ucambio) {
    Serial.println("cambio");
    Serial.print("Dedo1= ");
    Serial.print(UD1);
    Serial.print(" ");
    Serial.print("Dedo2= ");
    Serial.print(UD2);
    Serial.print(" ");
    Serial.print("Dedo3= ");
    Serial.print(UD3);
    Serial.print(" ");
    Serial.print("Dedo4= ");
    Serial.print(UD4);
    Serial.print(" ");
    Serial.print("Dedo5= ");
    Serial.print(UD5);
    Serial.println(" ");
    lcd.clear ();
    lcd.setCursor (0, 0);
    lcd.print (bufferLCD);
    //Cambio en los servos
    /*
      pulgar.write(UD1);
      indice.write(UD2);
      medio.write(UD3);
      anular.write(UD4);
      menique.write(UD4);*/
    delay(50);
    ucambio = 0;           
  }
}