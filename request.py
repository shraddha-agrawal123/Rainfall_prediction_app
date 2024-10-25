import requests

# URL to the local Flask API endpoint
url = 'http://127.0.0.1:5000/predict'

# Example input data
data = {
    'pressure': 1010,
    'temperature': 25,
    'dewpoint': 15,
    'humidity': 85,
    'cloud': 50,
    'sunshine': 8,
    'winddirection': 150,
    'windspeed': 10
}

# Make the POST request
response = requests.post(url, json=data)

# Print the response
if response.status_code == 200:
    result = response.json()
    print(f"Probability of rainfall: {result['rainfall_probability']:.2f}")
else:
    print("Error:", response.text)
