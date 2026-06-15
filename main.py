#include <ESP8266WiFi.h>
#include <ThingSpeak.h>
#include <DHT.h>

#define DHTPIN D4
#define DHTTYPE DHT11

const char* ssid = "redmi note 8";
const char* password = "12345678";

unsigned long channelID =".....";
const char* writeAPIKey = ".....";

WiFiClient client;

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(115200);

  dht.begin();

  WiFi.begin(ssid, password);
  Serial.print("Connecting to WiFi");

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nWiFi Connected");

  ThingSpeak.begin(client);
}

void loop() {

  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();

  if (isnan(temperature) || isnan(humidity)) {
    Serial.println("Failed to read from DHT11!");
    return;
  }

  Serial.print("Temperature: ");
  Serial.print(temperature);
  Serial.println(" °C");

  Serial.print("Humidity: ");
  Serial.print(humidity);
  Serial.println(" %");

  ThingSpeak.setField(1, temperature);
  ThingSpeak.setField(2, humidity);

  int x = ThingSpeak.writeFields(channelID, writeAPIKey);

  if (x == 200) {
    Serial.println("Data uploaded successfully");
  } else {
    Serial.print("Upload failed. Error code: ");
    Serial.println(x);
  }

  delay(20000);
}
