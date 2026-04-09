import requests
def get_weather():
    api_key = "YOUR_API_KEY_HERE" 
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    city = input("Enter the name of the municipality: ")
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric' 
    }
    try:
        response = requests.get(base_url, parameters=params)
        if response.status_code == 200:
            data = response.json()
            desc = data['weather'][0]['description']
            temp = data['main']['temp']
            print(f"\nWeather in {city.capitalize()}:")
            print(f"Condition: {desc}")
            print(f"Temperature: {temp}°C")
        elif response.status_code == 404:
            print("Municipality not found. Please check the spelling.")
        else:
            print(f"Error: Unable to fetch data (Status Code: {response.status_code})")
    except requests.exceptions.RequestException as e:
        print(f"Connection error: {e}")
if __name__ == "__main__":
    get_weather()