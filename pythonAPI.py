import requests

url = '<API_URL>'
response = requests.get(url)

# Handle the response
if response.status_code == 200:
    data = response.json()
    # Process the data
else:
    print('Error:', response.status_code)
