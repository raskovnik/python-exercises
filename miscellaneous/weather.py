import string
import urllib.request, urllib.parse, urllib.error
from xml.dom import minidom

WEATHER_URL = "https://www.google.com/ig/api?weather=%s&hl=%s"

def extract_value(dom, parent, child): # convenience functiom to dig out weather values
    return dom.getElementByTagName(parent)[0].getElementByTagName(child)[0].getAttribute("data")

def fetch_weather(location, hl = ""): # Fethches weather report from Google
    url = WEATHER_URL % (urllib.parse.quote(location), hl)
    handler = urllib.request.urlopen(url)
    data = handler.read()
    dom = minidom.parseString(data)
    handler.close

    data = {}
    weather_dom = dom.getElementsByTagName("weather")[0]
    data["city"] = extract_value(weather_dom, "forecast_information", "city")
    data["temperature"] = extract_value(weather_dom, "current_conditions", "temp_f")
    data["conditions"] = extract_value(weather_dom, "current_conditions", "condition")
    dom.uplink()
    return data

