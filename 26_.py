class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def get_hour(self):
        return self.__hour

    def get_minute(self):
        return self.__minute

    def get_second(self):
        return self.__second

    def set_time(self, hour, minute, second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def display_time(self):
        print(f"{self.__hour:02d}:{self.__minute:02d}:{self.__second:02d}")

    def __add__(self, other):
        # Overloading the '+' operator to find the sum of two time objects
        total_seconds = (self.__hour + other.get_hour()) * 3600 + \
                        (self.__minute + other.get_minute()) * 60 + \
                        (self.__second + other.get_second())

        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        # Creating a new Time object to store the result
        result_time = Time(hours, minutes, seconds)
        return result_time

# Example usage:
time1 = Time(3, 30, 45)
time2 = Time(1, 15, 20)

sum_time = time1 + time2

print("Time 1:")
time1.display_time()

print("\nTime 2:")
time2.display_time()

print("\nSum of Time 1 and Time 2:")
sum_time.display_time()
