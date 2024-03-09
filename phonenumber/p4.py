# validating the number
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

if phonenumbers.is_possible_number(pase):
    print(" it can be possible number")
else:
    print(" it can not be a possible number")