import pandas
import folium

data = pandas.read_csv('Volcanoes.txt')

lat = list(data['LAT'])
lon = list(data['LON'])
elevations = list(data['ELEV'])
names = list(data["NAME"])

# Multi-line string
html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

def color_producer(elevation):
    if elevation < 1000: 
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")
fgv = folium.FeatureGroup(name="Volcano Map")

# zip() example:
# 
# for i, j in zip([1,2,3], [4,5,6]):
#   print(i + ',' + j)
# 
# Result:
# 1, 4
# 2, 5
# 3, 6
for lt, ln, el, name in zip(lat, lon, elevations, names):
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    # fgv.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe),
    #   icon=folium.Icon(color=color_producer(el))))
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=str(el) + ' m', 
        fill_color=color_producer(el), color='grey', fill_opacity=0.7))

# Add GeoJson polygon layer
fgp = folium.FeatureGroup(name='Population')
fgp.add_child(folium.GeoJson(data=(open('world.json', 'r', encoding='utf-8-sig').read()),
    style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
        else 'orange' if 1000000 <= x['properties']['POP2005'] < 20000000 else 'red' }))

map.add_child(fgv)
map.add_child(fgp)
# Make sure adding this after the above children added
map.add_child(folium.LayerControl())

# Save as HTML
map.save("VolcanoMap.html")