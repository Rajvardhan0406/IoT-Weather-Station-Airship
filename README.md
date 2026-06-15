IoT Weather Station Airship

 Overview

The IoT Weather Station Airship is a smart monitoring system that collects real-time environmental data such as temperature, humidity, atmospheric pressure, and air quality. The collected data is transmitted over the internet and can be monitored remotely through a web dashboard or mobile device. This project demonstrates the application of the Internet of Things (IoT) in weather monitoring and environmental analysis.

 Features

* Real-time temperature monitoring
* Humidity measurement
* Atmospheric pressure sensing
* Air quality monitoring
* Wireless data transmission using Wi-Fi
* Remote monitoring through cloud platform
* User-friendly dashboard for data visualization

 Components Used

* ESP8266 NodeMCU / ESP32
* DHT11/DHT22 Temperature and Humidity Sensor
* BMP180/BMP280 Pressure Sensor
* MQ135 Air Quality Sensor
* Breadboard
* Jumper Wires
* Power Supply
* Wi-Fi Network

 Working Principle

The sensors continuously collect environmental data and send it to the ESP8266/ESP32 microcontroller. The controller processes the sensor readings and uploads the data to an IoT cloud platform via Wi-Fi. Users can access the weather information from anywhere using a web browser or mobile application.


 Software Requirements

* Arduino IDE
* ESP8266/ESP32 Board Package
* DHT Sensor Library
* Adafruit BMP Library
* WiFi Library
* IoT Cloud Platform (ThingSpeak, Blynk, etc.)

Installation

1. Install Arduino IDE.
2. Install the required board package and libraries.
3. Connect all sensors according to the circuit diagram.
4. Configure Wi-Fi credentials in the source code.
5. Upload the code to ESP8266/ESP32.
6. Open the cloud dashboard to monitor weather data.

 Usage

1. Power on the system.
2. Connect the device to a Wi-Fi network.
3. Sensors start collecting environmental data.
4. Data is uploaded to the cloud platform.
5. View real-time weather information through the dashboard.

Applications

* Smart Weather Monitoring
* Environmental Analysis
* Agriculture Monitoring
* Air Quality Assessment
* Educational IoT Projects
* Smart City Solutions

 Future Enhancements

* Rainfall Detection
* Wind Speed Monitoring
* GPS-Based Location Tracking
* Mobile Application Integration
* Weather Forecast Prediction using Machine Learning

 Project Output

The system displays real-time weather parameters including temperature, humidity, pressure, and air quality on an IoT dashboard, allowing users to monitor environmental conditions remotely.

 
