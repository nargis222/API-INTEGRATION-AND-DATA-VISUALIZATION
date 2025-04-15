import requests
import matplotlib.pyplot as plt

# Define the API key and city
API_KEY = '0c8a958de82fd44980adb7a214e7e4b2'  # Replace with your OpenWeatherMap API key
CITY = 'BANGALORE'

# Base URL for OpenWeatherMap API
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

# Complete URL
URL = f'{BASE_URL}?q={CITY}&appid={API_KEY}&units=metric'

# Fetch weather data
response = requests.get(URL)
data = response.json()

# Check if the API request was successful
if data['cod'] == 200:
    # Extract weather data
    city = data['name']
    country = data['sys']['country']
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    
    # Display the extracted data
    print(f"Weather Data for {city}, {country}:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Pressure: {pressure} hPa")
    
    # Data to be visualized
    labels = ['Temperature (°C)', 'Humidity (%)', 'Pressure (hPa)']
    values = [temperature, humidity, pressure]
    
    # Plotting the data
    plt.figure(figsize=(8, 5))
    plt.bar(labels, values, color=['blue', 'green', 'red'])
    plt.title(f"Weather in {city}, {country}")
    plt.xlabel("Weather Parameters")
    plt.ylabel("Values")
    plt.show()
else:
    print(f"City {CITY} not found. Please check the city name or API key.")
