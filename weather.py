import requests
import matplotlib.pyplot as plt


api_key = "c6bbe118a770e1faf80dc8c547f68a10"   
city = "Delhi"


url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
response = requests.get(url)


if response.status_code == 200:
    data = response.json()

    
    if "list" in data:

        dates = []
        temperatures = []
        humidity = []

        
        for item in data["list"][:8]:
            dates.append(item["dt_txt"])
            temperatures.append(item["main"]["temp"])
            humidity.append(item["main"]["humidity"])

        
        plt.figure(figsize=(10, 5))
        plt.plot(dates, temperatures, marker='o')
        plt.xticks(rotation=45)
        plt.title(f"24-Hour Temperature Forecast for {city}")
        plt.xlabel("Date & Time")
        plt.ylabel("Temperature (°C)")
        plt.tight_layout()
        plt.show()

        
        plt.figure(figsize=(10, 5))
        plt.bar(dates, humidity)
        plt.xticks(rotation=45)
        plt.title(f"24-Hour Humidity Forecast for {city}")
        plt.xlabel("Date & Time")
        plt.ylabel("Humidity (%)")
        plt.tight_layout()
        plt.show()

    else:
        print("Error from API:", data)

else:
    print("Failed to connect to API")
    print("Status Code:", response.status_code)
