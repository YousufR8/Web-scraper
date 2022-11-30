from bs4 import BeautifulSoup
import requests

print("Let's check the weather where you want to visit.")
city = input("Pick a city: ")
state = input("What state is that in? ")
url = f'https://www.wunderground.com/weather/us/{state}/{city}'

response = requests.get(url)
# print(response.text)
soup = BeautifulSoup(response.content,'html.parser')

# temps = soup.find_all('a')
temp = soup.find(class_ ='wu-value wu-value-to')
# print(temp.text)s
int_temp = int(temp.text)
comfortability = ""

if int_temp >= 90:
    comfortability = "too hot!!!"
elif int_temp < 90 and int_temp > 65:
    comfortability = "just right!"
else:
    comfortability = "way too freaking cold."

print(f"It's curently {int_temp} degrees. It's {comfortability}")
