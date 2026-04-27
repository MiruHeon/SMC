#include <WiFi.h> 
#include <WiFiUdp.h>

const char* ssid = "wifi_name";
const char* password = "wifi_password";
const char* server_ip = "server_ip";
const int port = 9000;

WiFiUDP udp;

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
  }
}

void loop() {
  delay(5000);

  udp.beginPacket(server_ip, port);
  udp.print("Telemetry Code Here");
  udp.endPacket();
}
