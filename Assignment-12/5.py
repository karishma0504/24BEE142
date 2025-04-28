class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        # Initialize time with hours, minutes, and seconds
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.normalize_time()

    def normalize_time(self):
        """ Normalize time to make sure minutes and seconds are within proper range. """
        if self.seconds >= 60:
            self.minutes += self.seconds // 60
            self.seconds = self.seconds % 60

        if self.minutes >= 60:
            self.hours += self.minutes // 60
            self.minutes = self.minutes % 60

        # Normalize negative time values (if any)
        if self.seconds < 0:
            self.minutes -= 1
            self.seconds += 60
        if self.minutes < 0:
            self.hours -= 1
            self.minutes += 60
        if self.hours < 0:
            self.hours = 0  # Time can't be negative, setting to zero

    def __add__(self, other):
        """ Overload the + operator to add two Time objects """
        total_seconds = self.to_seconds() + other.to_seconds()
        return Time.from_seconds(total_seconds)

    def __sub__(self, other):
        """ Overload the - operator to subtract two Time objects """
        total_seconds = self.to_seconds() - other.to_seconds()
        return Time.from_seconds(total_seconds)

    def __lt__(self, other):
        """ Less than comparison (used for time comparisons) """
        return self.to_seconds() < other.to_seconds()

    def __eq__(self, other):
        """ Equal to comparison (used for time comparisons) """
        return self.to_seconds() == other.to_seconds()

    def to_seconds(self):
        """ Convert time to total seconds """
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    @classmethod
    def from_seconds(cls, total_seconds):
        """ Convert seconds back into Time object """
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return cls(hours, minutes, seconds)

    def __str__(self):
        """ Return time as a string in the format HH:MM:SS """
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"


# Example usage
time1 = Time(2, 45, 50)  # 2 hours, 45 minutes, 50 seconds
time2 = Time(1, 30, 20)  # 1 hour, 30 minutes, 20 seconds

print(f"Time 1: {time1}")
print(f"Time 2: {time2}")

# Add two times
sum_time = time1 + time2
print(f"Sum of Time 1 and Time 2: {sum_time}")

# Subtract two times
difference_time = time1 - time2
print(f"Difference of Time 1 and Time 2: {difference_time}")

# Comparison
if time1 < time2:
    print("Time 1 is less than Time 2")
elif time1 == time2:
    print("Time 1 is equal to Time 2")
else:
    print("Time 1 is greater than Time 2")
