/*
 * Created by Pi BOTS MakerHub
 *
 * Email: pibotsmakerhub@gmail.com
 * 
 * Github: https://github.com/pibotsmakerhub
 *
 * Join Us on Telegram : https://t.me/pibots 
 * Copyright (c) 2020 Pi BOTS MakerHub
*/

// REQUIRES the following Arduino libraries:
// - DHT Sensor Library: https://github.com/adafruit/DHT-sensor-library
// - Adafruit Unified Sensor Lib: https://github.com/adafruit/Adafruit_Sensor

#include "DHT.h"
#define DHTPIN 2     // Digital pin connected to the DHT sensor

#define DHTTYPE DHT11   // DHT 11
//#define DHTTYPE DHT22   // DHT 22  (AM2302), AM2321
//#define DHTTYPE DHT21   // DHT 21 (AM2301)
#define MQ3_PIN A0

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  Serial.println(F("fruit detection"));

  dht.begin();
}

void loop() {
  // Wait a few seconds between measurements.
  delay(3000);

  
  float h = dht.readHumidity();
  // Read temperature as Celsius (the default)
  float t = dht.readTemperature();
  
  int gas_read = analogRead(MQ3_PIN);
 
  // Check if any reads failed and exit early (to try again).
  if (isnan(h) || isnan(t) ) {
    Serial.println(F("Failed to read from DHT sensor!"));
    return;
  }

  if (gas_read/10 < 65){
    Serial.print(F(" Humidity: "));
    Serial.print(h);
    Serial.print("%, ");
    Serial.print(F("Temperature: "));
    Serial.print(t);
    Serial.print(F("C "));
    Serial.print(", ");
    Serial.print("Ethylene Gas: ");
    Serial.print(gas_read/10);
    Serial.print(", ");
    Serial.print("Fruit Condition: ");
    Serial.println("Good Fruit Condition");
  }
  else{
    Serial.print(F(" Humidity: "));
    Serial.print(h);
    Serial.print("%, ");
    Serial.print(F("Temperature: "));
    Serial.print(t);
    Serial.print(F("C "));
    Serial.print(", ");
    Serial.print("Ethylene Gas: ");
    Serial.print(gas_read/10);
    Serial.print(", ");
    Serial.print("Fruit Condition: ");
    Serial.println("Bad Fruit Condition");
  }
}
