# validating the number
import phonenumbers
from phonenumbers import timezone
from phonenumbers import geocoder,carrier
from opencage.geocoder import OpenCageGeocode
import folium
number="+918248431135"
pase=phonenumbers.parse(number)

timezone=timezone.time_zones_for_number(pase)
# print(timezone)

carrie=carrier.name_for_number(pase,"en")
# print(carrie)
geo_location= geocoder.country_name_for_number(pase,"en")
# print(geo)

# if phonenumbers.is_possible_number(pase):
#     print(" it can be possible number")
# else:
#     print(" it can not be a possible number")

ai_key="2bff9b1eb36d4cb3bd8c46b566e0dab8"
geocoder = OpenCageGeocode(ai_key)
query=str(geo_location)
result = geocoder.geocode(query)

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']
print(lat)
print(lng)

map_location=folium.Map(location=[lat,lng],zoom_start=11)
folium.Marker([lat,lng],popup=geo_location).add_to(map_location)
map_location.save("location.html")