# Application Programming Interfaces (API's)

# 🚨
import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)
print(response.status_code)
# Errors
# 1XX: Hold on,
# 2XX: Here You Go
# 3XX: Go Away
# 4XX: You Screwed Up
# 5XX: I Screwed Up
print("\n")

# 🚨
response = requests.get(url="http://api.open-notify.org/is-now.json")
print(response)
print(response.status_code)

print("\n")

# 🚨
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()
print(data)
print("\n")
iss_position = response.json()["iss_position"]
print(iss_position)
print("\n")
longitude = response.json()["iss_position"]["longitude"]
print(longitude)

print("\n")

# 🚨
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()

longitude = response.json()["iss_position"]["longitude"]
latitude = response.json()["iss_position"]["latitude"]

iss_position = (longitude, latitude)
print(iss_position)

