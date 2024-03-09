import folium
import geocoder

g=geocoder.ip("192.168.218.1")

myadd=g.latlng

map1=folium.Map(location=myadd,zoom_start=9)

folium.CircleMarker(location=myadd,radius=50,popup="yorksshir").add_to(map1)

map1.save("l.html")