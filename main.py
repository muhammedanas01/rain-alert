import requests
from twilio.rest import Client

OPEN_WHEATHER_MAP_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "7ed1d55db01178a46f7c7c097754fc0c"

account_sid = 'account no. twilio'
auth_token = 'this is authkey'

weather_parameter = {
    "lat": 12.23000000,
    "lon": 76.42000000,
    "cnt": 4,
    "appid": api_key,
}
response = requests.get(OPEN_WHEATHER_MAP_Endpoint, params=weather_parameter)
# response.raise_for_status()
weather_data = response.json()
# print(weather_data)

will_rain = False
for hour_data in weather_data['list']:
    condition = hour_data['weather'][0]['id']
    if condition < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body = "its going to rain today. Remember to bring your umbrella",
        from_='+15709903312',
        to='+912545245845'
    )

    print(message.status)
else:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="its not going to rain today.",
        from_='+15709903312',
        to='+912545245845'
    )

    print(message.status)


