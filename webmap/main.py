import folium
import pandas as pd

data = pd.read_csv("Volcanoes.txt")
lon = list(data["LON"])
lat = list(data["LAT"])
elev = list(data["ELEV"])

map = folium.Map(location=(38.58,-99.09),zoom_start=6, title="Stamen Terrain")

fg = folium.FeatureGroup(name="my map")

for lt,ln,el in zip(lat,lon,elev):
    if el > 3000:
        map.add_child(folium.Marker(location=[lt,ln], popup=el, icon=folium.Icon(color='red')))
    else:
        map.add_child(folium.Marker(location=[lt, ln], popup=el, icon=folium.Icon(color='green')))




fg.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
                            style_function= lambda x:{'fillColor':'green' if x['properties']['POP2005'] < 10000000
                                                      else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000
                                                      else 'red'}))

map.add_child(fg)
map.add_child(folium.LayerControl())
map.save("map1.html")