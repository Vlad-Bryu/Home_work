from flask import Flask
from weather import weather_in_city
app = Flask(__name__)


@app.route("/")
def hello():
    weather = weather_in_city("Moscow,Russia")
    return f"Погода: {weather['temp_C']}, ощущается как {weather['FeelsLikeC']}"


if __name__ == "__main__":
    app.run(debug=True)

