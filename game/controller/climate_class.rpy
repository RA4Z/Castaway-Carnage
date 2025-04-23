# CRIAR CLASSE PARA DATA E HORA DO MOMENTO, TEMPERATURA E CLIMA. 

python early:
    import datetime
    import random

    class WorldState:
        def __init__(self, start_hour=8):
            self.current_time = datetime.datetime(2025, 1, 1, start_hour, 0, 0)  # Year, month, day are arbitrary but required
            self.temperature = 25  # Initial temperature (Celsius) - adjust as needed
            self.weather = "Clean" # Initial weather - can be any string you like ("Rainy", "Cloudy", etc.)
            self.weathers = ["Clean", "Cloudy", "Rainy", "Foggy"] # Weather options to randomize from (expand as needed)

        def advance_time(self, hours=0, minutes=0, days=0):
            """Advances the game time.
            
            Args:
                hours (int): Number of hours to advance.
                minutes (int): Number of minutes to advance.
                days (int): Number of days to advance.
            """
            time_delta = datetime.timedelta(hours=hours, minutes=minutes, days=days)
            self.current_time += time_delta

            # Update temperature and weather based on time passage (example)
            self.update_temperature()
            self.update_weather()

        def update_temperature(self):
            """Updates the temperature based on the time of day (example logic)."""
            current_hour = self.current_time.hour
            if 6 <= current_hour < 12:  # Morning
                self.temperature += random.randint(1, 3)

            elif 12 <= current_hour < 18: # Afternoon
                self.temperature += random.randint(0, 2)
                
            elif 18 <= current_hour < 24 or 0 <= current_hour < 6:  # Night
                self.temperature -= random.randint(1, 3)
            
            # Clamp temperature to reasonable values (avoiding too extreme shifts)
            self.temperature = min(max(self.temperature, 0), 40) # Example: Between 0 and 40 Celsius


        def update_weather(self):
            if random.random() < 0.2:  # 20% chance of weather change
                self.weather = random.choice(self.weathers)


        def get_time_string(self, format_string="%I:%M %p"):
            return self.current_time.strftime(format_string)