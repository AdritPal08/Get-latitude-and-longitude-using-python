# import necessary libraries
from geopy.geocoders import Bing
import pandas as pd

# loading all datasets
exports = pd.read_csv("Stripped exports.csv",dtype='object')
imports = pd.read_csv("Stripped imports.csv",dtype='object')
exports_country = exports['Country'].unique().tolist()
imports_country = imports['Country'].unique().tolist()
countries = list(set(exports_country + imports_country))
len = len(countries)
print("Length of Country list: ",len)

# loading BingMap APi Key
with open('BingMapApiKey.txt', 'r') as file:
    key = file.read()
geolocator = Bing(key)

lat = []
long = []
Country =[]
Geo_Country =[]
for i in range(len):
    Country.append(countries[i])
    # location = geolocator.geocode(export_country[i],timeout=1)
    location = geolocator.geocode(countries[i])
    if location is None:
        # lat.append("")
        # long.append("")
        latitude = ""
        longitude = ""
        loc=""

        print(i,location,"-","","")
    else:
        latitude = location.latitude
        longitude = location.longitude
        loc=location[0]

        print(i,location,"-",location.latitude, location.longitude)
    lat.append(latitude)
    long.append(longitude)
    Geo_Country.append(loc)

GeoData = pd.DataFrame({'Country':Country,'latitude':lat,'longitude':long,'GeoCountryName':Geo_Country})
print(GeoData.head())
print(GeoData.shape)
#Save the GeoData
GeoData.to_csv('country_geodata.csv')

##Merge Geodata with Main Dataset and save the new Datset
# export_data = pd.merge(exports, GeoData, on='Country')
# export_data.to_csv('export_data.csv')

# import_data = pd.merge(exports, GeoData, on='Country')
# import_data.to_csv('import_data.csv')