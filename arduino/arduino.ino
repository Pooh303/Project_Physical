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

// void displayname(String msg){
//   lcd.clear();
//   lcd.setCursor(0, 0);
//   lcd.print(msg);
//   lcd.print(getTime());
//   delay(5000);
//   lcd.clear();
//   personDetected = false;
// }

void checkBolb(String msg){
  if (distance < 100 && !personDetected) // Adjust the threshold distance as needed
    {
      digitalWrite(Blue_pin, HIGH);
      digitalWrite(RED_pin, LOW);
      scrollText(msg, 300);
      digitalWrite(Blue_pin, LOW);
      digitalWrite(RED_pin, HIGH);
      personDetected = true;
    }
    else if (distance > 20 && personDetected)
    {
      personDetected = false;
    }
}

void scrollText(String text, int scrollDelay) {
  int textLength = text.length();
  int displayLength = 16;

  while (true) {
    for (int i = 0; i < textLength + displayLength; i++) {
      lcd.clear();
      int startPos = i % (textLength + displayLength - 16);
      if (startPos < 0) {
        startPos = 0;
      }
      lcd.setCursor(0, 0);
      lcd.print(text.substring(startPos, startPos + displayLength));
      delay(scrollDelay);
    }
  }
}



String getTime() {
  time_t currentTime = now(); // Get current time

  int currentHour = hour(currentTime);
  int currentMinute = minute(currentTime);
  int currentSecond = second(currentTime);

  // Format the time as "HH:MM:SS"
  char buffer[9]; // HH:MM:SS + null terminator
  snprintf(buffer, sizeof(buffer), "%02d:%02d:%02d", currentHour, currentMinute, currentSecond);

  return String(buffer);
}