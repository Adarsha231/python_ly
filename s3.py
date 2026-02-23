import numpy as np

collection = np.array([
    [5000, 5200, 5400],
    [4800, 5100, 5300],
    [4500, 4700, 4900]
])

# Add 1000 to Day 1 collections (column index 0)
collection[:, 0] += 1000

# Convert to single row
report = collection.reshape(1, -1)

print("Updated Ticket Collection:\n", collection)
print("\nSingle Row Report:\n", report)