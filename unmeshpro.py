import folium
import pandas

data= pandas.read_csv("in.csv")
LNG = list(data["lng"])
LAT = list(data["lat"])
nam = list(data['city'])
pop= list(data["population"])

data1= pandas.read_csv('Volcanoes.txt')
lat1 = list(data1.LAT)
lon1 = list(data1.LON)
elev = list(data1.ELEV)
nam1 = list(data1.NAME)

def color_producer(elevation):
    if elevation < 600000:
        return 'green'
    elif 600000 <= elevation < 2000000:
        return 'orange'
    else:
        return 'red'

def color_producer1(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 2000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[20.5937 , 78.9629],zoom_start=10)

fgp=folium.FeatureGroup(name="India Population")
for lt,ln,nm,el in zip(LAT,LNG,nam,pop):  
    fgp.add_child(folium.CircleMarker(location=[lt , ln],popup=nm,radius=6,fill_color=color_producer(el),color="black",fill_opacity=0.7))

fgv=folium.FeatureGroup(name="Volcanoes in India")
for lt1,ln1,nm1,el1 in zip(lat1,lon1,nam1,elev):
    fgv.add_child(folium.Marker(location=[lt1,ln1],popup=nm1,icon=folium.Icon(color=color_producer1(el1))))

fgwp= folium.FeatureGroup(name="World Population")

fgwp.add_child(folium.GeoJson(data=open('world.json',"r",encoding='utf-8-sig').read(),
style_function= lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000
else 'red'}))



map.add_child(fgp)
map.add_child(fgwp)
map.add_child(fgv)
map.add_child(folium.LayerControl())

map.save("my_first_project.html")
