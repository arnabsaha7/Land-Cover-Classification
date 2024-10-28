### **Import Dependencies**
import ee
import geemap
from geemap import ee_export_image_collection

### **Authorize & Initialize Earth-Engine**
ee.Authenticate()
ee.Initialize(project='ee-bdon0387')

### **Select a Region of Interest**
# Define the region of interest.
roi = ee.Geometry.Rectangle([68.1, 20.1, 74.6, 24.7])  # Gujarat boundaries

### **Load MODIS Land Cover Type Dataset**
# Load the MODIS Land Cover Type dataset and get the first image for the specified year.
landcover = ee.ImageCollection("MODIS/061/MCD12Q1") \
            .filterDate('2020-01-01', '2022-12-31') \
            .first() \
            .select(['LC_Type1', 'LC_Type2', 'LC_Type3'])

# Visualization parameters for the IGBP classification scheme
visualization = {
    'min': 1,
    'max': 17,
    'palette': [
        '05450a', '086a10', '54a708', '78d203', '009900', 'c6b044', 'dcd159',
        'dade48', 'fbff13', 'b6ff05', '27ff87', 'c24f44', 'a5a5a5', 'ff6d4c',
        '69fff8', 'f9ffa4', '1c0dff'
    ]
}

### **Classification Model**
# Sample the land cover points within the ROI for training
training_points = landcover.sample(
    region=roi,
    scale=500,
    numPixels=500,
    geometries=True  # Keep geometries for debugging if needed
)

bands = ['LC_Type2', 'LC_Type3']

# Train a Random Forest classifier on the sampled points
classifier = ee.Classifier.smileRandomForest(10).train(
    features=training_points,
    classProperty='LC_Type1',  # Ensure it matches the selected class
    inputProperties=bands
)

# Classify the land cover image
classified_image = landcover.select(bands).classify(classifier)

# Visualization parameters for the classified image
classified_vis = {
    'min': 1,
    'max': 17,
    'palette': visualization['palette']
}

### **Display Results on Map**
# Initialize geemap map object and add layers
Map = geemap.Map()
Map.centerObject(roi, 7)

# Add land cover layer
try:
    Map.addLayer(landcover.select('LC_Type1').clip(roi), visualization, 'Land Cover for Gujarat')
except Exception as e:
    print(f"Error adding layers to the map: {e}")
    
# Add the classified layer to the map (if needed)
try:
    Map.addLayer(classified_image.clip(roi), classified_vis, 'Classified Land Cover')
except Exception as e:
    print(f"Error adding layers to the map: {e}")

Map

# Define the output filename for the exported vector data
filename = 'training_points.geojson'  # Change the filename and format as needed

# Export the training points to a GeoJSON file
try:
    geemap.ee_export_vector(
        ee_object=training_points,
        filename=filename
    )
    print("Export of training points started successfully.")
except Exception as e:
    print(f"Error during export: {e}")