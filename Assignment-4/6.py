# Prompt: Print 24 hours of the day with suitable suffixes like AM, PM, Noon, and Midnight

for hour in range(24):
    if hour == 0:
        print(f"12:00 AM (Midnight)")
    elif hour == 12:
        print(f"12:00 PM (Noon)")
    elif hour < 12:
        print(f"{hour}:00 AM")
    else:
        print(f"{hour - 12}:00 PM")
