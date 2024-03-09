# timezone and country name
import phonenumbers
from phonenumbers import timezone
from phonenumbers import geocoder,carrier
number="+918248431135"
pase=phonenumbers.parse(number)

timezone=timezone.time_zones_for_number(pase)
print(timezone)

carrie=carrier.name_for_number(pase,"en")
print(carrie)
geo = geocoder.country_name_for_number(pase,"en")
print(geo)