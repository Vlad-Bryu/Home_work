import ephem
import re
import datetime

now = datetime.datetime.now()
coord_planet = ephem.Mars(now.strftime("%Y/%m-%d"))
coordinate = ephem.constellation(coord_planet)
print(coordinate)
print(now.strftime("%Y-%m-%d"))