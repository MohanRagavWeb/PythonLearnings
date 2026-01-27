import requests

try:
    url = "https://api.agify.io/?name=mohan"
    response = requests.get(url, timeout=5)

    if response.status_code == 200:
        data = response.json()
        print("Name:", data["name"])
        print("Predicted Age:", data["age"])
    else:
        print("API Error:", response.status_code)

except Exception as e:
    print("Request failed:", e)
