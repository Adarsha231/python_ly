import numpy as np

# Weekly rainfall data (in mm)
rainfall = np.array([12, 18, 10, 22, 15, 20, 16])

# Student exam scores
scores = np.array([78, 85, 90, 88, 76, 95, 89])

# Temperature data (in degree Celsius)
temperature = np.array([30, 32, 31, 29, 35, 33, 34])

# Rainfall standard deviation
rain_std = np.std(rainfall)

# Mean and median of student scores
score_mean = np.mean(scores)
score_median = np.median(scores)

# Temperature statistics
temp_mean = np.mean(temperature)
temp_variance = np.var(temperature)
temp_std = np.std(temperature)

print("Weekly Rainfall Data:", rainfall)
print("Standard Deviation of Rainfall:", rain_std)

print("\nStudent Scores:", scores)
print("Mean of Scores:", score_mean)
print("Median of Scores:", score_median)

print("\nTemperature Data:", temperature)
print("Mean Temperature:", temp_mean)
print("Variance of Temperature:", temp_variance)
print("Standard Deviation of Temperature:", temp_std)