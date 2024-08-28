import requests

def get_weather_data(city, api_key, units='metric'):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units={units}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(response.status_code)
        return None

def get_user_input():
    city = input("Enter the city name: ")
    unit = input("Choose temperature unit: (C)elsius or (F)ahrenheit: ").strip().upper()
    if unit == 'F':
        units = 'imperial'
    else:
        units = 'metric'
    return city, units

def display_weather(data):
    if data:
        city_name = data['name']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        weather_desc = data['weather'][0]['description']
        
        print(f"\nWeather in {city_name}:")
        print(f"Temperature: {temp}°")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Conditions: {weather_desc.capitalize()}\n")
    else:
        print("Error: Could not retrieve weather data.\n")

def main():
    api_key = '7ae20626d3fc5edda0c3404c8c729080'
    city, units = get_user_input()
    data = get_weather_data(city, api_key, units)
    
    if data and data.get('cod') != '404':
        display_weather(data)
    else:
        print("Invalid city name or API request failed.\n")

if __name__ == "__main__":
    main()
