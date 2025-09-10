import pandas as pd
import simplekml

data = {
    "Name": ["Point A", "Point B", "Point C"],
    "Latitude": [6.5244, 9.0579, 7.3775],
    "Longitude": [3.3792, 7.4951, 3.9470]
}

df_sample = pd.DataFrame(data)
df_sample.to_excel("locations.xlsx", index=False)

print("Sample Excel created: locations.xlsx")

df = pd.read_excel("locations.xlsx", header=0)

kml = simplekml.Kml()

for _, row in df.iterrows():
    name = str(row["Name"])
    lat = float(row["Latitude"])
    lon = float(row["Longitude"])
    kml.newpoint(name=name, coords = [(lon, lat)])
    
kml.savekmz("locations.kmz")
print("KMZ file created: locations.kmz")