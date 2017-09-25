import os
import time
import datetime
import requests
import json
import cairosvg

class Weather:

    # Global variables
    api_key = os.getenv("OPEN_WEATHER_API_KEY")
    city_id = "6556317"

    # Constructor
    def __init__(self, throttle_time):
        self.last_update_current = 0.0
        self.weather = {}
        self.throttle_time = throttle_time

    # Update the current weather
    def update_current(self):
        if time.time() - self.last_update_current < self.throttle_time:
            return
        res = requests.post("http://api.openweathermap.org/data/2.5/weather?id=" + self.city_id + "&appid=" + self.api_key)
        try:
            self.weather = json.loads(res.text)
        except Exception:
            self.weather = {}
        self.last_update_current = time.time()
        self.create_image_current()

    # Create an image from the svg template
    def create_image_current(self):
        status = json.loads(open("src/weather-mapping.json", "r").read())

        svg = open("templates/weather.svg", "r").read()
        try:
            svg = svg.replace("[[description]]", "[[" + str(self.weather["weather"][0]["id"]) + "]]")
        except Exception:
            pass
        try:
            weather_id = str(self.weather["weather"][0]["id"])
            mapping = json.loads(open("src/weather-mapping.json", "r").read())
            svg = svg.replace("[[" + weather_id + "]]", mapping[weather_id])
        except Exception:
            try:
                weather_id = str(self.weather["weather"][0]["id"])
                svg = svg.replace("[[" + weather_id + "]]", self.weather["weather"][0]["description"])
            except Exception:
                pass
        try:
            svg = svg.replace("[[temp]]", str(round(int(self.weather["main"]["temp"]) - 273.15, 2)).replace(".", ","))
        except Exception:
            pass
        try:
            svg = svg.replace("[[humidity]]", str(self.weather["main"]["humidity"]))
        except Exception:
            pass
        try:
            dawn = datetime.datetime.fromtimestamp(int(self.weather["sys"]["sunrise"])).strftime("%H:%M")
            svg = svg.replace("[[dawn]]", dawn)
        except Exception:
            pass
        try:
            sunset = datetime.datetime.fromtimestamp(int(self.weather["sys"]["sunset"])).strftime("%H:%M")
            svg = svg.replace("[[sunset]]", sunset)
        except Exception:
            pass
        try:
            svg = svg.replace("[[icon]]", self.weather["weather"][0]["icon"])
        except Exception:
            pass
        temp = open("images/temp_weather.svg", "w+")
        temp.write(svg)
        temp.close()
        cairosvg.svg2png(url = "images/temp_weather.svg", write_to = "images/weather.png")
        os.remove("images/temp_weather.svg")

# debug

w = Weather(10)
w.update_current()
