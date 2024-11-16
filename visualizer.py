# Image and 3D point cloud visualization
"""
Quality:
Defines if the depth map is a good candidate for 3D reconstruction
high = 1
low = 0

Accuracy:
Defines if the depth map point are accurate within the physical world or relatively to each other
absolute = 1
relative = 0
"""

import pyvista as pv
import matplotlib.pyplot as plt
import numpy as np
import json
import io
from PIL import Image
import base64

# Load the JSON file
with open("Captures/capture_2024-11-16_16:23:22.json", "r") as file:
    # Get json object
    json_data = json.load(file)

    # Get and decode image data
    base64_string = json_data["image"]
    image_data = base64.b64decode(base64_string)
    image = Image.open(io.BytesIO(image_data))

    # Get point cloud
    point_cloud = json_data["point-cloud"]

# Show image
plt.imshow(image)
plt.show()

### Visualize point cloud
# Create a PyVista PointSet from the data
points = pv.PolyData(point_cloud)

# Compute euclidean distance of each point from the origin
origin = np.array([0.0, 0.0, 0.0])
distances = np.linalg.norm(point_cloud - origin, axis=1)

# Store the distances as a point array to use for coloring
points.point_data["Distance"] = distances

# Create the plotter for interactive visualization
plotter = pv.Plotter()
plotter.add_mesh(points, scalars="Distance", cmap="viridis", point_size=3)

# Add axes to the plot
plotter.add_axes()

# Display the interactive plot
plotter.show()
