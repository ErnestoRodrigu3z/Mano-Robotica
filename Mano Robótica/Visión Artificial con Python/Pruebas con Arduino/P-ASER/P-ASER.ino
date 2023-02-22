/*
   Comunicación LV-Arduino
   Recepción de cadena de caracteres
   NOTAS: Agregar un mensaje que indique que no ha llegado nada, agregar el armador de textos:) y realizar la interfaz en Python...
*/
//Se utilizara una pantalla LCD para verificar que los datos recibidos sean correctos
#include <LiquidCrystal.h>
int pos = 60;
//Variables para recibir cadena de caracteres
char lecturaDato = "";
String bufferString = "";
const int rs = 12, en = 11, d4 = 2, d5 = 3, d6 = 4, d7 = 5;

LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

//
int visualizarFrase = 8;
bool banderaD8 = false;

void setup() {
  lcd.begin(16, 2);
  lcd.clear ();
  lcd.print("Bienvenido");
  lcd.setCursor (0, 1);
  lcd.print ("Esperando");
  Serial.begin(9600);
  pinMode (visualizarFrase, INPUT);

}
void recepcionDatos ()
{
  do {
    if (Serial.available())
    {
      lecturaDato = Serial.read();
      bufferString += lecturaDato; // bufferString = (char)Serial.read() + bufferString
      Serial.println (lecturaDato);
      if (lecturaDato == '\n')
      {
        Serial.println(bufferString);
        break;
      }
    }
  } while (true);

  lcd.clear ();
  lcd.print("Mensaje");
  lcd.setCursor (0, 1);
  lcd.print ("Recibido");
}



void loop() {
  if (Serial.available() > 0)
  {
    lecturaDato = Serial.read();
    if (lecturaDato == 'A')
    {
      lcd.clear ();
      lcd.setCursor (0, 0);
      lcd.print ("Indice");
      lcd.setCursor (0, 1);
      lcd.print ("Arriba");
      bufferString = "";
      lecturaDato = "";
      delay (200);
    }
    if (lecturaDato == 'B')
    {
      lcd.clear ();
      lcd.setCursor (0, 0);
      lcd.print ("Indice");
      lcd.setCursor (0, 1);
      lcd.print ("Abajo");
      bufferString = "";
      lecturaDato = "";
      delay (200);
    }
    if (lecturaDato == 'C')
    {
      lcd.clear ();
      lcd.setCursor (0, 0);
      lcd.print ("Medio");
      lcd.setCursor (0, 1);
      lcd.print ("Arriba");
      bufferString = "";
      lecturaDato = "";
      delay (200);
    }
    if (lecturaDato == 'D')
    {
      lcd.clear ();
      lcd.setCursor (0, 0);
      lcd.print ("Medio");
      lcd.setCursor (0, 1);
      lcd.print ("Abajo");
      bufferString = "";
      lecturaDato = "";
      delay (200);
    }
    if (lecturaDato == 'E')
    {
      lcd.clear ();
      lcd.setCursor (0, 0);
      lcd.print ("Anular");
      lcd.setCursor (0, 1);
      lcd.print ("Arriba");
      bufferString = "";
      lecturaDato = "";
      delay (200);
    }
    if (lecturaDato == 'G')
    {
      lcd.clear ();
      lcd.setCursor (0, 0);
      lcd.print ("Anular");
      lcd.setCursor (0, 1);
      lcd.print ("Abajo");
      bufferString = "";
      lecturaDato = "";
      delay (200);
    }
    if (lecturaDato == 'J')
    {
      lcd.clear ();
      lcd.setCursor (0, 0);
      lcd.print ("Menhique");
      lcd.setCursor (0, 1);
      lcd.print ("Arriba");
      bufferString = "";
      lecturaDato = "";
      delay (200);
    }
    if (lecturaDato == 'K')
    {
      lcd.clear ();
      lcd.setCursor (0, 0);
      lcd.print ("Menhique");
      lcd.setCursor (0, 1);
      lcd.print ("Abajo");
      bufferString = "";
      lecturaDato = "";
      delay (200);
    }
        if (lecturaDato == '1')
    {
      lcd.clear ();
      lcd.setCursor (0, 0);
      lcd.print ("Pulgar");
      lcd.setCursor (0, 1);
      lcd.print ("Arriba");
      bufferString = "";
      lecturaDato = "";
      delay (200);
    }
    if (lecturaDato == '2')
    {
      lcd.clear ();
      lcd.setCursor (0, 0);
      lcd.print ("Pulgar");
      lcd.setCursor (0, 1);
      lcd.print ("Abajo");
      bufferString = "";
      lecturaDato = "";
      delay (200);
    }
  }
}
