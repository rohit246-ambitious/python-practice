import requests

def weather_api(city):

    url = f"http://api.weatherapi.com/v1/current.json?key=334e79efdcee404aa2c151950252211&q={city}"
    try:
        response = requests.get(url)
        data = response.json()
        if("error" in data):
            print("Error:", data["error"]["message"])
            exit()
        
        print("\n-----------------------------")
        print(f" 🌤️  Weather Report for: {city.title()}")
        print("-----------------------------")
        print(f"Temperature: {data['current']['temp_c']}°C")
        print(f"Condition: {data['current']['condition']['text']}")
        print(f"Humidity: {data['current']['humidity']}%")
        print(f"Wind Speed: {data['current']['wind_kph']} kph")
        print("-----------------------------")
    except Exception as e:
        print("An error occurred:", e)
    
    toContune = input("Do you want to continue (yes/no): ")
    if toContune.lower() == "yes":
        city = input("Enter city name: ")
        weather_api(city)

city = input("Enter city name: ")
weather_api(city)