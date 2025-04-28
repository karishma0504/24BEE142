class Weather:
    def __init__(self, temperature, humidity, wind_speed, pressure):
        """Initialize the Weather object with weather parameters."""
        self.weather_params = {
            "Temperature": temperature,
            "Humidity": humidity,
            "Wind Speed": wind_speed,
            "Pressure": pressure
        }

    def __contains__(self, item):
        """Override the 'in' operator to check if an item is in the weather parameters."""
        # Check if the item is a key in the weather_params dictionary
        return item in self.weather_params

    def __str__(self):
        """Return a string representation of the weather parameters."""
        return f"Weather Data: {self.weather_params}"


# Example usage:
weather1 = Weather(30, 80, 15, 1012)

print(f"Weather Details: {weather1}")

# Check if a specific weather parameter is in the list
if "Temperature" in weather1:
    print("Temperature is in the weather data.")
else:
    print("Temperature is not in the weather data.")

if "Rain" in weather1:
    print("Rain is in the weather data.")
else:
    print("Rain is not in the weather data.")
