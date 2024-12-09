import calendar
def isleapyear(year):
        return calendar.isleap(year)
year=int(input("Enter the year : "))
if isleapyear(year):
        print(f"{year} is leap year")
else:
        print(f"{year} is not leap year")
