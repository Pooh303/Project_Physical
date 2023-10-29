#include <Wire.h>
#include <LCD.h>
#include <LiquidCrystal_I2C.h>
#include <TimeLib.h>

#define I2C_ADDR 0x27
#define BACKLIGHT_PIN 3

#define RED_pin 8 //RED
#define Blue_pin 9 //BLUE

LiquidCrystal_I2C lcd(I2C_ADDR, 2, 1, 0, 4, 5, 6, 7);

int peopleCount = 0;
int count = 0;
bool personDetected = false;
long distance = 0;

void setup() {
  
  Serial.begin(9600);

  lcd.begin(16, 2);

  lcd.setBacklightPin(BACKLIGHT_PIN, POSITIVE);
  lcd.setBacklight(HIGH);
  lcd.home();

  pinMode(RED_pin, OUTPUT);
  pinMode(Blue_pin, OUTPUT);

  pinMode(4, OUTPUT); // Trig pin
  pinMode(2, INPUT);  // Echo pin

}

void loop() {
  // Ultrasonic Sensor Code
  digitalWrite(RED_pin, HIGH);
  digitalWrite(4, HIGH);
  delayMicroseconds(10);
  digitalWrite(4, LOW);

  int pulseWidth = pulseIn(2, HIGH);

  distance = pulseWidth / 29 / 2; // Convert pulse width to distance in cm
  delay(500);
  Serial.print("Distance: ");
  Serial.println(distance);

  if (Serial.available() > 0) {
    String msg = Serial.readString();
    // ================================
    if (msg == "ON") {
      digitalWrite(RED_pin, HIGH);
    }
    else if (msg == "OFF") {
      digitalWrite(RED_pin, LOW);
    }
  // ================================
    else if (msg == "DREAM"){
      checkBolb("65070182");
    }
    else if (msg == "MEAN"){
      checkBolb("65070197");
    }
    else if (msg == "BIKE"){
      checkBolb("65070215");
    }
    else{
      checkBolb("UNKNOWN");
    }
  }
}

void displayname(String msg, int time){
  String message = "";
  int col = 0;
  int row = 0;
  lcd.clear();
  if(msg != "UNKNOWN"){
    message = "ID : " + String(msg);
    lcd.setCursor(4, 0);
    lcd.print("WELCOME");
    lcd.setCursor(1, 1);
  lcd.print(message);
  } else {
    col = 4;
    row = 1;
    message = "UNKNWON";
    lcd.setCursor(col, row);
    lcd.print(message);
  }
  delay(time);
  lcd.clear();
  personDetected = false;
}

void checkBolb(String msg){
  if (distance < 150 && !personDetected) // Adjust the threshold distance as needed
    {
      if (msg != "UNKNOWN"){
        digitalWrite(Blue_pin, HIGH);
        digitalWrite(RED_pin, LOW);
        displayname(msg, 6000);
        digitalWrite(Blue_pin, LOW);
        digitalWrite(RED_pin, HIGH);
        personDetected = true;
      } else {
        digitalWrite(RED_pin, LOW);
        delay(400);
        digitalWrite(RED_pin, HIGH);
        digitalWrite(RED_pin, LOW);
        delay(400);
        digitalWrite(RED_pin, HIGH);
        displayname(msg, 4000);
      }
    }
    else if (distance > 10 && personDetected)
    {
      personDetected = false;
    }
}


