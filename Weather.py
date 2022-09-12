import requests

KEY_API = "59cdc5ac43a49d36cc23f3fcc8c0ed22"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city : ")
request_URL = f"{BASE_URL}?appid={KEY_API}&q={city}"
response = requests.get(request_URL)

if response.status_code == 200 :
   data = response.json()
   weather = data['weather'][0]['description']
   print( " The weather is ", weather)
   temp = round(data['main']['temp'] - 273.15 , 2)
   print(  "temerature in celsius" , temp)


else :
    print("Error occured")    