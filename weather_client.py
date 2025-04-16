import json
import requests

#function to get weather data from OpenWeatherMap API
def get_weather_data(city_name, should_print=True):
    # OpenWeatherMap API key
    API_key = "****************42"
    # Construct the API URL
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}"
    
    # Make a GET request to the OpenWeatherMap API
    response = requests.get(url)
    if response.status_code == 200:
        print("Data retrieved successfully.")
        # Parse the JSON response
        weather_data = response.json()        
        
        # Extract relevant information from the response
        City = weather_data['name']
        Temperature = weather_data['main']['temp'] - 273.15
        Humidity_Percentage = weather_data['main']['humidity'] 
        Weather_description = weather_data['weather'][0]['description']
        Pressure = weather_data['main']['pressure'] 
        
        weather_info = {
            'City': City,
            'Temperature': Temperature,
            'Humidity_Percentage': Humidity_Percentage,
            'Weather_description': Weather_description,
            'Pressure': Pressure
        }

        if should_print:
            print(f"City: {weather_info['City']}")
            print(f"Temperature: {weather_info['Temperature']:.2f} °C")
            print(f"Humidity Percentage: {weather_info['Humidity_Percentage']}%")
            print(f"Description: {weather_info['Weather_description']}")
            print(f"Pressure: {weather_info['Pressure']} hPa")

        return weather_info
        
    else:
        print(f"Failed to retrieve data: {response.status_code}")
        return
 
 
 
    
def get_future_weather_data(city_name):
    # OpenWeatherMap API key
    API_key = "****************42"
    # Construct the API URL for 5-day forecast
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={API_key}"
    # Make a GET request to the OpenWeatherMap API
    response = requests.get(url)
    if response.status_code == 200:
        print("Data retrieved successfully.")
        print(f"Fetching 5 days weather forecast data for {city_name}...")
        # Parse the JSON response
        future_weather_data = response.json()
        
        if 'list' in future_weather_data:
            for item in future_weather_data['list']:
                timestamp = item['dt_txt']
                temperature = item['main']['temp'] - 273.15
                description = item['weather'][0]['description']            
                humidity = item['main']['humidity'] 
                pressure = item['main']['pressure']
                print(f"{timestamp}: Temperature: {temperature:.2f} °C, Description: {description}, Humidity: {humidity}, Pressure: {pressure} hPa")
        else:
            print("Error: 'list' key not found in forecast data.")
    else:
        print(f"Failed to retrieve future weather data: {response.status_code}")
        return
    
    

if __name__ == "__main__":
    # This block will only run when you execute weather_client.py directly
    city_input = input("Enter city name (separated by comma): ")
    city_names = [city.strip() for city in city_input.split(",")]

    for city in city_names:
        get_weather_data(city)
        get_future_weather_data(city)


