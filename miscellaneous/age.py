from time import localtime, sleep
from datetime import datetime
from calendar import month

date_format = "%m-%d-%Y %H:%M:%S"
def dates():
    birthday = datetime.strptime("9-15-2003 00:00:00", date_format)
    print(month(localtime().tm_year, localtime().tm_mon))
    print("Today :", f"{localtime().tm_mon}-{localtime().tm_mday}-{localtime().tm_year} {localtime().tm_hour}:{localtime().tm_min}:{localtime().tm_sec}")
    print("Day of the year: ", localtime().tm_yday)
    print("Days to birthday: ",datetime.strptime(f"9-15-{localtime().tm_year} 00:00:00", date_format) - datetime.strptime(f"{localtime().tm_mon}-{localtime().tm_mday}-{localtime().tm_year} {localtime().tm_hour}:{localtime().tm_min}:{localtime().tm_sec}", date_format), str("hours"))
    print("Age: ", (datetime.strptime(f"{localtime().tm_mon}-{localtime().tm_mday}-{localtime().tm_year} {localtime().tm_hour}:{localtime().tm_min}:{localtime().tm_sec}", date_format) - birthday).days / 365.25, str("years") )
    print("\n")

if __name__ == "__main__":
    dates()