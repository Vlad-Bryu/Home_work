import ephem
import re
import datetime
a = [" "]

now = datetime.datetime.now()
datetime.datetime.strptime(a[0], '%Y/%m/%d')

'''coord_planet = getattr(ephem, a[0])(now.strftime("%Y/%m-%d"))
coordinate = ephem.constellation(coord_planet)
print(coordinate)
print(now.strftime("%Y-%m-%d"))'''