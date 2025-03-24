import requests
key= "917f3e81cdc041caaf674930252103"
respond = requests.get("http://api.weatherapi.com/v1/forecast.json?key=917f3e81cdc041caaf674930252103&q=Liepaja&days=2&aqi=yes&alerts=yes")

data = respond.json()

maxtemp = data["forecast"]["forecastday"][1]["day"]["maxtemp_c"]
print(maxtemp)