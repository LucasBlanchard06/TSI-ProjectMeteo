import datetime
import math
from sklearn.linear_model import LinearRegression
import numpy as np
 
# ----- RISK CALCULATION -----
 
def calculate_risk(weather):
   score = 0
 
   if weather["wind_kmh"] > 40: score += 2
   if weather["wind_kmh"] > 70: score += 3
   if weather["rain_mm"] > 10: score += 2
   if weather["storm"]: score += 4
   if weather["visibility_km"] < 5: score += 2
   if weather["visibility_km"] < 2: score += 3
 
   return score
 
 
# ----- STORAGE -----
 
weather_data = {}
model = None
 
 
# ----- DATE ENCODING FOR PATTERN LEARNING -----
 
def encode_date(date):
   dt = datetime.datetime.strptime(date, "%Y-%m-%d")
   day = dt.timetuple().tm_yday  # Day of year: 1 → 365
 
   # Cyclic encoding (captures seasonal pattern)
   sin_val = math.sin(2 * math.pi * day / 365)
   cos_val = math.cos(2 * math.pi * day / 365)
 
   return sin_val, cos_val
 
 
# ----- ADD WEATHER DATA -----
 
def add_data():
   print("\n--- Add Weather Data ---")
   date = input("Date (YYYY-MM-DD): ")
 
   # Check date
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
 
 
# ----- MACHINE LEARNING USING YEARLY PATTERN -----
 
def train_model():
   global model
 
   if len(weather_data) < 5:
       print("❌ Not enough data to train the model (min 5).")
       return False
 
   X = []
   y = []
 
   for date, values in weather_data.items():
       sin_val, cos_val = encode_date(date)
       X.append([sin_val, cos_val])  # Pattern only
       y.append(values["risk"])
 
   model = LinearRegression()
   model.fit(X, y)
 
   print("✔ Pattern-learning model trained successfully!")
   return True
 
 
# ----- FUTURE RISK PREDICTION BASED ONLY ON DATE -----
 
def future_prediction():
   if model is None:
       print("❌ Model not trained. Use menu option 2.")
       return
 
   print("\n--- Future Risk Prediction ---")
   date = input("Flight date (YYYY-MM-DD): ")
 
   try:
       datetime.datetime.strptime(date, "%Y-%m-%d")
   except ValueError:
       print("❌ Invalid date format.")
       return
 
   sin_val, cos_val = encode_date(date)
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
 
 
# ----- SEASON ANALYSIS (OPTIONAL) -----
 
def season(date):
   month = int(date[5:7])
   if month in [12,1,2]: return "Winter"
   if month in [3,4,5]: return "Spring"
   if month in [6,7,8]: return "Summer"
   return "Autumn"
 
 
def season_analysis():
   if not weather_data:
       print("❌ No recorded data.")
       return
 
   stats = {"Winter": [], "Spring": [], "Summer": [], "Autumn": []}
 
   for date, values in weather_data.items():
      stats[season(date)].append(values["risk"])
 
   print("\n--- Seasonal Analysis ---")
   for s, risks in stats.items():
       if risks:
           print(f"{s}: average risk = {sum(risks)/len(risks):.2f}")
       else:
           print(f"{s}: no data")
 
 
# ----- MENU -----
 
def menu():
   while True:
       print("\n======== MENU ========")
       print("1. Add weather data")
       print("2. Train the prediction model")
       print("3. Predict future risk")
       print("4. Season analysis")
       print("5. Display stored data")
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
       elif choice == "0":
           break
       else:
           print("❌ Invalid choice.")
 
 
menu()
