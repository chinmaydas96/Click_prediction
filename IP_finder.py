# -*- coding: utf-8 -*-



from sys import argv, stderr, exit
from geoip import geolite2

IP_PROVIDER = "http://httpbin.org/ip"
comma_sep = lambda x: ", ".join([str(y) for y in x])

if not argv[1:]:
    from urllib2 import urlopen
    from json import load

    ip = load(urlopen(IP_PROVIDER))["origin"]
else:
    ip = argv[1]

#try:
match = geolite2.lookup(ip)
#except ValueError, e:
#    stderr.write(str(e) + "\n")
#    exit(1)

if not match:
    stderr.write("No IP %s found\n" % ip)
    exit(2)

print("IP: %s" % match.ip)
print("Country: %s" % match.country)
print("Continent: %s" % match.continent)
print("Subvisions: %s" % comma_sep(match.subdivisions))
print("Timezone: %s" % match.timezone)
print("Location: %s" % comma_sep(match.location))