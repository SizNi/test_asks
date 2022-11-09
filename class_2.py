# мое решение
class HourClock:
    def __init__(self):
        self.time = 0

    @property
    def hours(self):
        return self.time

    @hours.setter
    def hours(self, new_time):
        self.time = new_time % 12

# решение преподавателя
class HourClock:
    def __init__(self):
        """Create a new hour clock."""
        self.hand_position = 0

    @property
    def hours(self):
        return self.hand_position

    @hours.setter
    def hours(self, new_position):
        self.hand_position = new_position % 12
        
clock = HourClock()
clock.hours  # 0
clock.hours = 13
clock.hours = 1    