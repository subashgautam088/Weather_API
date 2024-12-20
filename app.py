from flask import Flask, render_template, request
import requests

app = Flask(__name__)


API_KEY = "b87b79610450c442c876b6336d72f012"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"



# Define the API Details
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/weather", methods=['POST', 'GET'])
def weather():
    city = request.form.get('city')
    if not city:
        return render_template("index.html",error="Please enter a city name.")
    
    # Fetch data from OpenWeather API
    try:
        params = {"q": city, "appid":API_KEY, "units":"metric"}
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        
        if data['cod'] != 200:
            return render_template('index.html', error="City not found!")
        
        weather_data = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "icon": data["weather"][0]["icon"],
        }
        return render_template('weather.html', weather= weather_data)
    except Exception as e:
        return render_template('index.html', error="An error occurred. Please try again")
    
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5007)