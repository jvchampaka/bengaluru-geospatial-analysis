import pandas as pd
import folium

# Load the CSV created earlier
data_file = "data/bengaluru_top10_locations.csv"
df = pd.read_csv(data_file)

# Create base map centered on Bengaluru
bengaluru_map = folium.Map(
    location=[12.97, 77.59],
    zoom_start=10,
    tiles="OpenStreetMap"
)

# Color coding
color_map = {
    "Bengaluru_Urban": "blue",
    "Bengaluru_Rural": "green"
}

# Add points to map
for _, row in df.iterrows():
    folium.CircleMarker(
        location=[row["latitude"], row["longitude"]],
        radius=6,
        popup=f"""
        <b>Name:</b> {row['name']}<br>
        <b>Category:</b> {row['category']}<br>
        <b>Region:</b> {row['region']}
        """,
        color=color_map[row["region"]],
        fill=True,
        fill_opacity=0.7
    ).add_to(bengaluru_map)

# Save map
output_map = "data/bengaluru_urban_vs_rural_map.html"
bengaluru_map.save(output_map)

print("✅ Map created successfully!")
print(f"🌍 Open this file in browser: {output_map}")
