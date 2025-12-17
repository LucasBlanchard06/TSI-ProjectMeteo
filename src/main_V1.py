import datetime

# ----- RISK CALCULATION -----

def calculate_risk(weather):
    score = 0

    # Wind
    if weather["wind_kmh"] > 40:
        score += 2
    if weather["wind_kmh"] > 70:
        score += 3

    # Rain
    if weather["rain_mm"] > 10:
        score += 2

    # Thunderstorm
    if weather["thunderstorm"]:
        score += 4

    # Visibility
    if weather["visibility_km"] < 5:
        score += 2
    if weather["visibility_km"] < 2:
        score += 3

    return score


# ----- SEASONS -----

def get_season(date_str):
    # Date format is YYYY-MM-DD
    try:
        month = int(date_str[5:7])
        if month in [12, 1, 2]:
            return "Winter"
        elif month in [3, 4, 5]:
            return "Spring"
        elif month in [6, 7, 8]:
            return "Summer"
        else:
            return "Autumn"
    except ValueError:
        return "Unknown"


# ----- DATABASE -----

weather_data = {}


def add_data():
    print("\n--- Add Weather Data ---")
    date_str = input("Date (format YYYY-MM-DD): ")

    try:
        datetime.datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print("❌ Incorrect date format. Please use YYYY-MM-DD.")
        return

    try:
        wind = float(input("Wind (km/h): "))
        rain = float(input("Rain (mm): "))
        storm_input = input("Thunderstorm? (y/n): ").lower()
        visibility = float(input("Visibility (km): "))
    except ValueError:
        print("❌ Error: Please enter numbers for wind, rain, and visibility.")
        return

    thunderstorm = (storm_input == "y")

    weather_data[date_str] = {
        "wind_kmh": wind,
        "rain_mm": rain,
        "thunderstorm": thunderstorm,
        "visibility_km": visibility,
    }

    # Calculate risk immediately
    weather_data[date_str]["risk_score"] = calculate_risk(weather_data[date_str])

    print(f"✔ Data added for {date_str}. Calculated risk score: {weather_data[date_str]['risk_score']}")


# ----- ANALYSIS -----

def analyze_seasons():
    if not weather_data:
        print("❌ No data recorded.")
        return

    stats = {"Winter": [], "Spring": [], "Summer": [], "Autumn": []}

    for date_str, values in weather_data.items():
        season = get_season(date_str)
        if season in stats:
            stats[season].append(values["risk_score"])

    print("\n--- Seasonal Analysis ---")
    for season, risks in stats.items():
        if risks:
            average = sum(risks) / len(risks)
            print(f"{season}: average risk = {average:.2f} (over {len(risks)} entries)")
        else:
            print(f"{season}: no data")


# ----- FLIGHT RISK CHECK -----

def check_flight_risk():
    print("\n--- Flight Risk Analysis ---")
    date_str = input("Enter flight date (YYYY-MM-DD): ")

    if date_str not in weather_data:
        print("❌ No weather data found for this date.")
        return

    score = weather_data[date_str]["risk_score"]

    if score <= 2:
        print(f"✔ Low Risk ({score}): Safe to fly.")
    elif score <= 5:
        print(f"⚠ Moderate Risk ({score}): Proceed with caution.")
    else:
        print(f"❌ HIGH RISK ({score}): DANGEROUS to fly!")


# ----- MAIN MENU -----

def menu():
    while True:
        print("\n" + "="*10 + " MENU " + "="*10)
        print("1. Add weather data")
        print("2. Analyze seasons")
        print("3. Check flight risk")
        print("4. Show all data")
        print("0. Exit")

        choice = input("Your choice: ")

        if choice == "1":
            add_data()
        elif choice == "2":
            analyze_seasons()
        elif choice == "3":
            check_flight_risk()
        elif choice == "4":
            print("\n--- Recorded Weather Data ---")
            if not weather_data:
                print("No data.")
            else:
                for date, data in weather_data.items():
                    print(f"{date}: {data}")
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("❌ Invalid choice.")


# ----- ENTRY POINT -----

if __name__ == "__main__":
    menu()
