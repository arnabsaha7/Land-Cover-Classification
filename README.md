# Land Cover Classification Project 🌍
![Python](https://img.shields.io/badge/Python-3.11%2B-blue?logo=python&logoColor=white)
![Earth Engine API](https://img.shields.io/badge/Earth_Engine-API-brightgreen?logo=google-earth&logoColor=white)
![Geemap](https://img.shields.io/badge/Geemap-v0.9.6-orange?logo=google-earth&logoColor=white)
![MODIS Dataset](https://img.shields.io/badge/MODIS_Dataset-v6.1-2F2A29?logo=NASA&logoColor=white)

This project utilizes Google Earth Engine to perform land cover classification for the region of Gujarat using the MODIS Land Cover Type dataset. It implements a Random Forest classifier to predict land cover types based on sampled data.

---
## Features

- Land cover classification using `MODIS` dataset
- Comapring a custom classified layer to landcover dataset
- Visualization of classified results
- Export of training points and classified results in GeoJSON format

---
## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/arnabsaha7/Land-Cover-Classification.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Land-Cover-Classification
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
---
## Usage

1. Ensure you have Google Earth Engine access.
2. Set necessary IAM Roles in [Google Console](https://console.cloud.google.com/) 
3. Run the main script:
   ```bash
   python land_cover_classification.py
   ```
---
## Results

### Output Images

| Map | Land Cover | Classified Land Cover |
|-----|------------|-----------------------|
| ![Map](images/map.png) | ![Land Cover](images/land_cover.png) | ![Classified Land Cover](images/classified_land_cover.png) |
| *Map of Gujarat*       | *Land Cover Types*       | *Classified Land Cover*    |

### Exported Data

- The classified land cover and training points are exported as GeoJSON files located in the `json` folder.

## Contributing

Contributions are welcome! Please create a pull request or open an issue for any enhancements or bugs.

