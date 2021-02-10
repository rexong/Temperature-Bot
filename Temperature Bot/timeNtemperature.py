from datetime import datetime
from random import randint


class timeNtemp(object):
    def get_temp(self):  # return a temperature from 35.8 to 37.2
        return randint(358, 372)  # get temp

    def get_time(self):  # return the current time
        now = datetime.now().strftime("%H:%M:%S")  # 8 char
        return now
