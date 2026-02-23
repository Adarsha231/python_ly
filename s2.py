import numpy as np

downloads = np.array([
    [1500, 2200, 1800],
    [3000, 1900, 2500],
    [1700, 2100, 1600]
])

# Double downloads below 2000
downloads[downloads < 2000] *= 2

# Convert to single row
report = downloads.flatten()

print("Updated Downloads:\n", downloads)
print("\nSingle Row Format:\n", report)