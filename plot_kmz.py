import pandas as pd
import simplekml

file_path = "KMZ_Design_Summary.xlsx"
df = pd.read_excel(file_path)

kml = simplekml.Kml()

type_colors = {
    "MH": simplekml.Color.red,
    "Other": simplekml.Color.blue,
    "FAT BOUNDARY": simplekml.Color.green
}

for _, row in df.iterrows():
    name = str(row["Name"])
    ttype = str(row["Type"])
    coords_text = str(row["Coordinates"]).strip()
    desc = f"Type: {ttype}"
    if not pd.isna(row.get("Street", None)):
        desc += f"<br>Street: {row['Street']}"


    coords = [tuple(map(float, c.split(","))) for c in coords_text.split()]
    
    if len(coords) == 1:

        pnt = kml.newpoint(name=name, coords=[(coords[0][0], coords[0][1])])
        pnt.description = desc
        pnt.style.iconstyle.color = type_colors.get(ttype, simplekml.Color.white)

    else:

        poly = kml.newpolygon(name=name)
        poly.outerboundaryis = [(c[0], c[1]) for c in coords]
        poly.description = desc
        poly.style.polystyle.color = simplekml.Color.changealphaint(100, type_colors.get(ttype, simplekml.Color.yellow))
        poly.style.linestyle.color = type_colors.get(ttype, simplekml.Color.yellow)


kml.savekmz("KMZ_Design_Output.kmz")
print("KMZ file created: KMZ_Design_Output.kmz")
