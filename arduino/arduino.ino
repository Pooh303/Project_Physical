#include <Wire.h>
#include <LCD.h>
#include <LiquidCrystal_I2C.h>

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
      checkBolb("Phowadol  Sriphanna");
    }
    else if (msg == "MEAN"){
      checkBolb("MEAN SWIM");
    }
    else if (msg == "BIKE"){
      checkBolb("BIKE JUMP");
    }
  }
}

void displayname(String msg){
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print(msg);
  delay(5000);
  lcd.clear();
  personDetected = false;
}

void checkBolb(String msg){
  if (distance < 100 && !personDetected) // Adjust the threshold distance as needed
    {
      digitalWrite(Blue_pin, HIGH);
      digitalWrite(RED_pin, LOW);
      displayname(msg);
      digitalWrite(Blue_pin, LOW);
      digitalWrite(RED_pin, HIGH);
      personDetected = true;
    }
    else if (distance > 20 && personDetected)
    {
      personDetected = false;
    }
}

