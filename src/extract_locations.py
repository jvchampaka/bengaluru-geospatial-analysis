import os
import osmnx as ox
import pandas as pd

# Enable logging and caching
ox.settings.log_console = True
ox.settings.use_cache = True

# Define regions
regions = {
    "Bengaluru_Urban": "Bengaluru Urban, Karnataka, India",
    "Bengaluru_Rural": "Bengaluru Rural, Karnataka, India"
}

# Define tags
categories = {
    "Park": {"leisure": "park"},
    "Hospital": {"amenity": "hospital"},
    "Waterbody": {"natural": "water"}
}

# Ensure output folder exists
os.makedirs("data", exist_ok=True)

all_results = []

for region_name, place_name in regions.items():
    print(f"\n📍 Processing region: {region_name}")

    for category_name, tags in categories.items():
        print(f"  → Fetching {category_name}s")

        try:
            gdf = ox.features_from_place(place_name, tags)

            if gdf.empty:
                print("    No data found.")
                continue

            # Keep required columns
            gdf = gdf[["name", "geometry"]].dropna(subset=["geometry"])

            # Extract latitude & longitude
            gdf["latitude"] = gdf.geometry.centroid.y
            gdf["longitude"] = gdf.geometry.centroid.x

            # Add metadata columns
            gdf["region"] = region_name
            gdf["category"] = category_name

            # Sort by name and take top 10
            gdf = gdf.sort_values(by="name").head(10)

            all_results.append(
                gdf[["name", "category", "region", "latitude", "longitude"]]
            )

        except Exception as e:
            print(f"    Error fetching {category_name}: {e}")

# Combine all results
final_df = pd.concat(all_results, ignore_index=True)

# Save to CSV
output_file = "data/bengaluru_top10_locations.csv"
final_df.to_csv(output_file, index=False)

print("\n✅ Data extraction complete!")
print(f"📁 Saved file to: {output_file}")
print(final_df)
