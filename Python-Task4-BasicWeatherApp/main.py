import requests

API_KEY = "5b2539cc5befb4781e8e8c1744157ef6"

while True:
    city = input("\nEnter city name or ZIP code: ").strip()

    if not city:
        print("Please enter a city name or ZIP code.")
        continue

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params, timeout=10)

        if response.status_code == 401:
            print("Invalid API key.")
            continue

        if response.status_code == 404:
            print("City not found.")
            continue

        response.raise_for_status()

        data = response.json()

        temperature_c = data["main"]["temp"]
        temperature_f = (temperature_c * 9 / 5) + 32
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]

        print("\n--- Weather Information ---")
        print("City:", data["name"])
        print(f"Temperature: {temperature_c:.2f} °C")
        print(f"Temperature: {temperature_f:.2f} °F")
        print("Humidity:", humidity, "%")
        print("Weather Condition:", condition.title())
        print("Wind Speed:", wind_speed, "m/s")

    except requests.exceptions.Timeout:
        print("Request timed out. Please try again.")

    except requests.exceptions.ConnectionError:
        print("Network error. Please check your internet connection.")

    except requests.exceptions.RequestException:
        print("Unable to fetch weather information.")

    again = input("\nCheck another city? (yes/no): ").strip().lower()

    if again != "yes":
        print("Thank you!")
        break