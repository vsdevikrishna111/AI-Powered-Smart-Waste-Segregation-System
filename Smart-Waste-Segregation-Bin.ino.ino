#include <Arduino.h>
#include <Servo.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

// ---------- PINS ----------
#define SERVO_PIN 3
#define MOTOR_IN1 10
#define MOTOR_IN2 11

// ---------- CONSTANTS ----------
#define FLAP_OPEN  90
#define FLAP_CLOSE 0

#define MOTOR_STEP_MS 1000   // reduced for stable rotation
#define MOTOR_SETTLE  300

LiquidCrystal_I2C lcd(0x27, 16, 2);
Servo flapServo;

// ---------- STATE ----------
int currentBin = 0;

// ---------- SETUP ----------
void setup() {
  Serial.begin(9600);

  pinMode(MOTOR_IN1, OUTPUT);
  pinMode(MOTOR_IN2, OUTPUT);

  flapServo.attach(SERVO_PIN);
  flapServo.write(FLAP_CLOSE);

  lcd.init();
  lcd.backlight();
  lcd.setCursor(0,0);
  lcd.print("Smart Waste Bin");
  delay(2000);

  lcd.clear();
  lcd.print("Waiting...");
}

// ---------- MAIN LOOP ----------
void loop() {

  if (Serial.available() > 0) {

    char received = Serial.read();

    if (received >= '0' && received <= '2') {

      int targetBin = received - '0';

      lcd.clear();
      lcd.print("Detected:");
      lcd.setCursor(0,1);
      lcd.print(binLabel(targetBin));

      Serial.println("Received from Python");
      delay(1000);

      // ---------- STEP 1: Rotate ----------
      rotateToBin(targetBin);

      // ---------- STEP 2: Open flap ----------
      flapServo.write(FLAP_OPEN);
      delay(1200);

      // ---------- STEP 3: Close flap ----------
      flapServo.write(FLAP_CLOSE);
      delay(800);

      currentBin = targetBin;

      lcd.clear();
      lcd.print("Done!");
      delay(1500);

      lcd.clear();
      lcd.print("Waiting...");
    }
  }
}

// ---------- ROTATION ----------
void rotateToBin(int target) {

  int steps = (target - currentBin + 3) % 3;

  for (int i = 0; i < steps; i++) {
    rotateMotor120();
  }
}

// ---------- MOTOR CONTROL ----------
void rotateMotor120() {

  digitalWrite(MOTOR_IN1, HIGH);
  digitalWrite(MOTOR_IN2, LOW);

  delay(MOTOR_STEP_MS);

  motorStop();
  delay(MOTOR_SETTLE);
}

void motorStop() {
  digitalWrite(MOTOR_IN1, LOW);
  digitalWrite(MOTOR_IN2, LOW);
}

// ---------- LABELS ----------
const char* binLabel(int bin) {
  if (bin == 0) return "Dry";
  if (bin == 1) return "Wet";
  if (bin == 2) return "Recycle";
  return "Unknown";
}