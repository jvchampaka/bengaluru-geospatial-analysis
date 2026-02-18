# Bengaluru Geospatial Analysis (Urban vs Rural)

## 📌 Project Overview
This project performs a geospatial analysis of Bengaluru (Karnataka, India) using OpenStreetMap data.  
It extracts and visualizes key public infrastructure locations and compares **Urban vs Rural** regions.

## 📊 Features Extracted
- 🏥 Hospitals
- 🌳 Parks
- 🌊 Water bodies (lakes, tanks, rivers)

## 🛠️ Technologies Used
- Python
- OSMnx
- GeoPandas
- Pandas
- Folium
- OpenStreetMap

## 🗺️ Output
- Clean CSV datasets
- Interactive HTML map with:
  - Color-coded markers
  - Popups with name, category, and region
  - Urban vs Rural comparison

## 📁 Project Structure
bengaluru_geospatial_project/
├── src/
├── data/
├── README.md
├── requirements.txt


---

## 🚀 How to Run

```bash
pip install -r requirements.txt
python src/extract_locations.py
python src/plot_map.py

Open the generated HTML file using Live Server.

Link: https://jvchampaka.github.io/bengaluru-geospatial-analysis/bengaluru_urban_vs_rural_map.html

