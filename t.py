import numpy as np

# Initial traffic flow matrix (vehicles per cycle)
# Rows: Incoming direction (NS, EW)
# Columns: Outgoing direction (NS, EW)
traffic_matrix = np.array([
    [120, 30],
    [40, 100]
])

print("Initial Traffic Matrix:")
print(traffic_matrix)

# Signal optimization transformation matrix
signal_matrix = np.array([
    [0.9, 0.1],
    [0.2, 0.8]
])

print("\nSignal Optimization Matrix:")
print(signal_matrix)

# Apply transformation
optimized_traffic = signal_matrix @ traffic_matrix

print("\nTraffic Matrix After Signal Optimization:")
print(optimized_traffic)

# Traffic analysis
total_before = np.sum(traffic_matrix)
total_after = np.sum(optimized_traffic)

print("\nTotal Traffic Before Optimization:", total_before)
print("Total Traffic After Optimization:", total_after)

# Direction-wise flow
ns_flow_before = np.sum(traffic_matrix[0])
ew_flow_before = np.sum(traffic_matrix[1])

ns_flow_after = np.sum(optimized_traffic[0])
ew_flow_after = np.sum(optimized_traffic[1])

print("\nBefore Optimization:")
print("NS Flow:", ns_flow_before)
print("EW Flow:", ew_flow_before)

print("\nAfter Optimization:")
print("NS Flow:", ns_flow_after)
print("EW Flow:", ew_flow_after)