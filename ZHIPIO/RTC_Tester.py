from RTC_Class import RTC
# Create an instance of the RTC class
rtc = RTC()

if rtc.lost_power:
    print("\n\n------------------------DS3223-RTC------------------------------------------")
    print("Date And Time is not set (RTC Power lost after it's last activity.).\nPlease Set correct datetime")
    print("-------------------------------------------------------------------------------\n")
    #rtc.set_datetime()

rtc.print_current_time()