import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")

if response.status_code == 404:
    print("404: Not Found")
elif response.status_code == 401:
    print("401: Unauthorized")
elif response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Error:", response.status_code)
