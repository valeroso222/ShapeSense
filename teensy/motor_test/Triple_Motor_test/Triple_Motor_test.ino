#include<Encoder.h>
#include "dec.h"

void setup() {
  pinMode(M1IN1, OUTPUT);
  pinMode(M1IN2, OUTPUT);
  pinMode(M1PWM, OUTPUT);

  pinMode(M2IN1, OUTPUT);
  pinMode(M2IN2, OUTPUT);
  pinMode(M2PWM, OUTPUT);

  pinMode(M3IN1, OUTPUT);
  pinMode(M3IN2, OUTPUT);
  pinMode(M3PWM, OUTPUT);
  
  //pinMode(STBY, OUTPUT);
  pinMode(LED, OUTPUT);

  Serial.begin(BAUDRATE);
  delay(2000);
  Serial.println("Triple_Motor_test Standby");
  //digitalWrite(STBY, HIGH);
}

void loop() {
  //digitalWrite(LED,HIGH);
  counter1 = E1.read();
  counter2 = E2.read();
  counter3 = E3.read();

  int m1Out = calculatePWM(targetCount1, counter1, M1IN1, M1IN2);
  int m2Out = calculatePWM(targetCount2, counter2, M2IN1, M2IN2);
  int m3Out = calculatePWM(targetCount3, counter3, M3IN1, M3IN2);
  if (m1Out == 0 && m2Out == 0 && m3Out == 0 && isMoving){
    Serial.println("moveFin");
    isMoving = false;
  }
  analogWrite(M1PWM, m1Out);
  analogWrite(M2PWM, m2Out);
  analogWrite(M3PWM, m3Out);
  
  if (counter1 != prevCounter1 || counter2 != prevCounter2 || counter3 != prevCounter3){
    /*
    Serial.print("a: ");
    Serial.print(counter1);
    Serial.print(" b: ");
    Serial.print(counter2);
    Serial.print(" c: ");
    Serial.println(counter3);
    */
    digitalWrite(LED, HIGH);
    isMoving = true;
  } else {
    digitalWrite(LED, LOW);
  }
  prevCounter1 = counter1;
  prevCounter2 = counter2;
  prevCounter3 = counter3;

  if (Serial.available() > 0){
    handleSerialEvent();
  }
}


int calculatePWM(int targetCount, int counter, int motorPin1, int motorPin2) {

  int motorErrorInCounts = targetCount - counter;

  if (abs(motorErrorInCounts) < 50) {
    digitalWrite(motorPin1, LOW);
    digitalWrite(motorPin2, LOW);
    return 0;
  }

  int motorOut = (int)(MOTOR_GAIN * motorErrorInCounts);

  if (motorOut > 0) {  // increase motor count
    digitalWrite(motorPin1, LOW);
    digitalWrite(motorPin2, HIGH);
  } else if (motorOut < -0){  // decrease motor count
    digitalWrite(motorPin1, HIGH);
    digitalWrite(motorPin2, LOW);
  }

  return constrain(abs(motorOut), MIN_MOTOR_OUT, MAX_MOTOR_OUT);
}


void handleSerialEvent() {
  char cmd = Serial.read();
  switch (cmd) {
    case 'a':
      targetCount1 = fetchValue();
      Serial.print("Target1: ");
      Serial.println(targetCount1);
      break;
    case 'b':
      targetCount2 = fetchValue();
      Serial.print("Target2: ");
      Serial.println(targetCount2);
      break;
    case 'c':
      targetCount3 = fetchValue();
      Serial.print("Target3: ");
      Serial.println(targetCount3);
      break;
    case 'i':
      stop();
      break;
    case 'g':
      Serial.print("a: ");Serial.print(counter1);
      Serial.print(" b: ");Serial.print(counter2);
      Serial.print(" c: ");Serial.println(counter3);
      break;
    default:
      Serial.print("ERROR: ");
      Serial.print(cmd+Serial.readString());
      break;
  }
}

int fetchValue() {
  int i = 0;
  char string[10];

  while (i < sizeof(string)) {
    if (Serial.available()) {
      char c = Serial.read();
      if ((c >= '0' && c <= '9') || c == '-') {
        string[i] = c;
        i++;
      } else {
        string[i] = '\0';
        break;
      }
    }
  }
  return atoi(string);
}

void stop(){
  digitalWrite(M1IN1, HIGH);
  digitalWrite(M1IN2, HIGH);
  digitalWrite(M2IN1, HIGH);
  digitalWrite(M2IN2, HIGH);
  digitalWrite(M3IN1, HIGH);
  digitalWrite(M3IN2, HIGH);
  analogWrite(M1PWM, 0);
  analogWrite(M2PWM, 0);
  analogWrite(M3PWM, 0);
  delay(250);
  E1.write(0);
  E2.write(0);
  E3.write(0);
  targetCount1=0;
  targetCount2=0;
  targetCount3=0;
}
