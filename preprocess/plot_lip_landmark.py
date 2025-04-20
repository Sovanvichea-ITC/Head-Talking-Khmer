
import numpy as np
import matplotlib.pyplot as plt
import os

# Load the landmark file
landmark_file_path = "../data_root_test/lrs2_landmarks/6392525815109495392/00001/10.npy"
landmark_data = np.load(landmark_file_path, allow_pickle=True).item()

# Extract content_landmarks
content_landmarks = landmark_data["content_landmarks"]
content_array = np.array(content_landmarks)

# Plot
plt.figure(figsize=(6, 6))
plt.scatter(content_array[:, 1], 1 - content_array[:, 2], c='red', label="Lip Points")
for idx, x, y in content_array:
    plt.text(x, 1 - y, str(int(idx)), fontsize=8, ha='center')

plt.title("2D Lip Landmarks (Normalized Coordinates)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.gca().set_aspect('equal')
plt.tight_layout()

# Save figure
output_path = os.path.join(os.getcwd(), "lip_landmarks_plot.png")
plt.savefig(output_path)
print(f"✅ Plot saved as: {output_path}")
