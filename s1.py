import numpy as np

usage = np.array([
    [300, 320, 350],
    [280, 300, 330],
    [260, 290, 310]
])

# Increase Month 3 usage by 20% (column index 2)
usage[:, 2] = usage[:, 2] * 1.2

# Convert to single row
report = usage.reshape(1, -1)

print("Updated Electricity Usage:\n", usage)
print("\nSingle Row Report:\n", report)