/*
   Comunicación LV-Arduino
   Recepción de cadena de caracteres
   NOTAS: Agregar un mensaje que indique que no ha llegado nada, agregar el armador de textos:) y realizar la interfaz en Python...
*/
//Se utilizara una pantalla LCD para verificar que los datos recibidos sean correctos
#include <LiquidCrystal.h>
#include <Servo.h>

Servo gradosPulgar;
Servo gradosIndice;
Servo gradosMedio;
Servo gradosAnular;
Servo gradosMenhique;

int pinPulgar = 5;
int pinIndice = 6;
int pinMedio = 9;
int pinAnular = 10;
int pinMenhique = 11;


int pos = 60;
//Variables para recibir cadena de caracteres
char lecturaDato = "";
String bufferString = "";
const int rs = 12, en = 11, d4 = 2, d5 = 3, d6 = 4, d7 = 5;

int servoPulgar [] = {50, 150}; // [valorBajo,valorAlto]
int indexPulgar = 0;
int servoIndice [] = {50, 150};
int indexIndice = 0;
int servoMedio [] = {50, 150};
int indexMedio = 0;
int servoAnular [] = {50, 150};
int indexAnular = 0;
int servoMenhique [] = {50, 150};
int indexMenhique = 0;

LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

int visualizarFrase = 8;
bool banderaD8 = false;

void setup() {
  lcd.begin(16, 2);
  lcd.clear ();
  lcd.print("Bienvenido");
  lcd.setCursor (0, 1);
  lcd.print ("Esperando");
  Serial.begin(9600);
  gradosPulgar.attach (pinPulgar);
  gradosIndice.attach (pinIndice);
  gradosMedio.attach (pinMedio);
  gradosAnular.attach (pinAnular);
  gradosMenhique.attach (pinMenhique);  
}

void gradosMotor ()
{
  gradosPulgar.write(servoPulgar[indexPulgar]);
  gradosIndice.write(servoIndice[indexIndice]);
  gradosMedio.write(servoMedio[indexMedio]);
  gradosAnular.write(servoMedio[indexAnular]);
  gradosMenhique.write(servoMenhique[indexMenhique]);
}
void imprimirLCD ()
{
  lcd.clear();
  lcd.print ("P: " + (String) indexPulgar);
  lcd.setCursor (5,0);  
  lcd.print ("I: " + (String) indexIndice);
  lcd.setCursor (10,0);  
  lcd.print ("M: " + (String) indexMedio);
  lcd.setCursor (0,1);  
  lcd.print ("A: " + (String) indexAnular);
  lcd.setCursor (5,1);  
  lcd.print ("m: " + (String) indexMenhique);
}
void imprimirDatosSerial ()
{
  Serial.print ("Pulgar: " + (String)indexPulgar);
  Serial.print ('\t');
  Serial.print ("Indice: " + (String)indexIndice);
  Serial.print ('\t');
  Serial.println ("Medio: " + (String)indexMedio);
  Serial.print ("Anular: " + (String) indexAnular);    
  Serial.print ('\t');
  Serial.println ("Menhique: " + (String)indexMenhique);
}
void recepcionDatos ()
{
  do {
    if (Serial.available() > 0)
    {
      lecturaDato = Serial.read();
      if (lecturaDato == 'A')
      {
        lecturaDato = Serial.parseInt();        
        indexPulgar = lecturaDato;
      }
      if (lecturaDato == 'B')
      {
        lecturaDato = Serial.parseInt();
        indexIndice = lecturaDato;
      }
      if (lecturaDato == 'C')
      {
        lecturaDato = Serial.parseInt();
        indexMedio = lecturaDato;
      }
      if (lecturaDato == 'D')
      {
        lecturaDato = Serial.parseInt();
        indexAnular = lecturaDato;
      }
      if (lecturaDato == 'E')
      {
        lecturaDato = Serial.parseInt();
        indexMenhique = lecturaDato;        
      }
      if (lecturaDato == ',')
      {
        break;
      }
    }
  } while (true);
  gradosMotor();
}

void loop() {
  if (Serial.available() > 0)
  {
    lecturaDato = Serial.read();
    if (lecturaDato == 'I')
    {
      bufferString = "";
      recepcionDatos();
      lecturaDato = "";
    }
  }  
}
