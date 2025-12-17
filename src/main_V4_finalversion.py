import datetime

import math

import random

from sklearn.linear_model import LinearRegression

import numpy as np
 
# ---------------------------------

# RISK CALCULATION

# ---------------------------------
 
def calculate_risk(weather):

    score = 0
 
    if weather["wind_kmh"] > 40:

        score += 2

    if weather["wind_kmh"] > 70:

        score += 3

    if weather["rain_mm"] > 10:

        score += 2

    if weather["storm"]:

        score += 4

    if weather["visibility_km"] < 5:

        score += 2

    if weather["visibility_km"] < 2:

        score += 3
 
    return score
 
 
# ---------------------------------

# DATA STORAGE

# ---------------------------------
 
weather_data = {}

model = None
 
 
# ---------------------------------

# SEASON DETECTION (ROBUST)

# ---------------------------------
 
def get_season(date):

    try:

        dt = datetime.datetime.strptime(date, "%Y-%m-%d")

    except ValueError:

        return None  # Date invalide, on gère plus tard

    month = dt.month

    if month in [12, 1, 2]:

        return "Winter"

    if month in [3, 4, 5]:

        return "Spring"

    if month in [6, 7, 8]:

        return "Summer"

    return "Autumn"
 
 
# ---------------------------------

# SEASON-BASED WEATHER GENERATION

# ---------------------------------
 
def generate_weather_for_season(season):

    if season == "Winter":

        return {

            "wind_kmh": random.uniform(20, 80),

            "rain_mm": random.uniform(0, 25),

            "storm": random.random() < 0.25,

            "visibility_km": random.uniform(1, 8),

        }
 
    if season == "Spring":

        return {

            "wind_kmh": random.uniform(10, 60),

            "rain_mm": random.uniform(0, 20),

            "storm": random.random() < 0.15,

            "visibility_km": random.uniform(5, 15),

        }
 
    if season == "Summer":

        return {

            "wind_kmh": random.uniform(0, 40),

            "rain_mm": random.uniform(0, 10),

            "storm": random.random() < 0.05,

            "visibility_km": random.uniform(10, 25),

        }
 
    if season == "Autumn":

        return {

            "wind_kmh": random.uniform(10, 70),

            "rain_mm": random.uniform(0, 30),

            "storm": random.random() < 0.20,

            "visibility_km": random.uniform(3, 12),

        }
 
 
# ---------------------------------

# ADD WEATHER MANUALLY

# ---------------------------------
 
def add_data():

    print("\n--- Add Weather Data ---")

    date = input("Date (YYYY-MM-DD): ")
 
    try:

        datetime.datetime.strptime(date, "%Y-%m-%d")

    except ValueError:

        print("❌ Invalid date format.")

        return
 
    wind = float(input("Wind (km/h): "))

    rain = float(input("Rain (mm): "))

    storm = input("Storm? (y/n): ").lower() == "y"

    visibility = float(input("Visibility (km): "))
 
    weather_data[date] = {

        "wind_kmh": wind,

        "rain_mm": rain,

        "storm": storm,

        "visibility_km": visibility,

    }
 
    weather_data[date]["risk"] = calculate_risk(weather_data[date])
 
    print(f"✔ Data added for {date}.")
 
 
# ---------------------------------

# AUTO-GENERATION FOR ONE DAY

# ---------------------------------
 
def auto_generate_one_day():

    print("\n--- Automatic Weather Generation ---")

    date = input("Date (YYYY-MM-DD): ")
 
    try:

        datetime.datetime.strptime(date, "%Y-%m-%d")

    except ValueError:

        print("❌ Invalid date format.")

        return
 
    season = get_season(date)

    if season is None:

        print("❌ Invalid date, cannot generate weather.")

        return
 
    meteo = generate_weather_for_season(season)
 
    weather_data[date] = meteo

    weather_data[date]["risk"] = calculate_risk(meteo)
 
    print(f"✔ Automatic seasonal weather generated for {date} ({season}).")
 
 
# ---------------------------------

# AUTO-GENERATION FOR MULTIPLE DAYS

# ---------------------------------
 
def auto_generate_multiple_days():

    print("\n--- Automatic Multi-Day Weather Generation ---")

    start_date = input("Start date (YYYY-MM-DD): ")

    try:

        days = int(input("How many days to generate? "))

    except ValueError:

        print("❌ Invalid number of days.")

        return
 
    try:

        current = datetime.datetime.strptime(start_date, "%Y-%m-%d")

    except ValueError:

        print("❌ Invalid start date format.")

        return
 
    for _ in range(days):

        date_str = current.strftime("%Y-%m-%d")

        season = get_season(date_str)

        if season is None:

            print(f"⚠ Skipping invalid date: {date_str}")

            current += datetime.timedelta(days=1)

            continue
 
        meteo = generate_weather_for_season(season)

        weather_data[date_str] = meteo

        weather_data[date_str]["risk"] = calculate_risk(meteo)
 
        current += datetime.timedelta(days=1)
 
    print(f"✔ {days} days of automatic weather generated starting from {start_date}.")
 
 
# ---------------------------------

# DATE ENCODING FOR AI

# ---------------------------------
 
def encode_date(date):

    try:

        dt = datetime.datetime.strptime(date, "%Y-%m-%d")

    except ValueError:

        return None, None

    day = dt.timetuple().tm_yday
 
    sin_val = math.sin(2 * math.pi * day / 365)

    cos_val = math.cos(2 * math.pi * day / 365)
 
    return sin_val, cos_val
 
 
# ---------------------------------

# TRAINING THE IA MODEL

# ---------------------------------
 
def train_model():

    global model
 
    if len(weather_data) < 5:

        print("❌ Not enough data to train the model (min 5).")

        return False
 
    X = []

    y = []
 
    for date, values in weather_data.items():

        sin_val, cos_val = encode_date(date)

        if sin_val is None:

            print(f"⚠ Skipping invalid date for training: {date}")

            continue

        X.append([sin_val, cos_val])

        y.append(values["risk"])
 
    model = LinearRegression()

    model.fit(X, y)
 
    print("✔ Pattern-learning model trained successfully!")

    return True
 
 
# ---------------------------------

# FUTURE RISK PREDICTION

# ---------------------------------
 
def future_prediction():

    if model is None:

        print("❌ Model not trained. Use menu option 2.")

        return
 
    date = input("Flight date (YYYY-MM-DD): ")
 
    sin_val, cos_val = encode_date(date)

    if sin_val is None:

        print("❌ Invalid date format.")

        return
 
    X_test = np.array([[sin_val, cos_val]])

    prediction = model.predict(X_test)[0]

    prediction = round(prediction, 2)
 
    print(f"\n📈 **Estimated risk for {date}: {prediction}**")
 
    if prediction <= 2:

        print("✔ Low risk: flight likely safe.")

    elif prediction <= 5:

        print("⚠ Moderate risk: caution advised.")

    else:

        print("❌ HIGH RISK: potentially dangerous flight.")
 
 
# ---------------------------------

# SEASONAL ANALYSIS

# ---------------------------------
 
def season_analysis():

    if not weather_data:

        print("❌ No recorded data.")

        return
 
    stats = {"Winter": [], "Spring": [], "Summer": [], "Autumn": []}
 
    for date, values in weather_data.items():

        season = get_season(date)

        if season is None:

            print(f"⚠ Skipping invalid date: {date}")

            continue

        stats[season].append(values["risk"])
 
    print("\n--- Seasonal Analysis ---")

    for s, risks in stats.items():

        if risks:

            print(f"{s}: average risk = {sum(risks)/len(risks):.2f}")

        else:

            print(f"{s}: no data")
 
 
# ---------------------------------

# MENU

# ---------------------------------
 
def menu():

    while True:

        print("\n======== MENU ========")

        print("1. Add weather data manually")

        print("2. Train the prediction model")

        print("3. Predict future risk")

        print("4. Season analysis")

        print("5. Display stored data")

        print("6. Auto-generate weather for one day")

        print("7. Auto-generate weather for multiple days")

        print("0. Quit")
 
        choice = input("Your choice: ")
 
        if choice == "1":

            add_data()

        elif choice == "2":

            train_model()

        elif choice == "3":

            future_prediction()

        elif choice == "4":

            season_analysis()

        elif choice == "5":

            print("\n--- Stored Data ---")

            for d, v in weather_data.items():

                print(d, ":", v)

        elif choice == "6":

            auto_generate_one_day()

        elif choice == "7":

            auto_generate_multiple_days()

        elif choice == "0":

            break

        else:

            print("❌ Invalid choice.")
 
 
menu()

 
