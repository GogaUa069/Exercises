class DeltaClock:
    def __init__(self, clock1, clock2):
        self.clock1, self.clock2 = clock1, clock2
        self.clock1_secs, self.clock2_secs = self.clock1.get_time(), self.clock2.get_time()

    def get_time_gap(self):
        return self.clock1_secs - self.clock2_secs

    @staticmethod
    def set_time(time_gap):
        hours = time_gap // 3600
        minutes = (time_gap % 3600) // 60
        seconds = time_gap % 60

        hours = str(hours).rjust(2, "0")
        minutes = str(minutes).rjust(2, "0")
        seconds = str(seconds).rjust(2, "0")
        return (f"{hours}: "
                f"{minutes}: "
                f"{seconds}")

    def __str__(self):
        """
        Time Gap
        :return: H:M:S
        """
        if self.clock1_secs < self.clock2_secs:
            return "00: 00: 00"
        else:
            time_sec_gap = self.clock1_secs - self.clock2_secs
            return self.set_time(time_sec_gap)

    def __len__(self):
        """
        Time Gap
        :return: Seconds
        """
        gap = self.clock1_secs - self.clock2_secs
        if gap >= 0:
            return self.clock1_secs - self.clock2_secs
        else:
            return 0


class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        seconds_time = self.hours*3600 + self.minutes*60 + self.seconds
        return seconds_time
