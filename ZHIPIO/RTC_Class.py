import time
import board
import adafruit_ds3231

class RTC:
    def __init__(self):
        i2c = board.I2C()  # uses board.SCL and board.SDA
        try:
            self.rtc = adafruit_ds3231.DS3231(i2c)
        except:
            print("\n\n------------------------------------------------------------------")
            print("Real time clock module (DS-3232) is not found.\nThe battery is low or DS-2233 RTC module disconnected from sircuire or burned out !")
            print("------------------------------------------------------------------\n")
            exit()

    def set_date_time(self, year, mon, day, hour, minuete, sec, wday):
        # year, mon, date, hour, min, sec, wday, yday, isdst
        t = time.struct_time((year, mon, day, hour, minuete, sec, wday, -1, -1))
        print("Setting time to:", t)  # uncomment for debugging
        self.rtc.datetime = t
        print()
        
    def set_datetime_from_command_line(self):
        year = int(input('Enter YEAR:'))
        mon = int(input('Enter MONTH:'))
        day = int(input('Enter DAY:'))
        hour = int(input('Enter HOUR:'))
        min = int(input('Enter MIN:'))
        sec = int(input('Enter SEC:'))
        self.set_date_time(year, mon, day, hour, min, sec, 0)
    
    def get_rtc_time_now_string(self):
        t = self.rtc.datetime
        return str(t.tm_hour) + ":" + str(t.tm_min) + ":" + str(t.tm_sec)
    
    def get_rtc_year_now_string(self):
        t = self.rtc.datetime
        return str(t.tm_year)
    
    def get_rtc_month_now_string(self):
        t = self.rtc.datetime
        return str(t.tm_mon)
    
    def get_rtc_day_now_string(self):
        t = self.rtc.datetime
        return str(t.tm_mday)
    
    def get_rtc_sec_now_string(self):
        t = self.rtc.datetime
        return str(t.tm_sec)
    
    def print_current_time(self):
        dt = self.rtc.datetime
        tmp = self.rtc.temperature
        print("\n\n------------------------DS3223-RTC------------------------------------------")
        print( "\nThe date is {} {}/{}/{}".format(days[int(dt.tm_wday)], dt.tm_mday, dt.tm_mon, dt.tm_year ))
        print( "The time is {}:{:02}:{:02}".format(dt.tm_hour, dt.tm_min, dt.tm_sec ))
        print( "Mudule Temp = "+str(tmp))
        print("-------------------------------------------------------------------------------\n")
        
    @property
    def lost_power(self):
        return self.rtc.lost_power

# Lookup table for names of days (nicer printing).
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")