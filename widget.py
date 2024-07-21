import requests
from mosaico import widget

# Set up the widget
icon = widget.createImage()

# URL for weather API
weather_url = "https://api.open-meteo.com/v1/forecast"
params = {"latitude": 44.4938, "longitude": 11.3387, "current": "weather_code"}


def fetch_weather_code():
    response = requests.get(weather_url, params=params)
    response.raise_for_status()  # Will raise an error for HTTP codes 4xx/5xx
    data = response.json()
    return data["current"]["weather_code"]


def set_icon_image(weather_code):
    image_file = str(weather_code) + ".ppm"
    icon.setImage(widget.widgetAsset(image_file))


try:
    weather_code = fetch_weather_code()
    set_icon_image(weather_code)
    icon.centerVertically()
    icon.centerHorizontally()        

except Exception as e:
    print(f"Error fetching weather data: {e}")


def loop():
    pass
