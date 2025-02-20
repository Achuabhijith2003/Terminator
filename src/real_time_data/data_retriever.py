class DataRetriever:
    def __init__(self):
        pass

    def get_time(self):
        from datetime import datetime
        return datetime.now().strftime("%H:%M:%S")

    def get_weather(self, location):
        import requests
        api_key = "YOUR_API_KEY"  # Replace with your actual API key
        base_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
        response = requests.get(base_url)
        if response.status_code == 200:
            data = response.json()
            return {
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"],
                "location": data["name"]
            }
        else:
            return None